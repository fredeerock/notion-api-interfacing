#!/usr/bin/env python3
"""
Simple Notion Database Query Script

This script provides simple functions to query your Notion database.
Perfect for use with VS Code chatbot - you can ask the chatbot to help
you write specific queries using these functions.

Usage: 
- Run interactively: python simple_query.py
- Import in VS Code: from simple_query import *
"""

import requests
import json
import os
from datetime import datetime
from collections import Counter, defaultdict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
DATABASE_ID = os.getenv("DATABASE_ID")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_API_URL = "https://api.notion.com/v1"

# Check if required environment variables are set
if not DATABASE_ID or not NOTION_TOKEN:
    print("❌ Error: Missing required environment variables.")
    print("Please make sure DATABASE_ID and NOTION_TOKEN are set in your .env file.")
    exit(1)

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Global cache for pages
_cached_pages = None

def load_all_pages():
    """Load all pages from the database and cache them."""
    global _cached_pages
    
    if _cached_pages is not None:
        return _cached_pages
    
    print("Loading pages from Notion database...")
    
    all_pages = []
    has_more = True
    next_cursor = None
    
    while has_more:
        query_data = {"page_size": 100}
        if next_cursor:
            query_data["start_cursor"] = next_cursor
        
        response = requests.post(
            f"{NOTION_API_URL}/databases/{DATABASE_ID}/query",
            headers=HEADERS,
            json=query_data
        )
        
        if response.status_code != 200:
            print(f"Error loading pages: {response.status_code}")
            return []
        
        data = response.json()
        all_pages.extend(data.get("results", []))
        
        has_more = data.get("has_more", False)
        next_cursor = data.get("next_cursor")
    
    _cached_pages = all_pages
    print(f"Loaded {len(all_pages)} pages")
    return all_pages

def get_property(page, property_name):
    """Get the value of a property from a page."""
    properties = page.get("properties", {})
    prop = properties.get(property_name, {})
    prop_type = prop.get("type")
    
    if prop_type == "title":
        items = prop.get("title", [])
        return " ".join([item.get("plain_text", "") for item in items])
    elif prop_type == "rich_text":
        items = prop.get("rich_text", [])
        return " ".join([item.get("plain_text", "") for item in items])
    elif prop_type == "select":
        select_item = prop.get("select")
        return select_item.get("name") if select_item else None
    elif prop_type == "date":
        date_item = prop.get("date")
        return date_item.get("start") if date_item else None
    elif prop_type == "checkbox":
        return prop.get("checkbox", False)
    elif prop_type == "url":
        return prop.get("url")
    else:
        return None

def count_total():
    """Count total entries in database."""
    pages = load_all_pages()
    return len(pages)

def count_by_category():
    """Count entries by category."""
    pages = load_all_pages()
    counts = Counter()
    
    for page in pages:
        category = get_property(page, "Category")
        if category:
            counts[category] += 1
    
    return counts

def search_text(search_term):
    """Search for text in names and descriptions."""
    pages = load_all_pages()
    matches = []
    search_term = search_term.lower()
    
    for page in pages:
        name = get_property(page, "Name") or ""
        description = get_property(page, "Description") or ""
        
        if search_term in name.lower() or search_term in description.lower():
            matches.append({
                'name': name,
                'description': description,
                'category': get_property(page, "Category"),
                'date': get_property(page, "Date"),
                'role': get_property(page, "Role"),
                'page': page
            })
    
    return matches

def filter_by_category(category_filter):
    """Filter pages by category (partial match)."""
    pages = load_all_pages()
    matches = []
    
    for page in pages:
        category = get_property(page, "Category")
        if category and category_filter.lower() in category.lower():
            matches.append({
                'name': get_property(page, "Name"),
                'description': get_property(page, "Description"),
                'category': category,
                'date': get_property(page, "Date"),
                'role': get_property(page, "Role"),
                'page': page
            })
    
    return matches

def count_graduate_committees():
    """Count graduate committee entries."""
    # Search by category
    category_matches = filter_by_category("Graduate Committees")
    # Search by text
    text_matches = search_text("graduate committee")
    
    # Combine and deduplicate
    all_ids = set()
    unique_matches = []
    
    for match in category_matches + text_matches:
        page_id = match['page']['id']
        if page_id not in all_ids:
            all_ids.add(page_id)
            unique_matches.append(match)
    
    return len(unique_matches), unique_matches

def get_entries_by_year():
    """Get entries grouped by year."""
    pages = load_all_pages()
    year_data = defaultdict(list)
    
    for page in pages:
        date_str = get_property(page, "Date")
        if date_str:
            try:
                year = datetime.fromisoformat(date_str).year
                year_data[year].append({
                    'name': get_property(page, "Name"),
                    'category': get_property(page, "Category"),
                    'date': date_str,
                    'page': page
                })
            except:
                continue
    
    return dict(year_data)

def print_results(results, title="Results"):
    """Pretty print results."""
    print(f"\n{title}")
    print("=" * len(title))
    
    if isinstance(results, dict):
        for key, value in results.items():
            if isinstance(value, list):
                print(f"{key}: {len(value)} entries")
            else:
                print(f"{key}: {value}")
    elif isinstance(results, list):
        print(f"Found {len(results)} entries:")
        for item in results:
            if isinstance(item, dict):
                print(f"  • {item.get('name', 'Untitled')} ({item.get('category', 'No category')})")
            else:
                print(f"  • {item}")
    else:
        print(results)

# Quick analysis functions for common queries
def quick_graduate_committees():
    """Quick analysis: Graduate committees."""
    count, matches = count_graduate_committees()
    print(f"\n🎓 Graduate Committees: {count} entries")
    for match in matches:
        print(f"  • {match['name']} ({match['date'] or 'No date'})")

def quick_teaching_summary():
    """Quick analysis: Teaching activities."""
    teaching = filter_by_category("1.2")
    print(f"\n👨‍🏫 Teaching Activities: {len(teaching)} entries")
    
    # Group by subcategory
    subcategories = Counter()
    for item in teaching:
        subcategories[item['category']] += 1
    
    for category, count in subcategories.most_common():
        print(f"  {count:2d} - {category}")

def quick_scholarship_summary():
    """Quick analysis: Scholarship activities."""
    scholarship = filter_by_category("1.3")
    print(f"\n📚 Scholarship Activities: {len(scholarship)} entries")
    
    # Group by subcategory
    subcategories = Counter()
    for item in scholarship:
        subcategories[item['category']] += 1
    
    for category, count in subcategories.most_common():
        print(f"  {count:2d} - {category}")

def quick_service_summary():
    """Quick analysis: Service activities."""
    service = filter_by_category("1.4")
    print(f"\n🤝 Service Activities: {len(service)} entries")
    
    # Group by subcategory
    subcategories = Counter()
    for item in service:
        subcategories[item['category']] += 1
    
    for category, count in subcategories.most_common():
        print(f"  {count:2d} - {category}")

if __name__ == "__main__":
    print("🔍 Simple Notion Database Query Tool")
    print("\nRunning quick analysis...")
    
    print(f"\n📊 Total entries: {count_total()}")
    
    quick_graduate_committees()
    quick_teaching_summary()
    quick_scholarship_summary()
    quick_service_summary()
    
    print("\n" + "="*50)
    print("💡 You can also import this script and use functions like:")
    print("   - count_graduate_committees()")
    print("   - search_text('your search term')")
    print("   - filter_by_category('category name')")
    print("   - get_entries_by_year()")
    print("\nOr ask VS Code chatbot to help write custom queries!")
