#!/usr/bin/env python3
"""
Notion Database Analysis Script

This script allows you to query and analyze your Notion database.
You can filter by categories, search for specific terms, count entries,
and perform various analytical queries.

Usage: python analyze_database.py
"""

import requests
import json
import os
from datetime import datetime
from collections import Counter, defaultdict
import re
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

# Headers for Notion API
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

class NotionAnalyzer:
    def __init__(self):
        self.all_pages = []
        self.loaded = False
    
    def load_all_pages(self):
        """Load all pages from the database."""
        print("📊 Loading all pages from database...")
        
        all_pages = []
        has_more = True
        next_cursor = None
        
        while has_more:
            # Build query
            query_data = {
                "page_size": 100
            }
            
            if next_cursor:
                query_data["start_cursor"] = next_cursor
            
            # Make API request
            response = requests.post(
                f"{NOTION_API_URL}/databases/{DATABASE_ID}/query",
                headers=HEADERS,
                json=query_data
            )
            
            if response.status_code != 200:
                print(f"❌ Error loading pages: {response.status_code}")
                print(f"   Response: {response.text}")
                return []
            
            data = response.json()
            all_pages.extend(data.get("results", []))
            
            has_more = data.get("has_more", False)
            next_cursor = data.get("next_cursor")
        
        self.all_pages = all_pages
        self.loaded = True
        print(f"✅ Loaded {len(all_pages)} pages from database")
        return all_pages
    
    def get_property_value(self, page, property_name):
        """Extract the value of a property from a page."""
        properties = page.get("properties", {})
        prop = properties.get(property_name, {})
        prop_type = prop.get("type")
        
        if prop_type == "title":
            title_items = prop.get("title", [])
            return " ".join([item.get("plain_text", "") for item in title_items])
        
        elif prop_type == "rich_text":
            text_items = prop.get("rich_text", [])
            return " ".join([item.get("plain_text", "") for item in text_items])
        
        elif prop_type == "select":
            select_item = prop.get("select")
            return select_item.get("name") if select_item else None
        
        elif prop_type == "multi_select":
            multi_select_items = prop.get("multi_select", [])
            return [item.get("name") for item in multi_select_items]
        
        elif prop_type == "date":
            date_item = prop.get("date")
            return date_item.get("start") if date_item else None
        
        elif prop_type == "checkbox":
            return prop.get("checkbox", False)
        
        elif prop_type == "url":
            return prop.get("url")
        
        elif prop_type == "relation":
            relation_items = prop.get("relation", [])
            return [item.get("id") for item in relation_items]
        
        else:
            return None
    
    def filter_by_category(self, category_filter, exact_match=False):
        """Filter pages by category."""
        if not self.loaded:
            self.load_all_pages()
        
        filtered_pages = []
        for page in self.all_pages:
            category = self.get_property_value(page, "Category")
            if category:
                if exact_match:
                    if category == category_filter:
                        filtered_pages.append(page)
                else:
                    if category_filter.lower() in category.lower():
                        filtered_pages.append(page)
        
        return filtered_pages
    
    def search_in_content(self, search_term):
        """Search for a term in names and descriptions."""
        if not self.loaded:
            self.load_all_pages()
        
        matching_pages = []
        search_term = search_term.lower()
        
        for page in self.all_pages:
            name = self.get_property_value(page, "Name") or ""
            description = self.get_property_value(page, "Description") or ""
            
            if (search_term in name.lower() or 
                search_term in description.lower()):
                matching_pages.append(page)
        
        return matching_pages
    
    def count_by_category(self):
        """Count entries by category."""
        if not self.loaded:
            self.load_all_pages()
        
        category_counts = Counter()
        for page in self.all_pages:
            category = self.get_property_value(page, "Category")
            if category:
                category_counts[category] += 1
        
        return category_counts
    
    def count_by_location(self):
        """Count entries by location."""
        if not self.loaded:
            self.load_all_pages()
        
        location_counts = Counter()
        for page in self.all_pages:
            location = self.get_property_value(page, "Location")
            if location:
                location_counts[location] += 1
        
        return location_counts
    
    def count_by_role(self):
        """Count entries by role."""
        if not self.loaded:
            self.load_all_pages()
        
        role_counts = Counter()
        for page in self.all_pages:
            role = self.get_property_value(page, "Role")
            if role:
                role_counts[role] += 1
        
        return role_counts
    
    def get_entries_by_year(self, year=None):
        """Get entries by year, or all years if year is None."""
        if not self.loaded:
            self.load_all_pages()
        
        year_data = defaultdict(list)
        
        for page in self.all_pages:
            date_str = self.get_property_value(page, "Date")
            if date_str:
                try:
                    page_year = datetime.fromisoformat(date_str).year
                    if year is None or page_year == year:
                        year_data[page_year].append(page)
                except:
                    continue
        
        return dict(year_data)
    
    def print_page_summary(self, page):
        """Print a summary of a page."""
        name = self.get_property_value(page, "Name") or "Untitled"
        category = self.get_property_value(page, "Category") or "No category"
        date = self.get_property_value(page, "Date") or "No date"
        role = self.get_property_value(page, "Role") or "No role"
        location = self.get_property_value(page, "Location") or "No location"
        
        print(f"  📄 {name}")
        print(f"     Category: {category}")
        print(f"     Date: {date}")
        print(f"     Role: {role}")
        print(f"     Location: {location}")
        print()


