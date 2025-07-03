#!/usr/bin/env python3
"""
Batch Entry Script for Professional Academic Events

This script adds all professional academic events entries to the 
"1.3.4 Participation in Professional Academic Events" category in the Notion database.
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
    """Main function to add all professional academic events entries."""
    
    entries = [
        # 2024 entries
        {
            "title": "Digital Twin Fundamentals in Manufacturing: Building an Industrial Twin of Twins for NASA",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2024-01-01",
            "location": "Online",
            "description": "Digital Twin Consortium Q1 Member Meeting, Presentation by Greg Porter on behalf of Louisiana State University collaboration.",
            "role": "Presenter"
        },
        
        # 2023 entries
        {
            "title": "Digital Twin Consortium Panel - NASA Digital Twin Project",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2023-12-14",
            "location": "Online",
            "description": "Invited speaker, Derick Ostrenko, Marc Aubanel, Jason Jamerson.",
            "role": "Invited Speaker"
        },
        
        # 2017 entries
        {
            "title": "Immersive Expressions: Virtual Reality on the Web",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2017-01-01",
            "location": "Los Angeles CA",
            "description": "ACM SIGGRAPH Panel Session of the ACM SIGGRAPH Digital Arts Community. Panel Chair.",
            "role": "Panel Chair"
        },
        {
            "title": "Diamonds in Dystopia: A Poetry Performance Web App",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2017-03-01",
            "location": "Austin TX",
            "description": "South by Southwest (SXSW). Panel Member.",
            "role": "Panel Member"
        },
        {
            "title": "Creative Workflows for 3D Scanning Applications: Augmented Reality Sandbox, Digital Contour Models, and Repurposing Art Objects into Virtual Terrains",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2017-02-01",
            "location": "Online",
            "description": "Educause ELI preconference seminar co-presented with Peter Summerlin, Sarah Ferguson, and Vincent Cellucci.",
            "role": "Co-Presenter"
        },
        
        # 2015 entries
        {
            "title": "The 15th International Conference on New Interfaces for Musical Expression",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2015-05-31",
            "location": "Baton Rouge LA",
            "description": "Louisiana State University. Art Co-Chair.",
            "role": "Art Co-Chair"
        },
        {
            "title": "Baton Rouge Mini Maker Faire",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Demo.",
            "role": "Presenter"
        },
        {
            "title": "HIVE: High-performance Interactive Visualization & Electroacoustics",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Coastal Sustainability Studio Open House. Presenter.",
            "role": "Presenter"
        },
        {
            "title": "Humming Mississippi",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2015-01-01",
            "location": "Paris France",
            "description": "WAC: 1st Web Audio Conference, Demo, Mozilla & IRCAM (Centre Pompidou).",
            "role": "Presenter"
        },
        {
            "title": "Poe's Magazines",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2015-01-01",
            "location": "New York NY",
            "description": "The Poe Studies Association's Fourth International Edgar Allan Poe Conference, Presentation by Gerald Kennedy, Website Demonstrated.",
            "role": "Demonstrator"
        },
        {
            "title": "Poe's Magazines",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2015-01-01",
            "location": "Vancouver Canada",
            "description": "Modern Language Association Convention, Tech Demo.",
            "role": "Demonstrator"
        },
        {
            "title": "HIVE: High-performance Interactive Visualization & Electroacoustics",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2015-01-01",
            "location": "Vancouver Canada",
            "description": "Artist talk presented at The International Symposium on Electronic Art (ISEA 2015), Simon Fraser University.",
            "role": "Presenter"
        },
        
        # 2014 entries
        {
            "title": "Interactive Mobile Art",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "iOS Bootcamp. Presenter.",
            "role": "Presenter"
        },
        {
            "title": "New Orleans Mini Maker Faire",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2014-01-01",
            "location": "New Orleans LA",
            "description": "Demo.",
            "role": "Presenter"
        },
        {
            "title": "Resonance",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2014-01-01",
            "location": "Abu Dhabi UAE",
            "description": "International Symposium on Electronic Art (ISEA 2014), New York University. Panelist.",
            "role": "Panelist"
        },
        {
            "title": "Coastal Sustainability Studio Open House",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "Presenter.",
            "role": "Presenter"
        },
        
        # 2013 entries
        {
            "title": "Conglomeration",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2013-01-01",
            "location": "New York NY",
            "description": "Artist Presentation, Different Games Conference, NYU.",
            "role": "Presenter"
        },
        {
            "title": "6 in 6",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2013-01-01",
            "location": "New York NY",
            "description": "Artist Talk, New Media Caucus Showcase at the National Academy.",
            "role": "Presenter"
        },
        
        # 2012 entries
        {
            "title": "Transmodal Journeys: Digital Adventures in the Physical World",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2012-01-01",
            "location": "Albuquerque NM",
            "description": "Artists Talk, International Symposium on Electronic Art (ISEA).",
            "role": "Presenter"
        },
        {
            "title": "What is New Media Art",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2012-01-01",
            "location": "Baton Rouge LA",
            "description": "Gallery Talk, Louisiana Art and Science Museum.",
            "role": "Presenter"
        },
        
        # 2010 entries
        {
            "title": "Arduino for Art Installations",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2010-01-01",
            "location": "Providence RI",
            "description": "Workshop, Rhode Island School of Design.",
            "role": "Workshop Leader"
        },
        {
            "title": "Max/MSP/Jitter for Interactive Art Installations",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2010-01-01",
            "location": "Providence RI",
            "description": "Workshop, Rhode Island School of Design.",
            "role": "Workshop Leader"
        },
        
        # 2007 entries
        {
            "title": "Oscar Niemeyer and Modernism in Brazil",
            "category": "1.3.4 Participation in Professional Academic Events",
            "date": "2007-01-01",
            "location": "DeLand FL",
            "description": "Lecture, Stetson University.",
            "role": "Lecturer"
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} professional academic events entries...")
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
