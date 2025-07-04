#!/usr/bin/env python3
"""
Batch Entry Script for Administrative Duties

This script adds entries to the "1.3.5.2 Administrative duties" category in the Notion database.
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
    """Main function to add all administrative duties entries."""
    
    entries = [
        {
            "title": "Manager, Media Research Studio",
            "category": "1.3.5.2 Administrative Duties",
            "date": "2012-01-01",
            "location": "Baton Rouge LA",
            "description": "Manager of Media Research Studio at Louisiana State University in Baton Rouge, LA (2012-2015).",
            "role": "Manager"
        },
        {
            "title": "Art Chair, NIME: New Interfaces for Musical Expression",
            "category": "1.3.5.2 Administrative Duties",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "Art Chair for NIME: New Interfaces for Musical Expression at Louisiana State University in Baton Rouge, LA (2014-2015).",
            "role": "Art Chair"
        },
        {
            "title": "Co-manager, Art & Technology Lab",
            "category": "1.3.5.2 Administrative Duties",
            "date": "2013-01-01",
            "location": "Baton Rouge LA",
            "description": "Co-manager of Art & Technology Lab at Louisiana State University in Baton Rouge, LA (2013-2015).",
            "role": "Co-manager"
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} administrative duties entries...")
    print("=" * 80)
    
    successful = 0
    failed = 0
    
    for i, entry in enumerate(entries, 1):
        print(f"\n[{i}/{len(entries)}] Processing: {entry['title']}")
        
        if add_entry_to_notion(entry):
            successful += 1
        else:
            failed += 1
    
    print("\n" + "=" * 80)
    print(f"📊 Batch addition completed!")
    print(f"✅ Successfully added: {successful} entries")
    print(f"❌ Failed to add: {failed} entries")
    
    if failed > 0:
        print("\n⚠️  Some entries failed to add. Check the error messages above.")
        sys.exit(1)
    else:
        print("\n🎉 All entries were successfully added to the Notion database!")

if __name__ == "__main__":
    # Change to the script directory to ensure add_notion_entry.py can be found
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    main()