def main():
    """Main function with interactive menu."""
    analyzer = NotionAnalyzer()
    
    while True:
        print("\n" + "="*60)
        print("🔍 NOTION DATABASE ANALYZER")
        print("="*60)
        print("1. Load and count all entries")
        print("2. Count by category")
        print("3. Count by location") 
        print("4. Count by role")
        print("5. Search for specific term")
        print("6. Filter by category")
        print("7. Show entries by year")
        print("8. Graduate committees analysis")
        print("9. Teaching activities analysis")
        print("10. Custom query (describe what you want)")
        print("0. Exit")
        print("-" * 60)
        
        choice = input("Enter your choice (0-10): ").strip()
        
        if choice == "0":
            print("👋 Goodbye!")
            break
        
        elif choice == "1":
            analyzer.load_all_pages()
            print(f"\n📊 Total entries in database: {len(analyzer.all_pages)}")
        
        elif choice == "2":
            print("\n📂 Counting entries by category...")
            counts = analyzer.count_by_category()
            for category, count in counts.most_common():
                print(f"  {count:3d} entries: {category}")
        
        elif choice == "3":
            print("\n🌍 Counting entries by location...")
            counts = analyzer.count_by_location()
            for location, count in counts.most_common():
                print(f"  {count:3d} entries: {location}")
        
        elif choice == "4":
            print("\n👤 Counting entries by role...")
            counts = analyzer.count_by_role()
            for role, count in counts.most_common():
                print(f"  {count:3d} entries: {role}")
        
        elif choice == "5":
            search_term = input("\nEnter search term: ").strip()
            if search_term:
                print(f"\n🔍 Searching for '{search_term}'...")
                matches = analyzer.search_in_content(search_term)
                print(f"Found {len(matches)} matching entries:")
                for page in matches:
                    analyzer.print_page_summary(page)
        
        elif choice == "6":
            category = input("\nEnter category to filter (partial match): ").strip()
            if category:
                print(f"\n📂 Filtering by category containing '{category}'...")
                matches = analyzer.filter_by_category(category)
                print(f"Found {len(matches)} matching entries:")
                for page in matches:
                    analyzer.print_page_summary(page)
        
        elif choice == "7":
            year_input = input("\nEnter year (or press Enter for all years): ").strip()
            year = int(year_input) if year_input.isdigit() else None
            
            year_data = analyzer.get_entries_by_year(year)
            
            if year:
                entries = year_data.get(year, [])
                print(f"\n📅 Entries for {year}: {len(entries)}")
                for page in entries:
                    analyzer.print_page_summary(page)
            else:
                print(f"\n📅 Entries by year:")
                for year in sorted(year_data.keys(), reverse=True):
                    print(f"  {year}: {len(year_data[year])} entries")
        
        elif choice == "8":
            print("\n🎓 Graduate Committees Analysis...")
            # Search for graduate committees
            committee_matches = analyzer.search_in_content("graduate committee")
            category_matches = analyzer.filter_by_category("1.2.1.2.1 Graduate Committees")
            
            # Combine and deduplicate
            all_matches = list({page['id']: page for page in committee_matches + category_matches}.values())
            
            print(f"Found {len(all_matches)} graduate committee entries:")
            for page in all_matches:
                analyzer.print_page_summary(page)
        
        elif choice == "9":
            print("\n👨‍🏫 Teaching Activities Analysis...")
            teaching_matches = analyzer.filter_by_category("1.2")  # All teaching categories
            print(f"Found {len(teaching_matches)} teaching-related entries:")
            
            # Break down by subcategory
            subcategory_counts = Counter()
            for page in teaching_matches:
                category = analyzer.get_property_value(page, "Category")
                if category:
                    subcategory_counts[category] += 1
            
            print("\nBreakdown by teaching category:")
            for category, count in subcategory_counts.most_common():
                print(f"  {count:3d} entries: {category}")
        
        elif choice == "10":
            print("\n💬 Describe what you want to analyze:")
            print("Examples:")
            print("- 'How many presentations have I given?'")
            print("- 'Show me all scholarship activities'")
            print("- 'Count entries by year'")
            print("- 'Find all service activities'")
            
            query = input("\nYour query: ").strip()
            if query:
                print(f"\n🤖 For the query: '{query}'")
                print("Here are some suggestions:")
                
                if "presentation" in query.lower() or "present" in query.lower():
                    matches = analyzer.search_in_content("presentation")
                    role_matches = [p for p in analyzer.all_pages 
                                  if analyzer.get_property_value(p, "Role") == "Presenter"]
                    all_matches = list({page['id']: page for page in matches + role_matches}.values())
                    print(f"Found {len(all_matches)} presentation-related entries")
                
                elif "scholarship" in query.lower():
                    matches = analyzer.filter_by_category("1.3")
                    print(f"Found {len(matches)} scholarship entries")
                
                elif "service" in query.lower():
                    matches = analyzer.filter_by_category("1.4")
                    print(f"Found {len(matches)} service entries")
                
                elif "year" in query.lower():
                    year_data = analyzer.get_entries_by_year()
                    print("Entries by year:")
                    for year in sorted(year_data.keys(), reverse=True):
                        print(f"  {year}: {len(year_data[year])} entries")
                
                else:
                    print("Try using the specific menu options above for detailed analysis.")
        
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
