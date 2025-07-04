#!/usr/bin/env python3
"""
Batch Entry Script for New Standard Testing Methods and Equipment

This script adds entries to the "1.3.5.3 New standard testing methods, new design of equipment, etc." category in the Notion database.
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
    """Main function to add all new standard testing methods and equipment entries."""
    
    entries = [
        {
            "title": "Titan Computer System Setup",
            "category": "1.3.5.3 Standards and Equipment",
            "date": "2016-01-01",
            "location": "Baton Rouge LA",
            "description": "Set up a new computer system called \"Titan\" for experimentation on applications in machine learning in visual and sonic arts at Louisiana State University in Baton Rouge, LA. Made possible by a grant from the Louisiana Board of Regents.",
        },
        {
            "title": "K2 Computer System Setup",
            "category": "1.3.5.3 Standards and Equipment",
            "date": "2016-01-01",
            "location": "Baton Rouge LA",
            "description": "Set up a new computer system called \"K2\" for experimentation on grid computing applications in the arts at Louisiana State University in Baton Rouge, LA.",
        },
        {
            "title": "OpenStack Cloud-Based Render Farm",
            "category": "1.3.5.3 Standards and Equipment",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Constructed a cloud based render farm using the OpenStack cloud platform for use with 3D graphics software such as Maya, Houdini, and Nuke at Louisiana State University in Baton Rouge, LA.",
        },
        {
            "title": "HIVE: High-performance Interactive Visualization and Electroacoustics",
            "category": "1.3.5.3 Standards and Equipment",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Started a new initiative called HIVE: High-performance Interactive Visualization and Electroacoustics at Louisiana State University in Baton Rouge, LA. HIVE houses several new platforms for research existing between art and high-performance computing.",
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} new standard testing methods and equipment entries...")
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
