#!/usr/bin/env python3
"""
Batch Entry Script for Awards and Lectureships

This script adds entries to the "1.3.6 Other awards, lectureships, or prizes that show recognition of scholarly or artistic achievement" category in the Notion database.
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
    """Main function to add all awards and lectureships entries."""
    
    entries = [
        {
            "title": "Stetson Digital Media Festival Honorarium",
            "category": "1.3.6 Other awards lectureships or prizes that show recognition of scholarly or artistic achievement",
            "date": "2015-01-01",
            "location": "DeLand FL",
            "description": "Stetson Digital Media Festival Honorarium ($200) from Stetson University in DeLand, FL.",
        },
        {
            "title": "Junior Faculty Travel Grant",
            "category": "1.3.6 Other awards lectureships or prizes that show recognition of scholarly or artistic achievement",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "Junior Faculty Travel Grant ($700) from Louisiana State University Office of Research & Economic Development in Baton Rouge, LA.",
        },
        {
            "title": "Travel Honorarium from New York University Abu Dhabi",
            "category": "1.3.6 Other awards lectureships or prizes that show recognition of scholarly or artistic achievement",
            "date": "2014-01-01",
            "location": "Abu Dhabi UAE",
            "description": "Travel Honorarium (~$3,000) from New York University Abu Dhabi in Abu Dhabi, UAE for show during International Symposium on Electronic Art.",
        },
        {
            "title": "Artist Honorarium from Buffalo Media Resources",
            "category": "1.3.6 Other awards lectureships or prizes that show recognition of scholarly or artistic achievement",
            "date": "2013-01-01",
            "location": "Buffalo NY",
            "description": "Artist Honorarium from Buffalo Media Resources in Buffalo, NY for Peephow: Hotmess.",
        },
        {
            "title": "Junior Faculty Travel Grant",
            "category": "1.3.6 Other awards lectureships or prizes that show recognition of scholarly or artistic achievement",
            "date": "2012-01-01",
            "location": "Baton Rouge LA",
            "description": "Junior Faculty Travel Grant ($500) from Louisiana State University Office of Research & Economic Development in Baton Rouge, LA.",
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} awards and lectureships entries...")
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
