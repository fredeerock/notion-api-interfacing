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
            "description": "Artwork Commission, Mary Bird Perkins Cancer Center",
            "role": "Artist"
        },
        
        # 2017 entries
        {
            "title": "Diamonds in Dystopia - SXSW",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2017-03-01",
            "location": "Austin TX",
            "description": "South by Southwest (SXSW) performance and presentation on an interactive poetry piece called Diamonds in Dystopia. This was followed by a panel discussion on the intersection of technology and poetry.",
            "role": "Artist"
        },
        {
            "title": "Diamonds in Dystopia - Firehouse Gallery",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2017-01-01",
            "location": "Baton Rouge LA",
            "description": "Exhibition at Firehouse Gallery",
            "role": "Artist"
        },
        {
            "title": "Spotlight",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2017-01-01",
            "location": "Baton Rouge LA",
            "description": "BREW: Baton Rouge Entrepreneurship Week, Shaw Center for the Arts",
            "role": "Artist"
        },
        
        # 2016 entries
        {
            "title": "Causeway - Louisiana Contemporary",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-08-01",
            "location": "Baton Rouge LA",
            "description": "Louisiana Contemporary, Ogden Museum of Southern Art",
            "role": "Artist"
        },
        {
            "title": "Causeway - Griffith University",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-07-01",
            "location": "Brisbane Australia",
            "description": "Exhibition at Griffith University",
            "role": "Artist"
        },
        {
            "title": "Reflection - LSU Annual Dance Concert",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-04-01",
            "location": "Baton Rouge LA",
            "description": "LSU Annual Dance Concert, Shaver Theater",
            "role": "Artist"
        },
        {
            "title": "Causeway - New Orleans Poetry Festival",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-04-01",
            "location": "New Orleans LA",
            "description": "New Orleans Poetry Festival presentation",
            "role": "Artist"
        },
        {
            "title": "Diamonds in Dystopia - TEDxLSU",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2016-03-01",
            "location": "Baton Rouge LA",
            "description": "TEDxLSU, LSU Student Union",
            "role": "Presenter"
        },
        
        # 2015 entries
        {
            "title": "Causeway - Digital Divide",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2015-12-01",
            "location": "Baton Rouge LA",
            "description": "Digital Divide, LSU Digital Media Center",
            "role": "Artist"
        },
        {
            "title": "Space Cadet - Uncommon Thread",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2015-11-01",
            "location": "Baton Rouge LA",
            "description": "Uncommon Thread, Goodwood Library, http://drive.google.com/open?id=1pK1TynQmDtxCZKgNI0ySV86ddqwpkNEHuTndpsYIHaI",
            "role": "Artist"
        },
        {
            "title": "Causeway - Katrina & Rita",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2015-08-01",
            "location": "Baton Rouge LA",
            "description": "Katrina & Rita: A Decade of Research & Response, LSU Digital Media Center",
            "role": "Artist"
        },
        
        # 2014 entries
        {
            "title": "Humming Mississippi - Resonance ISEA",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2014-11-01",
            "location": "Abu Dhabi UAE",
            "description": "Resonance, ISEA: International Symposium for Electronic Art, New York University Art Center Project Space",
            "role": "Artist"
        },
        {
            "title": "Projection Vine Spine and Mirror Genome - Prospect.3",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2014-10-01",
            "location": "Baton Rouge LA",
            "description": "Prospect.3+Baton Rouge: Notes Upriver",
            "role": "Artist"
        },
        {
            "title": "Pierrot Lunaire Op. 21 Interactive Audio Video Performance",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2014-04-01",
            "location": "Baton Rouge LA",
            "description": "LSU School of Music Recital Hall",
            "role": "Artist"
        },
        {
            "title": "Humming Mississippi - NIME London",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2014-06-01",
            "location": "London UK",
            "description": "NIME: New Interfaces for Musical Expression, Goldsmiths University",
            "role": "Artist"
        },
        
        # 2013 entries
        {
            "title": "Orbs Humming Mississippi IMG_1984 Conglomeration - Right Here Now",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-11-01",
            "location": "Baton Rouge LA",
            "description": "Right Here Now, LSU Museum of Art",
            "role": "Artist"
        },
        {
            "title": "Uncertain Languages: Subz_2001 & IMG_1984 Solo Show",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-09-01",
            "location": "Santander Spain",
            "description": "Solo Show, Demolden Video Projects",
            "role": "Artist"
        },
        {
            "title": "Conglomeration - Currents Santa Fe",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-06-01",
            "location": "Santa Fe NM",
            "description": "Currents: Santa Fe International New Media Festival",
            "role": "Artist"
        },
        {
            "title": "Conglomeration - Different Games NYU",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-04-01",
            "location": "New York NY",
            "description": "Different Games, NYU",
            "role": "Artist"
        },
        {
            "title": "IMG 1984 - Art & Copyright Interartive",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-03-01",
            "location": "International",
            "description": "Art & Copyright, Interartive, Online Exhibition",
            "role": "Artist"
        },
        {
            "title": "Change Industries - Hot Mess: Peepshow",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2013-02-01",
            "location": "Buffalo NY",
            "description": "Hot Mess: Peepshow, Buffalo Media Resources",
            "role": "Artist"
        },
        
        # 2012 entries
        {
            "title": "Social Media Center - social(dis)order",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2012-11-01",
            "location": "Baton Rouge LA",
            "description": "social(dis)order, Glassell Gallery",
            "role": "Artist"
        },
        {
            "title": "mememe - GLI.TC/H 2112",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2012-09-01",
            "location": "Chicago IL",
            "description": "GLI.TC/H 2112, OP3N R3P0",
            "role": "Artist"
        },
        {
            "title": "MPG - Symposium on Laptop Ensembles & Orchestras",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2012-04-01",
            "location": "Baton Rouge LA",
            "description": "Symposium on Laptop Ensembles & Orchestras (SLEO)",
            "role": "Performer"
        },
        {
            "title": "Water Cube - Cavortress",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2012-03-01",
            "location": "New Orleans LA",
            "description": "Cavortress, LeMieux Gallery",
            "role": "Artist"
        },
        
        # 2011 entries
        {
            "title": "Tear Catchers - Beyond the Brickyard",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2011-08-01",
            "location": "Helena MT",
            "description": "Beyond the Brickyard, Archie Bray Foundation",
            "role": "Artist"
        },
        {
            "title": "Language Visualizations",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2011-01-01",
            "location": "Baton Rouge LA",
            "description": "Center for Computation & Technology",
            "role": "Artist"
        },
        
        # 2010 entries
        {
            "title": "What is Digital Art - Gallery 229",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-11-01",
            "location": "Baton Rouge LA",
            "description": "Gallery 229 exhibition",
            "role": "Artist"
        },
        {
            "title": "Phone Talks - Maker Faire",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-09-01",
            "location": "Pawtucket RI",
            "description": "Maker Faire presentation",
            "role": "Artist"
        },
        {
            "title": "Orbs - Beautiful and Barbaric at All Times",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-06-01",
            "location": "New York NY",
            "description": "Beautiful and Barbaric at All Times, Art Jail Gallery",
            "role": "Artist"
        },
        {
            "title": "IAM: Indians Astronauts & Magic - Accumulations",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-05-01",
            "location": "Providence RI",
            "description": "Accumulations of Opaque Experiments, Rhode Island Convention Center",
            "role": "Artist"
        },
        {
            "title": "Tipi Experiment - Stetson Alumni Exhibition",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-04-01",
            "location": "DeLand FL",
            "description": "Stetson University Selected Alumni Exhibition, Duncan Gallery",
            "role": "Artist"
        },
        {
            "title": "Static - Digital + Media Biennial",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2010-03-01",
            "location": "Providence RI",
            "description": "Digital + Media Biennial, Sol Koffler Gallery",
            "role": "Artist"
        },
        
        # 2009 entries
        {
            "title": "Park Cube City Public Installation",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2009-08-01",
            "location": "East Greenwich RI",
            "description": "Public Installation, Goddard Park",
            "role": "Artist"
        },
        {
            "title": "Change Industries 2.0",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2009-06-01",
            "location": "Providence RI",
            "description": "Downtown Providence installation",
            "role": "Artist"
        },
        {
            "title": "Movie Subz - Brown University",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2009-04-01",
            "location": "Providence RI",
            "description": "Brown University presentation",
            "role": "Artist"
        },
        
        # 2008 entries
        {
            "title": "MPG - Digital Art in the Post-Digital Age",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2008-11-01",
            "location": "Lakeland FL",
            "description": "Digital Art in the Post-Digital Age, Polk Museum of Art",
            "role": "Artist"
        },
        {
            "title": "Change Industries 1.0",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2008-09-01",
            "location": "Providence RI",
            "description": "Downtown Providence installation",
            "role": "Artist"
        },
        {
            "title": "Echo Cell - Stetson Thesis Show",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2008-05-01",
            "location": "DeLand FL",
            "description": "Stetson University Thesis Show, Duncan Gallery of Art",
            "role": "Artist"
        },
        {
            "title": "MPG - Fountain Art Fair",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2008-12-01",
            "location": "Miami FL",
            "description": "Fountain Art Fair (Art Basel)",
            "role": "Artist"
        },
        
        # 2007 entries
        {
            "title": "Crunch - Stetson Promotional CD",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2007-11-01",
            "location": "DeLand FL",
            "description": "Stetson University Promotional CD",
            "role": "Artist"
        },
        {
            "title": "MPG - Fusing Touchstone Festival",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2007-10-01",
            "location": "DeLand FL",
            "description": "Fusing Touchstone Art and Media Festival, Stetson University",
            "role": "Performer"
        },
        {
            "title": "California License - Mirror Pal Concert",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2007-08-01",
            "location": "Orlando FL",
            "description": "Mirror Pal Concert, Backbooth",
            "role": "Performer"
        },
        {
            "title": "MPG - New West Electronic Arts Festival",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2007-05-01",
            "location": "San Diego CA",
            "description": "New West Electronic Arts & Music Festival, San Diego State University",
            "role": "Performer"
        },
        
        # 2006 entries
        {
            "title": "Vengen - Digital Arts Night",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2006-04-01",
            "location": "DeLand FL",
            "description": "Digital Arts Night, Stetson University",
            "role": "Artist"
        },
        
        # 2005 entries
        {
            "title": "Bottle Wall - SHIPWRECK!",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2005-08-01",
            "location": "New Orleans LA",
            "description": "SHIPWRECK!, Odyssey Marine Museum",
            "role": "Artist"
        },
        
        # 2004 entries
        {
            "title": "Shadow Hands - Art Night",
            "category": "1.3.3.1 Original Creative Works & Presentations",
            "date": "2004-04-01",
            "location": "Tampa FL",
            "description": "Art Night, University of Tampa",
            "role": "Artist"
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} original creative works & presentations...")
    print("=" * 90)
    
    successful = 0
    failed = 0
    
    for i, entry in enumerate(entries, 1):
        print(f"\n[{i}/{len(entries)}] Processing: {entry['title']}")
        
        if add_entry_to_notion(entry):
            successful += 1
        else:
            failed += 1
    
    print("\n" + "=" * 90)
    print(f"📊 Batch addition complete!")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📋 Total: {len(entries)}")

if __name__ == "__main__":
    # Change to the script directory to ensure add_notion_entry.py can be found
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    main()
