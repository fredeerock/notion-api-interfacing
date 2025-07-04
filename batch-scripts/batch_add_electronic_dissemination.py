#!/usr/bin/env python3
"""
Batch Entry Script for Electronic Dissemination of Research

This script adds all electronic dissemination of research entries to the Notion database
under category "1.3.1.7 Electronic dissemination of research"
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
    
    # Electronic dissemination of research entries
    entries = [
        # 2024 entries
        {
            "title": "OSC Sender and Receiver",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2024-01-01",
            "location": "Baton Rouge LA",
            "description": "Custom Software by Derick Ostrenko, https://github.com/fredeerock/Simple-OSC-Sender-and-Receiver",
            "role": "Developer"
        },
        {
            "title": "Simple Unreal Switchboard",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2024-01-01",
            "location": "Baton Rouge LA",
            "description": "Custom Software by Derick Ostrenko, https://github.com/fredeerock/simpleUnrealSwitchboard",
            "role": "Developer"
        },
        {
            "title": "Images to Video",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2024-01-01",
            "location": "Baton Rouge LA",
            "description": "Custom Software by Derick Ostrenko, https://github.com/fredeerock/imagesToVideo",
            "role": "Developer"
        },
        {
            "title": "DMX Visualizer",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2024-01-01",
            "location": "Baton Rouge LA",
            "description": "Custom Software by Derick Ostrenko, https://github.com/fredeerock/simpleDmxVisualizer",
            "role": "Developer"
        },
        
        # 2023 entries
        {
            "title": "NASA TwinLink Digital Twin Platform",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2023-01-01",
            "location": "Baton Rouge LA",
            "description": "Greg Porter, Marc Aubanel, Gary Innerarity, Derick Ostrenko, Sidney Church, Jason Jamerson, Nick Lavergne, Chris Tranchina, http://pixels.ncam-dt.com",
            "role": "Co-Developer"
        },
        
        # 2021 entries
        {
            "title": "ACM SIGGRAPH Digital Arts Community Website",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2021-01-01",
            "location": "Baton Rouge LA",
            "description": "Web Designer / Developer",
            "role": "Web Designer / Developer"
        },
        
        # 2016 entries
        {
            "title": "Diamonds in Dystopia - Documentation Website",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2016-01-01",
            "location": "Baton Rouge LA",
            "description": "Documentation of original work, http://diamonds.emdm.io"
        },
        
        # 2015 entries
        {
            "title": "Causeway - Documentation Website",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Documentation of original work, http://causeway.emdm.io"
        },
        {
            "title": "Poe's Magazines: Glimpses of Antebellum Print Culture",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Digital Humanities Website, http://literati.cct.lsu.edu/poesmagazineworld/"
        },
        {
            "title": "Humming Mississippi Desktop Data Visualization",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2015-01-01",
            "location": "Baton Rouge LA",
            "description": "Real-time Interactive Data Visualization, http://2.hmiss.in"
        },
        
        # 2014 entries
        {
            "title": "Poe's Magazine World Prototype",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "Used as a proof of concept to attract NEH funding, http://literati.cct.lsu.edu/magworld/"
        },
        {
            "title": "Humming Mississippi - Documentation Website",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "Documentation of original work, http://humming.emdm.io"
        },
        {
            "title": "Humming Mississippi Mobile Application",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2014-01-01",
            "location": "Baton Rouge LA",
            "description": "Real-time Interactive Data Visualization, http://hmiss.in"
        },
        
        # 2013 entries
        {
            "title": "IMG_1984 - Original Work",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2013-01-01",
            "location": "Baton Rouge LA",
            "description": "Original Work, http://popsnorkle.com/works/1984/"
        },
        {
            "title": "Conglomeration - Original Work",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2013-01-01",
            "location": "Baton Rouge LA",
            "description": "Original Work, http://popsnorkle.com/conglomeration"
        },
        {
            "title": "Antebellum Print Culture",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2013-01-01",
            "location": "Baton Rouge LA",
            "description": "Proof of concept for NEH grant, http://literati.cct.lsu.edu/apc.orig/"
        },
        {
            "title": "IMG_1984 - Interartive Gallery",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2013-01-01",
            "location": "International",
            "description": "Interartive: Art + Contemporary Thought Independent Online Gallery"
        },
        {
            "title": "Orbs - National Academy Museum Website",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2013-01-01",
            "location": "New York NY",
            "description": "National Academy Museum Website Independent Work Showcase"
        },
        {
            "title": "Conglomeration - Professor Jones Blog",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2013-01-01",
            "location": "International",
            "description": "Professor Jones Blog Independent"
        },
        
        # 2012 entries
        {
            "title": "mememe",
            "category": "1.3.1.7 Electronic dissemination of research",
            "date": "2012-01-01",
            "location": "International",
            "description": "0P3NR3P0.net GLI.TCH 2112"
        }
    ]
    
    print(f"🚀 Starting batch addition of {len(entries)} electronic dissemination entries...")
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
