#!/usr/bin/env python3
"""
Batch Entry Script for Other Scholarly or Creative Activities

This script adds entries to the "1.3.5 Other scholarly or creative activities or other contributions to the profession" category in the Notion database.
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
    """Main function to add all other scholarly activities entries."""
    
    entries = [
        # 1.3.5.1 Membership in professional organizations
        {
            "title": "Association for Computing Machinery",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2011-01-01",  # Approximate start date
            "location": "",
            "description": "Member of the Association for Computing Machinery (ACM).",
            "role": "Member"
        },
        {
            "title": "New Media Caucus",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2012-01-01",
            "location": "",
            "description": "Member of New Media Caucus from 2012 to Present.",
            "role": "Member"
        },
        {
            "title": "SIGGRAPH Digital Arts Community",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2011-01-01",
            "location": "",
            "description": "Committee Member of the SIGGRAPH Digital Arts Community.",
            "role": "Committee Member"
        },
        {
            "title": "Special Interest Group on Computer Graphics and Interactive Techniques",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2011-01-01",
            "location": "",
            "description": "Member of the Special Interest Group on Computer Graphics and Interactive Techniques.",
            "role": "Member"
        },
        {
            "title": "Rhizome",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2011-01-01",
            "location": "",
            "description": "Member of Rhizome, digital art and culture organization.",
            "role": "Member"
        },
        
        # 1.3.5.2 Administrative duties
        {
            "title": "Manager Media Research Studio",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2012-01-01",
            "location": "Baton Rouge LA",
            "description": "Manager of the Media Research Studio at Louisiana State University in Baton Rouge, LA from 2012-15.",
            "role": "Manager"
        },
        {
            "title": "Art Chair NIME: New Interfaces for Musical Expression",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "Art Chair for NIME: New Interfaces for Musical Expression at Louisiana State University in Baton Rouge, LA from 2014-15.",
            "role": "Art Chair"
        },
        {
            "title": "Co-manager Art & Technology Lab",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2013-01-01",
            "location": "Baton Rouge LA",
            "description": "Co-manager of the Art & Technology Lab at Louisiana State University in Baton Rouge, LA from 2013-15.",
            "role": "Co-manager"
        },
        
        # 1.3.5.3 New standard testing methods, new design of equipment, etc.
        {
            "title": "Titan Computer System Setup",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2016-01-01",
            "location": "Baton Rouge LA",
            "description": "Set up a new computer system called 'Titan' for experimentation on applications in machine learning in visual and sonic arts at Louisiana State University in Baton Rouge, LA. Made possible by a grant from the Louisiana Board of Regents.",
            "role": "System Administrator"
        },
        {
            "title": "K2 Computer System Setup",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2016-01-01",
            "location": "Baton Rouge LA",
            "description": "Set up a new computer system called 'K2' for experimentation on grid computing applications in the arts at Louisiana State University in Baton Rouge, LA.",
            "role": "System Administrator"
        },
        {
            "title": "OpenStack Cloud Render Farm",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Constructed a cloud based render farm using the OpenStack cloud platform for use with 3D graphics software such as Maya, Houdini, and Nuke at Louisiana State University in Baton Rouge, LA.",
            "role": "System Administrator"
        },
        {
            "title": "HIVE: High-performance Interactive Visualization and Electroacoustics Initiative",
            "category": "1.3.5 Other scholarly or creative activities or other contributions to the profession",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Started a new initiative called HIVE: High-performance Interactive Visualization and Electroacoustics at Louisiana State University in Baton Rouge, LA. HIVE houses several new platforms for research existing between art and high-performance computing.",
            "role": "Founder"
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} other scholarly activities entries...")
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
