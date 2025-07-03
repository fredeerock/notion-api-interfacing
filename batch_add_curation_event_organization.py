#!/usr/bin/env python3
"""
Batch Entry Script for Curation and Event Organization

This script adds all curation and event organization entries to the 
"1.3.3.2 Curation and Event Organization" category in the Notion database.
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
    """Main function to add all curation and event organization entries."""
    
    entries = [
        # 2017 entries
        {
            "title": "Immersive Expressions",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2017-01-01",
            "location": "Online",
            "description": "ACM SIGGRAPH Digital Arts Community Online Exhibition. Curator.",
            "role": "Curator"
        },
        
        # 2016 entries
        {
            "title": "Art of the App",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2016-01-01",
            "location": "Baton Rouge LA",
            "description": "LSU Student Union Gallery. Co-curator.",
            "role": "Co-Curator"
        },
        {
            "title": "Kids Lab: Light and Shadow Play",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2016-01-01",
            "location": "Baton Rouge LA",
            "description": "Collaboration with Knock Knock Children's Museum for Red Stick International Festival, Goodwood Library. Co-Organizer.",
            "role": "Co-Organizer"
        },
        
        # 2015 entries
        {
            "title": "New Interfaces for Musical Expression 2015 Installations",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Shaw Center for the Arts. Curator.",
            "role": "Curator"
        },
        
        # 2014 entries
        {
            "title": "Prospect 3+ Satellite Festival",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "Co-Organizer.",
            "role": "Co-Organizer"
        },
        {
            "title": "Black Arts Film Festival",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "LSU Digital Media Center. Co-Organizer.",
            "role": "Co-Organizer"
        },
        {
            "title": "Redstick FutureFest",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "LSU Digital Media Center. Co-Organizer.",
            "role": "Co-Organizer"
        },
        {
            "title": "Digital by Design Art + Technology Exhibition",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "LSU Digital Media Center. Co-Organizer.",
            "role": "Co-Organizer"
        },
        
        # 2013 entries
        {
            "title": "Augmented Reality Digital Signage",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2013-01-01",
            "location": "Baton Rouge LA",
            "description": "LSU Museum of Art. Producer.",
            "role": "Producer"
        },
        {
            "title": "Global Game Jam Baton Rouge",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2013-01-01",
            "location": "Baton Rouge LA",
            "description": "LSU Digital Media Center. Co-Organizer.",
            "role": "Co-Organizer"
        },
        {
            "title": "Rashaad Newsome: Portraiture: Style and Ornament",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2013-01-01",
            "location": "Baton Rouge LA",
            "description": "LSU Museum of Art. Assisted Organization and Preparation.",
            "role": "Assistant Organizer"
        },
        
        # 2012 entries
        {
            "title": "social(dis)order",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2012-01-01",
            "location": "Baton Rouge LA",
            "description": "Exhibition with work by J. DeLappe, N. Bookchin, J. Cohen, Glassell Gallery. Co-Curator.",
            "role": "Co-Curator"
        },
        
        # 2010 entries
        {
            "title": "Digital + Media Biennial",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2010-01-01",
            "location": "Providence RI",
            "description": "Sol Koffler Gallery. Co-Curator.",
            "role": "Co-Curator"
        },
        
        # 2009 entries
        {
            "title": "RISD Digital + Media Graduate Student Journal",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2009-05-01",
            "location": "Providence RI",
            "description": "Frauke Behrendt, and Teri Reub, eds. Rhode Island School of Design. Dept. of Digital Media. Designer.",
            "role": "Designer"
        },
        
        # 2008 entries
        {
            "title": "Stetson University Thesis Show",
            "category": "1.3.3.2 Curation and Event Organization",
            "date": "2008-01-01",
            "location": "DeLand FL",
            "description": "Duncan Gallery of Art. Co-Curator.",
            "role": "Co-Curator"
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} curation and event organization entries...")
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
    main()
