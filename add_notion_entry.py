#!/usr/bin/env python3
"""
Notion Database Entry Script

This script allows you to easily add entries to your Notion database.
Simply modify the ENTRY_DATA dictionary below with your desired values
and run the script to add a new entry.

Usage: python add_notion_entry.py
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

# ============================================
# MODIFY THIS SECTION FOR EACH NEW ENTRY
# ============================================
ENTRY_DATA = {
    "Name": "Sample Academic Entry", # This is the title of the entry. It should be descriptive and concise. Don't include the year in the title, as it will be added automatically based on the date.  
    "Description": "This is a sample description for the academic entry", # This is a short description of the entry that expands on the title only when necessary.
    "Category": "1. Documentation",  # Choose from available options
    "Location": "Baton Rouge LA",     # This is the location of the item. It should default to Baton Rouge LA.
    "Role": "Presenter",             # Choose from: Presenter, Organizer, Co-organizer, Guest Critic, Guest Lecture or create a new role if needed.
    "Date": "2025-01-01",           # Format: YYYY-MM-DD. If the month and day are not specified, it should default to January 1st of the year.
    "URL": "https://example.com",    # Optional URL
    "Show Page Contents": False,      # True/False checkbox
    "Pinned": False,                # True/False checkbox
    "page_content": [
        {
            "type": "paragraph",
            "text": "This is the main content of the page. You can modify this text." # Content can be added here to further expand on the short description. This should only be used if the description is not sufficient. This should not duplicate the description or title.
        }
    ]
}
# ============================================


def create_notion_page():
    """Create a new page in the Notion database with the specified data."""
    
    # Build the page content blocks
    children = []
    for content_item in ENTRY_DATA.get("page_content", []):
        if content_item["type"] == "paragraph":
            children.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content_item["text"]}
                    }]
                }
            })
        elif content_item["type"] == "heading_2":
            children.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content_item["text"]}
                    }]
                }
            })
        elif content_item["type"] == "heading_1":
            children.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content_item["text"]}
                    }]
                }
            })
        elif content_item["type"] == "heading_3":
            children.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content_item["text"]}
                    }]
                }
            })
    
    # Build the page data
    page_data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {},
        "children": children
    }
    
    # Add properties based on what's provided in ENTRY_DATA
    if "Name" in ENTRY_DATA:
        page_data["properties"]["Name"] = {
            "title": [{
                "text": {"content": ENTRY_DATA["Name"]}
            }]
        }
    
    if "Description" in ENTRY_DATA:
        page_data["properties"]["Description"] = {
            "rich_text": [{
                "text": {"content": ENTRY_DATA["Description"]}
            }]
        }
    
    if "Category" in ENTRY_DATA:
        page_data["properties"]["Category"] = {
            "select": {"name": ENTRY_DATA["Category"]}
        }
    
    if "Location" in ENTRY_DATA:
        page_data["properties"]["Location"] = {
            "select": {"name": ENTRY_DATA["Location"]}
        }
    
    if "Role" in ENTRY_DATA:
        page_data["properties"]["Role"] = {
            "select": {"name": ENTRY_DATA["Role"]}
        }
    
    if "Date" in ENTRY_DATA:
        page_data["properties"]["Date"] = {
            "date": {"start": ENTRY_DATA["Date"]}
        }
    
    if "URL" in ENTRY_DATA:
        page_data["properties"]["URL"] = {
            "url": ENTRY_DATA["URL"]
        }
    
    if "Show Page Contents" in ENTRY_DATA:
        page_data["properties"]["Show Page Contents"] = {
            "checkbox": ENTRY_DATA["Show Page Contents"]
        }
    
    if "Pinned" in ENTRY_DATA:
        page_data["properties"]["Pinned"] = {
            "checkbox": ENTRY_DATA["Pinned"]
        }
    
    # Make the API request
    response = requests.post(
        f"{NOTION_API_URL}/pages",
        headers=HEADERS,
        json=page_data
    )
    
    if response.status_code == 200:
        result = response.json()
        page_id = result.get("id", "Unknown")
        page_url = result.get("url", "Unknown")
        print(f"✅ Successfully created page!")
        print(f"   Page ID: {page_id}")
        print(f"   Page URL: {page_url}")
        print(f"   Title: {ENTRY_DATA['Name']}")
    else:
        print(f"❌ Error creating page:")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        
        # Try to parse error details
        try:
            error_data = response.json()
            if "message" in error_data:
                print(f"   Error Message: {error_data['message']}")
        except:
            pass


def main():
    """Main function to run the script."""
    print("🚀 Adding entry to Notion database...")
    print(f"   Database ID: {DATABASE_ID}")
    print(f"   Entry Name: {ENTRY_DATA['Name']}")
    print()
    
    create_notion_page()


if __name__ == "__main__":
    main()
