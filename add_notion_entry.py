#!/usr/bin/env python3
"""
Notion Database Entry Script - Backend Utility Only

This script is a backend utility for adding entries to your Notion database.
It ONLY accepts data via command-line arguments from other scripts.
Direct/hardcoded data entry is not allowed.

Usage: 
  python add_notion_entry.py --title "Title" --category "Category" --date "2025-01-01" --location "Location" --description "Description" [--url "URL"] [--role "Role"]

This script should ONLY be called by other batch scripts. To add entries:
1. Create a new batch script (e.g., batch_add_your_data.py)
2. Have that script call this one with the appropriate arguments
"""

import requests
import json
import os
import argparse
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


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Add an entry to Notion database')
    parser.add_argument('--title', required=True, help='Title of the entry')
    parser.add_argument('--category', required=True, help='Category of the entry')
    parser.add_argument('--date', required=True, help='Date in YYYY-MM-DD format')
    parser.add_argument('--location', required=True, help='Location of the entry')
    parser.add_argument('--description', required=True, help='Description of the entry')
    parser.add_argument('--url', required=False, help='Optional URL')
    parser.add_argument('--role', required=False, help='Role (PI, Co-PI, Presenter, etc.)')
    return parser.parse_args()


def create_notion_page(entry_data):
    """Create a new page in the Notion database with the specified data."""
    
    # Build the page content blocks
    children = []
    for content_item in entry_data.get("page_content", []):
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
    
    # Add properties based on what's provided in entry_data
    if "Name" in entry_data:
        page_data["properties"]["Name"] = {
            "title": [{
                "text": {"content": entry_data["Name"]}
            }]
        }
    
    if "Description" in entry_data:
        page_data["properties"]["Description"] = {
            "rich_text": [{
                "text": {"content": entry_data["Description"]}
            }]
        }
    
    if "Category" in entry_data:
        page_data["properties"]["Category"] = {
            "select": {"name": entry_data["Category"]}
        }
    
    if "Location" in entry_data and entry_data["Location"]:
        page_data["properties"]["Location"] = {
            "select": {"name": entry_data["Location"]}
        }
    
    if "Role" in entry_data and entry_data["Role"]:
        page_data["properties"]["Role"] = {
            "select": {"name": entry_data["Role"]}
        }
    
    if "Date" in entry_data:
        page_data["properties"]["Date"] = {
            "date": {"start": entry_data["Date"]}
        }
    
    if "URL" in entry_data:
        page_data["properties"]["URL"] = {
            "url": entry_data["URL"]
        }
    
    if "Show Page Contents" in entry_data:
        page_data["properties"]["Show Page Contents"] = {
            "checkbox": entry_data["Show Page Contents"]
        }
    
    if "Pinned" in entry_data:
        page_data["properties"]["Pinned"] = {
            "checkbox": entry_data["Pinned"]
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
        print(f"   Title: {entry_data['Name']}")
        return True
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
        return False


def main():
    """Main function to run the script."""
    try:
        args = parse_arguments()
        
        # Build entry data from command-line arguments
        entry_data = {
            "Name": args.title,
            "Description": args.description,
            "Category": args.category,
            "Location": args.location,
            "Date": args.date,
            "Show Page Contents": False,
            "Pinned": False,
            "page_content": []
        }
        
        # Add optional fields
        if args.url:
            entry_data["URL"] = args.url
        if args.role:
            entry_data["Role"] = args.role
            
        print("🚀 Adding entry to Notion database...")
        print(f"   Database ID: {DATABASE_ID}")
        print(f"   Entry Name: {entry_data['Name']}")
        print()
        
        create_notion_page(entry_data)
        
    except SystemExit as e:
        # argparse calls sys.exit() when help is displayed or arguments are missing
        if e.code != 0:  # Only show error for non-help exits
            print("\n❌ Error: This script requires all required arguments to be provided.")
            print("This is a backend utility and should only be called by other batch scripts.")
            print("\nTo add entries to your Notion database:")
            print("1. Create a new batch script (e.g., batch_add_your_data.py)")
            print("2. Have that script call this one with the appropriate arguments")
            print("\nExample:")
            print('python add_notion_entry.py --title "My Entry" --category "Scholarship" --date "2025-01-01" --location "Baton Rouge LA" --description "My description"')
        raise


if __name__ == "__main__":
    main()
