#!/usr/bin/env python3
"""
Batch script to add new teaching methods/materials entries to Notion database.
This script adds entries under "1.2.5.3 New Teaching Methods/Material Developed".

Based on add_notion_entry.py structure with updated comments.
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

# Teaching methods/materials entries
# Following updated guidelines:
# - Name: Descriptive and concise, no year in title
# - Description: Short description expanding on title when necessary
# - Location: Defaults to Baton Rouge LA
# - Role: Most appropriate role (PI, Co-PI, Presenter, etc.) when applicable
# - Date: YYYY-MM-DD format, defaults to January 1st if month/day not specified
# - URL: Optional, but if used should also be included in description
# - Show Page Contents: Generally False to avoid duplication
TEACHING_ENTRIES = [
    {
        "Name": "XR Performance Teaching Resources",
        "Description": "Created a range of teaching resources on topics related to 'XR Performance' that coincided with the class taught with the same name.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2022-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Virtual Production Teaching Materials",
        "Description": "In conjunction with the $1,250,000 grant from Louisiana Economic Development on virtual production new material for teaching were developed in house to aid in education of virtual production technologies.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2021-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Creative Coding Teaching Materials",
        "Description": "Created a host of teaching materials and assignment on 'Creative Coding' published at https://lsudigitalart.github.io/2210/.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2019-01-01",
        "URL": "https://lsudigitalart.github.io/2210/",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Virtual Reality Lab Creation",
        "Description": "Led the creation of a Virtual Reality Lab for the creation of content in full room virtual reality.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2016-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "META: Melding Physical and Virtual Technologies Implementation",
        "Description": "Led the implementation of META: Melding the Physical and Virtual through Emerging Technologies in the Arts. An overhaul of two technology labs for hybrid (virtual & physical) creative expression. Made possible by a $75,000 grant from the La. Board of Regents.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2016-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Digital Media Arts and Engineering Lab Creation",
        "Description": "Helped lead the execution of the Digital Media Arts and Engineering Lab creation made possible by a $75,000 grant from the La. Board of Regents.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2015-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Digital Infrastructure Development for CoAD",
        "Description": "Aided in the development of digital infrastructure (upgraded servers, and networking equipment) for CoAD servers, set up file storage for Digital Art Student projects and classroom materials.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2015-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "CAVE2 Immersive VR Environment Content Creation",
        "Description": "Assisting in the creation of content for an upcoming CAVE2 (cave automatic virtual environment) immersive virtual reality environment.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2015-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Integrated Digital Environment for Artists (IDEA) Creation",
        "Description": "Helped lead the creation of the Integrated Digital Environment for Artists (IDEA). A physical space with tools for a common digital workflow between the varied disciplines in the School of Art. Made possible by a $120,000 grant from the La. Board of Regents.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2014-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "LSU Render Farm Pipeline Partnership",
        "Description": "Created a partnership between LSU School of Art, High Performance Computing, and CCT for the development of a render farm pipeline utilizing a 7000-core supercomputer.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2014-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "D+A Media Research Studio Blog",
        "Description": "Created a ongoing research blog for ART 7255 Digital Art Seminar entitled, D+A Media Research Studio, available at https://art7255.wordpress.com/.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2014-01-01",
        "URL": "https://art7255.wordpress.com/",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "High-End Motion Capture Studio",
        "Description": "Created a high-end motion capture studio with 6 infrared cameras.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Poe's Republic of Letters Digital Humanities Project",
        "Description": "Developed 'Poe's Republic of Letters' as a part of a Digital Humanities & Library Science initiative led by Boyd Professor Gerald Kennedy.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Online Selective Admissions Process for Digital Art",
        "Description": "Created new methods an online selective admissions process for digital art students using Slideroom.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Digital Art Community Moodle Page",
        "Description": "Created a Digital Art Community Moodle page for Graduate and Undergraduate students used for assessment and internal communications at http://community.moodle2.lsu.edu/course/view.php?id=24.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2012-01-01",
        "URL": "http://community.moodle2.lsu.edu/course/view.php?id=24",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "New Review Methods for Digital Art Students",
        "Description": "Created new methods for freshmen, junior, and senior review for digital art students within the school of art.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2012-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Online Resource Blogs for Digital Art Classes",
        "Description": "Created online Resource Blogs for the following classes: ART 4560 Interactive Media; ART 4030 Digital Art Senior Project; ART 4059 Digital Media Capstone.",
        "Category": "1.2.5.3 New Teaching Methods/Material Developed",
        "Location": "Baton Rouge LA",
        "Date": "2011-01-01",
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
    print("🚀 Adding teaching methods/materials entries to Notion database...")
    print(f"   Database ID: {DATABASE_ID}")
    print(f"   Total entries to add: {len(TEACHING_ENTRIES)}")
    print("-" * 60)
    
    success_count = 0
    
    for i, entry in enumerate(TEACHING_ENTRIES, 1):
        print(f"[{i}/{len(TEACHING_ENTRIES)}] Adding: {entry['Name']}")
        
        if create_notion_page(entry):
            success_count += 1
        
        print()  # Add spacing between entries
    
    print("-" * 60)
    print(f"Completed! Successfully added {success_count}/{len(TEACHING_ENTRIES)} entries.")
    
    if success_count < len(TEACHING_ENTRIES):
        print("⚠️  Some entries failed to add. Check the error messages above.")
    else:
        print("🎉 All teaching methods/materials entries added successfully!")


if __name__ == "__main__":
    main()
