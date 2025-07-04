#!/usr/bin/env python3
"""
Batch Entry Script for Professional Memberships

This script adds entries to the "1.3.5.1 Membership in professional organizations" category in the Notion database.
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
    """Main function to add all professional memberships entries."""
    
    entries = [
        {
            "title": "Association for Computing Machinery",
            "category": "1.3.5.1 Professional Organizations",
            "date": "2012-01-01",  # Using 2012 as approximate start date
            "location": "",
            "description": "Member of the Association for Computing Machinery (ACM).",
        },
        {
            "title": "New Media Caucus",
            "category": "1.3.5.1 Professional Organizations",
            "date": "2012-01-01",
            "location": "",
            "description": "Member of the New Media Caucus, 2012 - Present.",
        },
        {
            "title": "SIGGRAPH Digital Arts Community",
            "category": "1.3.5.1 Professional Organizations",
            "date": "2012-01-01",
            "location": "",
            "description": "Committee Member of the SIGGRAPH Digital Arts Community.",
            "role": "Committee Member"
        },
        {
            "title": "Special Interest Group on Computer Graphics and Interactive Techniques",
            "category": "1.3.5.1 Professional Organizations",
            "date": "2012-01-01",
            "location": "",
            "description": "Member of the Special Interest Group on Computer Graphics and Interactive Techniques.",
        },
        {
            "title": "Rhizome",
            "category": "1.3.5.1 Professional Organizations",
            "date": "2012-01-01",
            "location": "",
            "description": "Member of Rhizome digital arts organization.",
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} professional memberships entries...")
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
