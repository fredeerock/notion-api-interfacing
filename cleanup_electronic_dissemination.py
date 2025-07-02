#!/usr/bin/env python3
"""
Clean up Electronic Dissemination entries to re-add them with proper formatting
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_ID = os.getenv("DATABASE_ID")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_API_URL = "https://api.notion.com/v1"

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_all_pages():
    """Retrieve all pages from the database."""
    all_pages = []
    start_cursor = None
    
    while True:
        url = f"{NOTION_API_URL}/databases/{DATABASE_ID}/query"
        payload = {"page_size": 100}
        
        if start_cursor:
            payload["start_cursor"] = start_cursor
        
        response = requests.post(url, headers=HEADERS, json=payload)
        
        if response.status_code != 200:
            print(f"Error retrieving pages: {response.status_code}")
            print(response.text)
            break
        
        data = response.json()
        all_pages.extend(data.get("results", []))
        
        if not data.get("has_more", False):
            break
        
        start_cursor = data.get("next_cursor")
    
    return all_pages

def delete_page(page_id):
    """Delete a page by setting it as archived."""
    url = f"{NOTION_API_URL}/pages/{page_id}"
    payload = {"archived": True}
    
    response = requests.patch(url, headers=HEADERS, json=payload)
    return response.status_code == 200

def main():
    print("🧹 Cleaning up Electronic Dissemination entries...")
    
    pages = get_all_pages()
    print(f"Found {len(pages)} total pages")
    
    electronic_entries = []
    for page in pages:
        try:
            # Check category
            category_prop = page.get("properties", {}).get("Category", {})
            if category_prop.get("type") == "select":
                category = category_prop.get("select", {})
                if category and "1.3.1.7 Electronic dissemination of research" in category.get("name", ""):
                    title_prop = page.get("properties", {}).get("Name", {})
                    if title_prop.get("type") == "title":
                        title_content = title_prop.get("title", [])
                        if title_content:
                            title = title_content[0].get("text", {}).get("content", "")
                            electronic_entries.append({
                                "id": page["id"],
                                "title": title
                            })
        except Exception as e:
            print(f"Error processing page: {e}")
            continue
    
    if not electronic_entries:
        print("No Electronic Dissemination entries found!")
        return
    
    print(f"Found {len(electronic_entries)} Electronic Dissemination entries to delete")
    
    for entry in electronic_entries:
        print(f"Deleting: {entry['title']}")
        if delete_page(entry["id"]):
            print(f"✅ Deleted: {entry['title']}")
        else:
            print(f"❌ Failed to delete: {entry['title']}")
    
    print("✨ Cleanup complete!")

if __name__ == "__main__":
    main()
