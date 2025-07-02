#!/usr/bin/env python3
"""
Batch Entry Template for Notion Database

This is a template for creating new batch scripts to add entries to your Notion database.
Copy this file and modify the entries list below to add your data.

Instructions:
1. Copy this file to a new name (e.g., batch_add_my_data.py)
2. Modify the entries list below with your data
3. Run the script: python batch_add_my_data.py

Each entry should have the following required fields:
- title: The title of the entry.
- category: Category from your Notion database
- date: Date in YYYY-MM-DD format
- description: Don't duplicate content from the title as it's show right next to it. This is a short description of the entry that expands on the title only when necessary. It can also complement the title if needed. Commas and other punctuation are allowed in the description. If there's a URL it should be included in the description.

Optional fields:
- url: URL related to the entry
- location: Location of the item
- role: Your role (PI, Co-PI, Presenter, etc.)

Notes:
- Don't use commas in the location or role fields as they may cause issues with parsing.
"""

import subprocess
import sys
import os

def add_entry_to_notion(entry):
    """Add a single entry to Notion using add_notion_entry.py"""
    cmd = [
        sys.executable, 
        "add_notion_entry.py",
        "--title", entry["title"],
        "--category", entry["category"],
        "--date", entry["date"],
        "--location", entry["location"],
        "--description", entry["description"]
    ]
    
    # Add optional fields
    if "url" in entry and entry["url"]:
        cmd.extend(["--url", entry["url"]])
    if "role" in entry and entry["role"]:
        cmd.extend(["--role", entry["role"]])
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ Successfully added: {entry['title']}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error adding {entry['title']}: {e}")
        print(f"   Command output: {e.stdout}")
        print(f"   Command error: {e.stderr}")
        return False

def main():
    """Main function to add all entries."""
    
    # ============================================
    # MODIFY THIS SECTION WITH YOUR DATA
    # ============================================
    entries = [
        {
            "title": "Example Entry 1",
            "category": "Scholarship",  # Use valid categories from your Notion database
            "date": "2025-01-01",
            "location": "Baton Rouge LA", # Optional
            "description": "This is an example entry description",
            "url": "https://example.com",  # Optional
            "role": "Presenter"  # Optional
        },
        {
            "title": "Example Entry 2",
            "category": "Teaching",
            "date": "2025-01-02",
            "location": "New Orleans LA",
            "description": "Another example entry",
            # url, location, and role are optional and can be omitted
        }
    ]
    # ============================================
    
    print(f"🚀 Starting batch addition of {len(entries)} entries...")
    print("=" * 50)
    
    successful = 0
    failed = 0
    
    for i, entry in enumerate(entries, 1):
        print(f"\n[{i}/{len(entries)}] Processing: {entry['title']}")
        
        if add_entry_to_notion(entry):
            successful += 1
        else:
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Batch addition complete!")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📋 Total: {len(entries)}")

if __name__ == "__main__":
    # Change to the script directory to ensure add_notion_entry.py can be found
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    main()
