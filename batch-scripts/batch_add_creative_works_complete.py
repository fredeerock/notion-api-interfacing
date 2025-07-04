#!/usr/bin/env python3
"""
Batch Entry Script for Original Creative Works & Presentations

This script adds all original creative works and presentations to the Notion database
under category "1.3.3.1 Original Creative Works & Presentations"
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
    
    # Original Creative Works & Presentations entries
    entries = [
        # 2019 entries
        {
            "title": "Journey to Wellness",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2019-01-01",
            "location": "Baton Rouge LA",
            "description": "Artwork Commission Mary Bird Perkins Cancer Center"
        },
        {
            "title": "Diamonds in Dystopia",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2019-01-01",
            "location": "Baton Rouge LA",
            "description": "Baton Rouge Gallery"
        },
        
        # 2018 entries
        {
            "title": "XR Landscapes",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2018-01-01",
            "location": "Baton Rouge LA",
            "description": "Temporal Aesthetics Baton Rouge Arts Council Firehouse Gallery"
        },
        
        # 2017 entries
        {
            "title": "Diamonds in Dystopia - SXSW",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2017-03-01",
            "location": "Austin TX",
            "description": "South by Southwest (SXSW)"
        },
        {
            "title": "Spotlight",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2017-01-01",
            "location": "Baton Rouge LA",
            "description": "BREW: Baton Rouge Entrepreneurship Week Shaw Center for the Arts"
        },
        
        # 2016 entries
        {
            "title": "Causeway - Louisiana Contemporary",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-08-01",
            "location": "New Orleans LA",
            "description": "Louisiana Contemporary Ogden Museum of Southern Art"
        },
        {
            "title": "Causeway - Griffith University",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-07-01",
            "location": "Brisbane Australia",
            "description": "Griffith University"
        },
        {
            "title": "Reflection - LSU Dance Concert",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-04-01",
            "location": "Baton Rouge LA",
            "description": "LSU Annual Dance Concert Shaver Theater"
        },
        {
            "title": "Causeway - Poetry Festival",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-03-01",
            "location": "New Orleans LA",
            "description": "New Orleans Poetry Festival"
        },
        {
            "title": "Diamonds in Dystopia - TEDxLSU",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-02-01",
            "location": "Baton Rouge LA",
            "description": "TEDxLSU LSU Student Union"
        },
        
        # 2015 entries
        {
            "title": "Causeway - Digital Divide",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2015-12-01",
            "location": "Baton Rouge LA",
            "description": "Digital Divide LSU Digital Media Center"
        },
        {
            "title": "Space Cadet",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2015-11-01",
            "location": "Baton Rouge LA",
            "description": "Uncommon Thread Goodwood Library http://drive.google.com/open?id=1pK1TynQmDtxCZKgNI0ySV86ddqwpkNEHuTndpsYIHaI"
        },
        {
            "title": "Causeway - Katrina & Rita",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2015-08-01",
            "location": "Baton Rouge LA",
            "description": "Katrina & Rita: A Decade of Research & Response LSU Digital Media Center"
        },
        
        # 2014 entries
        {
            "title": "Humming Mississippi - Resonance",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2014-11-01",
            "location": "Abu Dhabi UAE",
            "description": "Resonance ISEA: International Symposium for Electronic Art New York University Art Center Project Space"
        },
        {
            "title": "Projection Vine Spine and Mirror Genome",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2014-10-01",
            "location": "Baton Rouge LA",
            "description": "Prospect.3+Baton Rouge: Notes Upriver"
        },
        {
            "title": "Pierrot Lunaire Op. 21",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2014-04-01",
            "location": "Baton Rouge LA",
            "description": "Interactive Audio Video Performance LSU School of Music Recital Hall"
        },
        {
            "title": "Humming Mississippi - NIME",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2014-06-01",
            "location": "London England",
            "description": "NIME: New Interfaces for Musical Expression Goldsmiths University"
        },
        
        # 2013 entries
        {
            "title": "Orbs Humming Mississippi IMG_1984 Conglomeration",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-11-01",
            "location": "Baton Rouge LA",
            "description": "Right Here Now LSU Museum of Art"
        },
        {
            "title": "Uncertain Languages: Subz_2001 & IMG_1984",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-10-01",
            "location": "Santander Spain",
            "description": "Solo Show Demolden Video Projects"
        },
        {
            "title": "Conglomeration - Currents",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-06-01",
            "location": "Santa Fe NM",
            "description": "Currents: Santa Fe International New Media Festival"
        },
        {
            "title": "Conglomeration - Different Games",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-04-01",
            "location": "New York NY",
            "description": "Different Games NYU"
        },
        {
            "title": "IMG 1984 - Art & Copyright",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-03-01",
            "location": "International",
            "description": "Art & Copyright Interartive Online Exhibition"
        },
        {
            "title": "Change Industries - Hot Mess",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-02-01",
            "location": "Buffalo NY",
            "description": "Hot Mess: Peepshow Buffalo Media Resources"
        },
        
        # 2012 entries
        {
            "title": "Social Media Center",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2012-12-01",
            "location": "Baton Rouge LA",
            "description": "social(dis)order Glassell Gallery"
        },
        {
            "title": "mememe - GLI.TC/H",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2012-11-01",
            "location": "Chicago IL",
            "description": "GLI.TC/H 2112 OP3N R3P0"
        },
        {
            "title": "MPG - SLEO",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2012-04-01",
            "location": "Baton Rouge LA",
            "description": "Symposium on Laptop Ensembles & Orchestras (SLEO)"
        },
        {
            "title": "Water Cube",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2012-03-01",
            "location": "New Orleans LA",
            "description": "Cavortress LeMieux Gallery"
        },
        
        # 2011 entries
        {
            "title": "Tear Catchers",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2011-08-01",
            "location": "Helena MT",
            "description": "Beyond the Brickyard Archie Bray Foundation"
        },
        {
            "title": "Language Visualizations",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2011-01-01",
            "location": "Baton Rouge LA",
            "description": "Center for Computation & Technology"
        },
        
        # 2010 entries
        {
            "title": "What is Digital Art",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-12-01",
            "location": "Baton Rouge LA",
            "description": "Gallery 229"
        },
        {
            "title": "Phone Talks - Maker Faire",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-09-01",
            "location": "Pawtucket RI",
            "description": "Maker Faire"
        },
        {
            "title": "Orbs - Beautiful and Barbaric",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-06-01",
            "location": "New York NY",
            "description": "Beautiful and Barbaric at All Times Art Jail Gallery"
        },
        {
            "title": "IAM: Indians Astronauts & Magic",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-05-01",
            "location": "Providence RI",
            "description": "Accumulations of Opaque Experiments Rhode Island Convention Center"
        },
        {
            "title": "Tipi Experiment",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-04-01",
            "location": "DeLand FL",
            "description": "Stetson University Selected Alumni Exhibition Duncan Gallery"
        },
        {
            "title": "Static",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-03-01",
            "location": "Providence RI",
            "description": "Digital + Media Biennial Sol Koffler Gallery"
        },
        
        # 2009 entries
        {
            "title": "Park Cube City",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2009-08-01",
            "location": "East Greenwich RI",
            "description": "Public Installation Goddard Park"
        },
        {
            "title": "Change Industries 2.0",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2009-06-01",
            "location": "Providence RI",
            "description": "Downtown Providence"
        },
        {
            "title": "Movie Subz - Brown University",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2009-04-01",
            "location": "Providence RI",
            "description": "Brown University"
        },
        
        # 2008 entries
        {
            "title": "MPG - Digital Art Post-Digital",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2008-12-01",
            "location": "Lakeland FL",
            "description": "Digital Art in the Post-Digital Age Polk Museum of Art"
        },
        {
            "title": "Change Industries 1.0",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2008-10-01",
            "location": "Providence RI",
            "description": "Downtown Providence"
        },
        {
            "title": "Echo Cell",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2008-05-01",
            "location": "DeLand FL",
            "description": "Stetson University Thesis Show Duncan Gallery of Art"
        },
        {
            "title": "MPG - Art Basel",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2008-12-01",
            "location": "Miami FL",
            "description": "Fountain Art Fair (Art Basel)"
        },
        
        # 2007 entries
        {
            "title": "Crunch",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2007-12-01",
            "location": "DeLand FL",
            "description": "Stetson University Promotional CD"
        },
        {
            "title": "MPG - Fusing Touchstone",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2007-04-01",
            "location": "DeLand FL",
            "description": "Fusing Touchstone Art and Media Festival Stetson University"
        },
        {
            "title": "California License",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2007-03-01",
            "location": "Orlando FL",
            "description": "Mirror Pal Concert Backbooth"
        },
        {
            "title": "MPG - New West Electronic Arts",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2007-02-01",
            "location": "San Diego CA",
            "description": "New West Electronic Arts & Music Festival San Diego State University"
        },
        
        # 2006 entries
        {
            "title": "Vengen",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2006-11-01",
            "location": "DeLand FL",
            "description": "Digital Arts Night Stetson University"
        },
        
        # 2005 entries
        {
            "title": "Bottle Wall",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2005-08-01",
            "location": "New Orleans LA",
            "description": "SHIPWRECK! Odyssey Marine Museum"
        },
        
        # 2004 entries
        {
            "title": "Shadow Hands",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2004-04-01",
            "location": "Tampa FL",
            "description": "Art Night University of Tampa"
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} original creative works and presentations...")
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
    print(f"📊 Batch addition complete!")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📋 Total: {len(entries)}")

if __name__ == "__main__":
    # Change to the script directory to ensure add_notion_entry.py can be found
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    main()
