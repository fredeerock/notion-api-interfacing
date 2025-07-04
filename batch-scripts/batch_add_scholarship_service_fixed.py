#!/usr/bin/env python3
"""
Batch script to add the remaining scholarship entries that failed due to comma issues in category names.
This script fixes the category names to be compatible with Notion's select field requirements.
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

# Fixed entries with corrected category names (no commas)
FIXED_SCHOLARSHIP_ENTRIES = [
    # 1.3.1.6 Exhibition Catalogs (fixed category name)
    {
        "Name": "LSU is on the Frontier of Virtual Production",
        "Description": "Newspaper Article, Jordan LaHaye Fontenot, Country Roads, 26 Oct 2023, available at https://countryroadsmagazine.com/art-and-culture/visual-performing-arts/lsu-is-on-the-frontier-of-virtual-production.",
        "Category": "1.3.1.6 Exhibition Catalogs and Reviews",
        "Location": "Baton Rouge LA",
        "Date": "2023-01-01",
        "URL": "https://countryroadsmagazine.com/art-and-culture/visual-performing-arts/lsu-is-on-the-frontier-of-virtual-production",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "How is Baton Rouge's recent film boom impacting city culture?",
        "Description": "Newspaper Article, Domenic Purdy, 225 Magazine, 30 Jan 2023, available at https://www.225batonrouge.com/our-city/baton-rouges-recent-film-boom-impacting-city-culture.",
        "Category": "1.3.1.6 Exhibition Catalogs and Reviews",
        "Location": "Baton Rouge LA",
        "Date": "2023-01-01",
        "URL": "https://www.225batonrouge.com/our-city/baton-rouges-recent-film-boom-impacting-city-culture",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "New Technologies Training Next Generation of Filmmakers",
        "Description": "Newspaper Article, Domenic Purdy, 225 Magazine, 06 Oct 2022, available at https://www.225batonrouge.com/our-city/new-technologies-training-next-generation-filmmakers-live-work-right-louisiana.",
        "Category": "1.3.1.6 Exhibition Catalogs and Reviews",
        "Location": "Baton Rouge LA",
        "Date": "2022-01-01",
        "URL": "https://www.225batonrouge.com/our-city/new-technologies-training-next-generation-filmmakers-live-work-right-louisiana",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.4 Professional Meetings (fixed category name)
    {
        "Name": "Digital Twin Fundamentals in Manufacturing Presentation",
        "Description": "Digital Twin Fundamentals in Manufacturing: Building an Industrial Twin of Twins for NASA, Digital Twin Consortium Q1 Member Meeting, Presentation by Greg Porter on behalf of Louisiana State University collaboration.",
        "Category": "1.3.4 Professional Meetings and Conferences",
        "Location": "Baton Rouge LA",
        "Role": "Presenter",
        "Date": "2024-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Digital Twin Consortium Panel - NASA Digital Twin Project",
        "Description": "Digital Twin Consortium Panel - NASA Digital Twin Project, invited speaker, 14 Dec 2023, Derick Ostrenko, Marc Aubanel, Jason Jamerson.",
        "Category": "1.3.4 Professional Meetings and Conferences",
        "Location": "Baton Rouge LA",
        "Role": "Presenter",
        "Date": "2023-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "ACM SIGGRAPH Immersive Expressions Panel Chair",
        "Description": "ACM SIGGRAPH. Panel Session of the ACM SIGGRAPH Digital Arts Community. 'Immersive Expressions: Virtual Reality on the Web.' Panel Chair. Los Angeles, CA.",
        "Category": "1.3.4 Professional Meetings and Conferences",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2017-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.4.4.1 Advisory boards (fixed category name)
    {
        "Name": "Museum of Science & Industry Advisory Council on STEAM Zone",
        "Description": "Museum of Science & Industry Advisory Council on Science, Technology, Art, Engineering, and Math (STEAM) Zone, Tampa, FL, Member.",
        "Category": "1.4.4.1 Advisory Boards and Commissions",
        "Location": "Baton Rouge LA",
        "Date": "2013-01-01",
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
    """Main function to run the batch script for failed entries."""
    print("🚀 Adding remaining scholarship and service entries with fixed category names...")
    print(f"   Database ID: {DATABASE_ID}")
    print(f"   Total entries to add: {len(FIXED_SCHOLARSHIP_ENTRIES)}")
    print("-" * 60)
    
    success_count = 0
    category_counts = {}
    
    for i, entry in enumerate(FIXED_SCHOLARSHIP_ENTRIES, 1):
        print(f"[{i}/{len(FIXED_SCHOLARSHIP_ENTRIES)}] Adding: {entry['Name']}")
        
        if create_notion_page(entry):
            success_count += 1
            category = entry['Category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        print()  # Add spacing between entries
    
    print("-" * 60)
    print(f"Completed! Successfully added {success_count}/{len(FIXED_SCHOLARSHIP_ENTRIES)} entries.")
    
    # Show breakdown by category
    if category_counts:
        print(f"📊 Category breakdown:")
        for category, count in sorted(category_counts.items()):
            print(f"   • {category}: {count}")
    
    if success_count < len(FIXED_SCHOLARSHIP_ENTRIES):
        print("⚠️  Some entries failed to add. Check the error messages above.")
    else:
        print("🎉 All remaining scholarship and service entries added successfully!")


if __name__ == "__main__":
    main()
