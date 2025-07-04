#!/usr/bin/env python3
"""
Batch script to add awards and grants entries to Notion database.
This script adds entries under "1.2.6 Awards and Recognition" and 
"1.2.7 Teaching-Related Research/Grants".

Based on add_notion_entry.py structure.
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

# Awards and grants entries
ENTRIES = [
    # Awards Section
    {
        "Name": "Nominated for the LSU Alumni Association Faculty Excellence Award",
        "Description": "Nominated for the LSU Alumni Association Faculty Excellence Award in recognition of outstanding teaching achievement.",
        "Category": "1.2.6 Awards and Recognition",
        "Location": "Baton Rouge LA",
        "Date": "2024-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Received the LSU Tiger Athletic Foundation Outstanding Teacher Award",
        "Description": "Received the LSU Tiger Athletic Foundation Outstanding Teacher Award in recognition of outstanding teaching achievement.",
        "Category": "1.2.6 Awards and Recognition",
        "Location": "Baton Rouge LA",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Nominated for LSU Tiger Athletic Foundation Outstanding Teacher Award",
        "Description": "Nominated for LSU Tiger Athletic Foundation Outstanding Teacher Award in recognition of outstanding teaching achievement.",
        "Category": "1.2.6 Awards and Recognition",
        "Location": "Baton Rouge LA",
        "Date": "2012-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "The Sheridan Center for Teaching & Learning: Collegiate Teaching Certificate I",
        "Description": "The Sheridan Center for Teaching & Learning: Collegiate Teaching Certificate I: Reflective Teaching, Brown University.",
        "Category": "1.2.6 Awards and Recognition",
        "Location": "Providence RI",
        "Date": "2010-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # Grants Section
    {
        "Name": "Efficiency and Innovation for the Multimodal Studio",
        "Description": "LSU Student Technology Fee Grant, $115,232.77, Co-PI.",
        "Category": "1.2.7 Teaching-Related Research/Grants",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2021-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Mixed Reality Garage: Labs for the future of Art and Design",
        "Description": "LSU Student Technology Fee Grant, $116,550, Co-PI.",
        "Category": "1.2.7 Teaching-Related Research/Grants",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2018-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "LSU Robotics = Engineering + Art + Design",
        "Description": "LSU Student Technology Fee Grant, $78,025, Co-PI.",
        "Category": "1.2.7 Teaching-Related Research/Grants",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2018-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "IndieGeauxGeaux",
        "Description": "LSU Student Technology Fee Grant, $114,943, Co-PI.",
        "Category": "1.2.7 Teaching-Related Research/Grants",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2015-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "CoAD Fabrication Factory & 21st Century Studios",
        "Description": "LSU Student Technology Fee Grant, $173,574, Co-PI.",
        "Category": "1.2.7 Teaching-Related Research/Grants",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2014-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    }
]


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
    
    if "Location" in entry_data:
        page_data["properties"]["Location"] = {
            "select": {"name": entry_data["Location"]}
        }
    
    if "Role" in entry_data:
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
        print(f"✅ Successfully created: {entry_data['Name']}")
        return True
    else:
        print(f"❌ Failed to create: {entry_data['Name']}")
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
    """Main function to run the batch script."""
    print("🚀 Adding awards and grants entries to Notion database...")
    print(f"   Database ID: {DATABASE_ID}")
    print(f"   Total entries to add: {len(ENTRIES)}")
    print("-" * 60)
    
    success_count = 0
    awards_count = 0
    grants_count = 0
    
    for i, entry in enumerate(ENTRIES, 1):
        print(f"[{i}/{len(ENTRIES)}] Adding: {entry['Name']}")
        
        if create_notion_page(entry):
            success_count += 1
            if "1.2.6" in entry['Category']:
                awards_count += 1
            elif "1.2.7" in entry['Category']:
                grants_count += 1
        
        print()  # Add spacing between entries
    
    print("-" * 60)
    print(f"Completed! Successfully added {success_count}/{len(ENTRIES)} entries.")
    print(f"   Awards (1.2.6): {awards_count}")
    print(f"   Grants (1.2.7): {grants_count}")
    
    if success_count < len(ENTRIES):
        print("⚠️  Some entries failed to add. Check the error messages above.")
    else:
        print("🎉 All awards and grants entries added successfully!")


if __name__ == "__main__":
    main()
