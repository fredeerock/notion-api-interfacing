#!/usr/bin/env python3
"""
Clean up Sample Academic Entries from Notion database
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
DATABASE_ID = os.getenv("DATABASE_ID")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_API_URL = "https://api.notion.com/v1"

# Headers for Notion API
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_all_pages():
    """Get all pages from the database"""
    pages = []
    start_cursor = None
    
    while True:
        # Build query parameters
        params = {"page_size": 100}
        if start_cursor:
            params["start_cursor"] = start_cursor
        
        # Make request to get database pages
        response = requests.post(
            f"{NOTION_API_URL}/databases/{DATABASE_ID}/query",
            headers=HEADERS,
            json=params
        )
        
        if response.status_code != 200:
            print(f"Error getting pages: {response.status_code}")
            print(response.text)
            break
        
        data = response.json()
        pages.extend(data.get("results", []))
        
        # Check if there are more pages
        if not data.get("has_more", False):
            break
        
        start_cursor = data.get("next_cursor")
    
    return pages

def delete_page(page_id):
    """Delete a page by moving it to trash"""
    response = requests.patch(
        f"{NOTION_API_URL}/pages/{page_id}",
        headers=HEADERS,
        json={"archived": True}
    )
    
    return response.status_code == 200

def main():
    print("🧹 Cleaning up Sample Academic Entries...")
    
    # Get all pages
    pages = get_all_pages()
    print(f"Found {len(pages)} total pages")
    
    # Find sample entries
    sample_entries = []
    for page in pages:
        title_prop = page.get("properties", {}).get("Name", {})
        if title_prop.get("type") == "title":
            title_text = ""
            for text_obj in title_prop.get("title", []):
                title_text += text_obj.get("text", {}).get("content", "")
            
            if title_text == "Sample Academic Entry":
                sample_entries.append({
                    "id": page["id"],
                    "title": title_text
                })
    
    print(f"Found {len(sample_entries)} Sample Academic Entries to delete")
    
    if len(sample_entries) == 0:
        print("No Sample Academic Entries found!")
        return
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to delete {len(sample_entries)} Sample Academic Entries? (y/N): ")
    if confirm.lower() != 'y':
        print("Cancelled.")
        return
    
    # Delete the entries
    deleted_count = 0
    for entry in sample_entries:
        print(f"Deleting: {entry['title']} (ID: {entry['id']})")
        if delete_page(entry["id"]):
            deleted_count += 1
            print("  ✅ Deleted")
        else:
            print("  ❌ Failed to delete")
    
    print(f"\n🎉 Cleanup complete! Deleted {deleted_count}/{len(sample_entries)} Sample Academic Entries")

if __name__ == "__main__":
    main()
