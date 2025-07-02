#!/usr/bin/env python3
"""
Download Notion Database Script

This script downloads the entire contents of your Notion database to a JSON file.
Useful for backup, analysis, and getting context about your database contents.

Usage: python download_notion_database.py
"""

import requests
import json
import os
from datetime import datetime
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

def get_database_info():
    """Get database schema information."""
    url = f"{NOTION_API_URL}/databases/{DATABASE_ID}"
    
    try:
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error getting database info:")
            print(f"   Status Code: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error getting database info: {str(e)}")
        return None

def get_all_pages():
    """Get all pages from the database."""
    url = f"{NOTION_API_URL}/databases/{DATABASE_ID}/query"
    
    all_pages = []
    has_more = True
    next_cursor = None
    
    while has_more:
        # Prepare the request body
        body = {
            "page_size": 100  # Maximum page size
        }
        
        if next_cursor:
            body["start_cursor"] = next_cursor
        
        try:
            response = requests.post(url, headers=HEADERS, json=body)
            
            if response.status_code == 200:
                data = response.json()
                all_pages.extend(data.get("results", []))
                
                has_more = data.get("has_more", False)
                next_cursor = data.get("next_cursor")
                
                print(f"📄 Retrieved {len(data.get('results', []))} pages (Total: {len(all_pages)})")
                
            else:
                print(f"❌ Error querying database:")
                print(f"   Status Code: {response.status_code}")
                print(f"   Response: {response.text}")
                break
                
        except Exception as e:
            print(f"❌ Error querying database: {str(e)}")
            break
    
    return all_pages

def get_page_content(page_id):
    """Get the content blocks of a specific page."""
    url = f"{NOTION_API_URL}/blocks/{page_id}/children"
    
    try:
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
        else:
            print(f"⚠️  Warning: Could not get content for page {page_id}")
            return []
            
    except Exception as e:
        print(f"⚠️  Warning: Error getting content for page {page_id}: {str(e)}")
        return []

def process_pages_with_content(pages):
    """Add content blocks to each page."""
    processed_pages = []
    
    for i, page in enumerate(pages, 1):
        page_id = page.get("id", "")
        page_title = ""
        
        # Extract page title
        if "properties" in page and "Name" in page["properties"]:
            title_prop = page["properties"]["Name"]
            if "title" in title_prop and title_prop["title"]:
                page_title = title_prop["title"][0].get("text", {}).get("content", "Untitled")
        
        print(f"🔍 [{i}/{len(pages)}] Processing: {page_title[:50]}...")
        
        # Get page content
        content = get_page_content(page_id)
        page["content_blocks"] = content
        
        processed_pages.append(page)
    
    return processed_pages

def save_to_json(data, filename):
    """Save data to a JSON file with pretty formatting."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"💾 Saved to: {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving to file: {str(e)}")
        return False

def create_summary(database_info, pages):
    """Create a summary of the database contents."""
    summary = {
        "total_pages": len(pages),
        "categories": {},
        "years": {},
        "locations": {}
    }
    
    for page in pages:
        properties = page.get("properties", {})
        
        # Count by category
        if "Category" in properties and properties["Category"].get("select"):
            category = properties["Category"]["select"]["name"]
            summary["categories"][category] = summary["categories"].get(category, 0) + 1
        
        # Count by year
        if "Date" in properties and properties["Date"].get("date"):
            date_str = properties["Date"]["date"]["start"]
            year = date_str[:4] if date_str else "Unknown"
            summary["years"][year] = summary["years"].get(year, 0) + 1
        
        # Count by location
        if "Location" in properties and properties["Location"].get("select"):
            location = properties["Location"]["select"]["name"]
            summary["locations"][location] = summary["locations"].get(location, 0) + 1
    
    return summary

def main():
    """Main function to download the database."""
    print("🚀 Downloading Notion database contents...")
    print(f"   Database ID: {DATABASE_ID}")
    print("-" * 60)
    
    # Get database schema
    print("📋 Getting database schema...")
    database_info = get_database_info()
    if not database_info:
        print("❌ Failed to get database information. Exiting.")
        return
    
    # Get all pages
    print("📄 Getting all pages...")
    pages = get_all_pages()
    if not pages:
        print("❌ No pages found or failed to retrieve pages. Exiting.")
        return
    
    print(f"✅ Retrieved {len(pages)} pages")
    
    # Get content for each page
    print("🔍 Getting page contents...")
    pages_with_content = process_pages_with_content(pages)
    
    # Create summary
    summary = create_summary(database_info, pages_with_content)
    
    # Prepare final data structure
    export_data = {
        "export_info": {
            "timestamp": datetime.now().isoformat(),
            "database_id": DATABASE_ID,
            "total_pages": len(pages_with_content)
        },
        "database_schema": database_info,
        "summary": summary,
        "pages": pages_with_content
    }
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"notion_database_export_{timestamp}.json"
    
    # Save to file
    print("💾 Saving to JSON file...")
    if save_to_json(export_data, filename):
        print("-" * 60)
        print("🎉 Database export completed successfully!")
        print(f"📁 File: {filename}")
        print(f"📊 Summary:")
        print(f"   Total pages: {summary['total_pages']}")
        print(f"   Categories: {len(summary['categories'])}")
        print(f"   Years: {len(summary['years'])}")
        print(f"   Locations: {len(summary['locations'])}")
        
        # Show top categories
        if summary['categories']:
            print(f"   Top categories:")
            sorted_categories = sorted(summary['categories'].items(), key=lambda x: x[1], reverse=True)
            for cat, count in sorted_categories[:5]:
                print(f"     • {cat}: {count}")
    else:
        print("❌ Export failed!")

if __name__ == "__main__":
    main()
