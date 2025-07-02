#!/usr/bin/env python3
"""
Notion Database Schema Inspector

This script helps you inspect your Notion database schema to see
what properties are available.

Usage: python inspect_database.py
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


def inspect_database():
    """Retrieve and display the database schema."""
    response = requests.get(
        f"{NOTION_API_URL}/databases/{DATABASE_ID}",
        headers=HEADERS
    )
    
    if response.status_code == 200:
        database = response.json()
        
        print(f"📊 Database Information")
        print(f"   Title: {database.get('title', [{}])[0].get('plain_text', 'Unknown')}")
        print(f"   ID: {database['id']}")
        print()
        
        print("🏷️  Available Properties:")
        properties = database.get("properties", {})
        
        for prop_name, prop_data in properties.items():
            prop_type = prop_data.get("type", "unknown")
            print(f"   • {prop_name} ({prop_type})")
            
            # Show additional details for some property types
            if prop_type == "select":
                options = prop_data.get("select", {}).get("options", [])
                if options:
                    print(f"     Options: {', '.join([opt['name'] for opt in options])}")
            elif prop_type == "multi_select":
                options = prop_data.get("multi_select", {}).get("options", [])
                if options:
                    print(f"     Options: {', '.join([opt['name'] for opt in options])}")
        
        print()
        print("💡 Use these property names in your ENTRY_DATA dictionary.")
        
    else:
        print(f"❌ Error retrieving database:")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")


if __name__ == "__main__":
    inspect_database()
