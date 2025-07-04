#!/usr/bin/env python3
"""
Batch Add Complete Media Coverage and Exhibition Catalogs
=========================================================

This script adds all the missing exhibition catalogs, media coverage, reviews, 
and conference proceedings entries to the Notion CV database.

Run with: python batch_add_media_coverage_complete.py
or with pipenv: pipenv run python batch_add_media_coverage_complete.py
"""

import sys
import subprocess
from datetime import datetime

def run_add_entry(entry_data):
    """Run the add_notion_entry.py script with the given entry data"""
    
    # Build command arguments
    cmd = [
        sys.executable, 
        'add_notion_entry.py',
        '--title', entry_data['title'],
        '--category', entry_data['category'],
        '--date', entry_data['date'],
        '--location', entry_data['location'],
        '--description', entry_data['description']
    ]
    
    # Add URL if provided
    if 'url' in entry_data and entry_data['url']:
        cmd.extend(['--url', entry_data['url']])
    
    try:
        print(f"\nAdding: {entry_data['title']}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Successfully added")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error adding entry: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main function to batch add all media coverage and exhibition catalog entries"""
    
    print("Starting batch add for Media Coverage and Exhibition Catalogs...")
    print("=" * 70)
    
    # Track success/failure
    successful_entries = 0
    failed_entries = 0
    
    # Define all entries to add
    entries = [
        # 2022 - Additional entries not previously added
        {
            'title': 'NASA AWARDS $5 MILLION TO LSU FOR NEW DIGITAL FACILITY',
            'category': 'Scholarship',
            'date': '2022-09-02',
            'location': '225 Magazine',
            'description': 'NASA AWARDS $5 MILLION TO LSU FOR NEW DIGITAL FACILITY, Newspaper Article, 225 Magazine, 02 Sep 2022. URL: https://www.225batonrouge.com/our-city/lsu-create-digital-twin-nasas-michoud-assembly-facility',
            'url': 'https://www.225batonrouge.com/our-city/lsu-create-digital-twin-nasas-michoud-assembly-facility'
        },
        {
            'title': 'LSU Supports Moon Mission and Beyond',
            'category': 'Scholarship',
            'date': '2022-09-01',
            'location': 'Science X',
            'description': 'LSU Supports Moon Mission and Beyond, Blog, Science X, 01 Sep 2022. URL: https://sciencex.com/wire-news/423488352/lsu-supports-moon-mission-and-beyond.html',
            'url': 'https://sciencex.com/wire-news/423488352/lsu-supports-moon-mission-and-beyond.html'
        },
        {
            'title': 'THE ART OF VIRTUAL PRODUCTION: LSU\'S JANIECE CAMPBELL TALKS WORLDBUILDING',
            'category': 'Scholarship',
            'date': '2022-06-14',
            'location': 'We\'ll Fix it in Post',
            'description': 'THE ART OF VIRTUAL PRODUCTION: LSU\'S JANIECE CAMPBELL TALKS WORLDBUILDING FOR \'THE SNOW\' WITH UNREAL ENGINE, Blog, We\'ll Fix it in Post, 14 Jun 2022. URL: https://wellfixitinpost.com/virtual-production-lsu-students-worldbuilding-with-unreal-engine',
            'url': 'https://wellfixitinpost.com/virtual-production-lsu-students-worldbuilding-with-unreal-engine'
        },
        
        # 2017
        {
            'title': 'Diamonds in Dystopia - Web Audio Conference Proceedings',
            'category': 'Scholarship',
            'date': '2017-08-01',
            'location': 'Web Audio Conference, London',
            'description': 'Jesse Allison, Derick Ostrenko, Vincent Cellucci. "Diamonds in Dystopia" Proceedings of 3rd Web Audio Conference, London, August 2017;82.',
            'url': ''
        },
        
        # 2016
        {
            'title': 'Causeway - Louisiana Contemporary Exhibition Catalog',
            'category': 'Scholarship',
            'date': '2016-08-01',
            'location': 'Louisiana Contemporary',
            'description': '"Causeway," Louisiana Contemporary. August 2016. Exhibition Catalog.',
            'url': ''
        },
        {
            'title': 'How sound becomes art - Art Collection Design Review',
            'category': 'Scholarship',
            'date': '2016-04-01',
            'location': 'Art Collection Design, Taiwan',
            'description': 'Pohao Chi, "How sound becomes art," review of Humming Mississippi, by Derick Ostrenko and Jesse Allison, Art Collection Design, Taiwan, April 2016.',
            'url': ''
        },
        {
            'title': 'Causeway - Web Audio Conference',
            'category': 'Scholarship',
            'date': '2016-04-01',
            'location': 'Georgia Institute of Technology, Atlanta, GA',
            'description': 'Jesse Allison, Derick Ostrenko, Vincent Cellucci. "Causeway," In Web Audio Conference, Georgia Institute of Technology, Atlanta, GA.',
            'url': ''
        },
        {
            'title': 'Causeway - ISEA 2016 Conference Program',
            'category': 'Scholarship',
            'date': '2016-05-01',
            'location': 'City University of Hong Kong',
            'description': '"Causeway," International Symposium on Electronic Art (ISEA 2016), City University of Hong Kong. Conference Program.',
            'url': ''
        },
        {
            'title': 'Causeway - NIME 2016 Conference Program',
            'category': 'Scholarship',
            'date': '2016-07-01',
            'location': 'Brisbane, Griffith University',
            'description': '"Causeway," New Interfaces for Musical Expression (NIME 2016), Brisbane, Griffith University. Conference Program.',
            'url': ''
        },
        {
            'title': 'Reflection - LSU Annual Dance Concert Program',
            'category': 'Scholarship',
            'date': '2016-04-01',
            'location': 'Shaver Theater, Baton Rouge, LA',
            'description': '"Reflection," LSU Annual Dance Concert Program, Shaver Theater, Program, April 2016.',
            'url': ''
        },
        
        # 2015
        {
            'title': 'Gallery mixes physical touch with visual art, music',
            'category': 'Scholarship',
            'date': '2015-06-13',
            'location': 'The Advocate',
            'description': 'Robin Miller, "Gallery mixes physical touch with visual art, music," The Advocate, June 13, 2015.',
            'url': ''
        },
        {
            'title': 'Art show brings wearable literature to the catwalk',
            'category': 'Scholarship',
            'date': '2015-12-02',
            'location': 'The Advocate',
            'description': '"Art show brings wearable literature to the catwalk," The Advocate, December 2, 2015.',
            'url': ''
        },
        {
            'title': 'Uncommon Thread Wearable Art Show 2015: Epilogue',
            'category': 'Scholarship',
            'date': '2015-12-05',
            'location': 'DIG Magazine',
            'description': '"Uncommon Thread Wearable Art Show 2015: Epilogue," DIG Magazine, December 5, 2015.',
            'url': ''
        },
        {
            'title': '10 fall events you shouldn\'t miss in Baton Rouge',
            'category': 'Scholarship',
            'date': '2015-09-01',
            'location': 'NOLA.com',
            'description': '"10 fall events you shouldn\'t miss in Baton Rouge" NOLA.com, September, 2015.',
            'url': ''
        },
        {
            'title': 'Humming Mississippi - Web Audio Conference Paris',
            'category': 'Scholarship',
            'date': '2015-01-01',
            'location': 'IRCAM @ Centre Pompidou & Mozilla, Paris',
            'description': '"Humming Mississippi," Web Audio Conference, IRCAM @ Centre Pompidou & Mozilla, Paris. Conference Program.',
            'url': ''
        },
        {
            'title': 'La. International Film Festival\'s eclectic program continues',
            'category': 'Scholarship',
            'date': '2015-05-07',
            'location': 'The Advocate',
            'description': '"La. International Film Festival\'s eclectic program continues through Sunday," The Advocate, May 7, 2015',
            'url': ''
        },
        {
            'title': 'HIVE - ISEA 2015 Conference Program',
            'category': 'Scholarship',
            'date': '2015-08-01',
            'location': 'Simon Fraser University, Vancouver, CA',
            'description': '"HIVE," International Symposium on Electronic Art (ISEA 2015), Simon Fraser University, Vancouver, CA. Conference Program.',
            'url': ''
        },
        {
            'title': 'Causeway - Katrina & Rita: A Decade of Recovery & Response',
            'category': 'Scholarship',
            'date': '2015-08-01',
            'location': 'LSU Office of Economic Development',
            'description': '"Causeway," Katrina & Rita: A Decade of Recovery & Response, LSU Office of Economic Development, Show program.',
            'url': ''
        },
        {
            'title': 'Digital Divide - LSU Digital Media Center Concert Program',
            'category': 'Scholarship',
            'date': '2015-01-01',
            'location': 'LSU Digital Media Center',
            'description': '"Digital Divide," LSU Digital Media Center, Concert Program.',
            'url': ''
        },
        
        # 2014
        {
            'title': 'Show Offs - 225 Baton Rouge',
            'category': 'Scholarship',
            'date': '2014-01-01',
            'location': '225 Baton Rouge',
            'description': '"Show Offs," 225 Baton Rouge, January 1, 2014.',
            'url': ''
        },
        {
            'title': 'Humming Mississippi - ISEA 2014 Catalog',
            'category': 'Scholarship',
            'date': '2014-11-01',
            'location': 'Zayed University, Dubai, UAE',
            'description': '"Humming Mississippi," International Symposium on Electronic Art (ISEA 2014), Zayed University, Dubai, UAE. Catalog.',
            'url': ''
        },
        {
            'title': 'Humming Mississippi - NIME 2014 Conference Program',
            'category': 'Scholarship',
            'date': '2014-06-01',
            'location': 'Goldsmiths, University of London',
            'description': '"Humming Mississippi," New Interfaces for Musical Expression (NIME 2014). Conference Program.',
            'url': ''
        },
        {
            'title': 'A Vision of the Future - Dig Magazine',
            'category': 'Scholarship',
            'date': '2014-05-06',
            'location': 'Dig Magazine',
            'description': 'Cody Worsham, "A Vision of the Future," Dig, May 6, 2014',
            'url': ''
        },
        {
            'title': 'Simplified Expressive Mobile Development with NexusUI',
            'category': 'Scholarship',
            'date': '2014-06-01',
            'location': 'Goldsmiths, University of London',
            'description': 'Ben Taylor, Jesse Allison, Will Conlin, Yemin Oh, Danny Holmes. "Simplified Expressive Mobile Development with NexusUI, NexusUp and NexusDrop," In Proceedings of the International Conference on New Musical Interfaces for Musical Expression. Goldsmiths, University of London. Reference to work, Humming Mississippi.',
            'url': ''
        },
        {
            'title': 'Resonance Panel Discussion - Abu Dhabi Exhibition Catalog',
            'category': 'Scholarship',
            'date': '2014-11-01',
            'location': 'New York University Abu Dhabi Arts Center Project Space',
            'description': 'Resonance Panel Discussion, Abu Dhabi: New York University Abu Dhabi Arts Center Project Space, November 2014. Exhibition Catalog.',
            'url': ''
        },
        {
            'title': 'Did you Know - LSU College of Art & Design Alumni Magazine',
            'category': 'Scholarship',
            'date': '2014-01-01',
            'location': 'LSU College of Art & Design',
            'description': 'Angela Harwood, "Did you Know," LSU College of Art & Design Alumni Magazine.',
            'url': ''
        },
        {
            'title': 'Pierrot Lunaire Presentation - LSU School of Music',
            'category': 'Scholarship',
            'date': '2014-01-01',
            'location': 'LSU School of Music',
            'description': '"Pierrot Lunaire Presentation", LSU School of Music, Concert Program.',
            'url': ''
        },
        
        # 2013
        {
            'title': 'Right Off the River - The Advocate',
            'category': 'Scholarship',
            'date': '2013-12-21',
            'location': 'The Advocate',
            'description': 'Robin Miller, "Right Off the River," The Advocate, December 21, 2013.',
            'url': ''
        },
        {
            'title': 'Art Exhibit Showcases University Faculty Work',
            'category': 'Scholarship',
            'date': '2013-11-10',
            'location': 'Daily Reveille',
            'description': 'Michael Tarver, "Art Exhibit Showcases University Faculty Work," Daily Reveille, November 10, 2013.',
            'url': ''
        },
        {
            'title': 'Right Here Now - LSU Museum of Art Show Catalog',
            'category': 'Scholarship',
            'date': '2013-11-01',
            'location': 'LSU Museum of Art',
            'description': '"Right Here Now," LSU Museum of Art, Show Catalog, 2013.',
            'url': ''
        },
        {
            'title': 'Conglomeration - Different Games Conference Program',
            'category': 'Scholarship',
            'date': '2013-04-01',
            'location': 'NYU',
            'description': '"Conglomeration," Different Games Conference, NYU, Conference Program, 2013.',
            'url': ''
        },
        {
            'title': 'LSU School of Art students use supercomputer to render digital art projects',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'NBC 33',
            'description': '"LSU School of Art students use supercomputer to render digital art projects," NBC 33.',
            'url': ''
        },
        {
            'title': 'Right Here, Now exhibition features work of LSU faculty-artists',
            'category': 'Scholarship',
            'date': '2013-11-12',
            'location': 'Nola.com',
            'description': 'Chelsea Brasted, "\'Right Here, Now\' exhibition features work of LSU faculty-artists," Nola.com, November 12, 2013.',
            'url': ''
        },
        {
            'title': 'Uncertain Languages de Derick Ostrenko en Demolden Video Project',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'Fundacion Santander Creativa',
            'description': '"\'Uncertain Languages\' de Derick Ostrenko en Demolden Video Project," Fundacion Santander Creativa.',
            'url': ''
        },
        {
            'title': 'LSU art students use supercomputer - CBS News',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'CBS News Channel 5',
            'description': '"LSU art students use supercomputer," CBS News Channel 5.',
            'url': ''
        },
        {
            'title': 'Digital Humanities at LSU - Inside CCT',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'Inside CCT',
            'description': 'Tatiana Johnson, "Digital Humanities at LSU," Inside CCT, 2013.',
            'url': ''
        },
        {
            'title': 'Frame of Minds brings together Baton Rouge artistic entities',
            'category': 'Scholarship',
            'date': '2013-10-12',
            'location': 'The Times Picayune',
            'description': 'Chelsea Brasted, "\'Frame of Minds\' brings together Baton Rouge artistic entities for screenings, discussion," The Times Picayune, October 12, 2013.',
            'url': ''
        },
        {
            'title': 'Render farm - Inside CCT',
            'category': 'Scholarship',
            'date': '2013-08-31',
            'location': 'Inside CCT',
            'description': 'Angela Harwood, "Render farm," Inside CCT, August 31, 2013, 3.',
            'url': ''
        },
        {
            'title': 'Work Showcase - National Academy Museum and School',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'National Academy Museum and School',
            'description': '"Work Showcase," National Academy Museum and School & School, Website.',
            'url': ''
        },
        {
            'title': 'IMG_1984 in Interartive: Art & Copyright',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'Interartive',
            'description': 'IMG_1984 in "Interartive: A platform for contemporary art and thought," special issue, Art & Copyright, no. 50.',
            'url': ''
        },
        {
            'title': 'Hot Mess: Peepshow by Jack Foran - Group Show Review',
            'category': 'Scholarship',
            'date': '2013-02-21',
            'location': 'ArtVoice',
            'description': 'Jack Foran, "Hot Mess: Peepshow by Jack Foran, Group Show Review, Change Industries," ArtVoice, February 21, 2013.',
            'url': ''
        },
        {
            'title': 'Peepshow 2013: Hot Mess - Squeaky Wheel Show Catalog',
            'category': 'Scholarship',
            'date': '2013-02-01',
            'location': 'Squeaky Wheel',
            'description': '"Peepshow 2013: Hot Mess", Squeaky Wheel, Show Catalog.',
            'url': ''
        },
        {
            'title': 'Conglomeration - Currents New Media Festival Catalog',
            'category': 'Scholarship',
            'date': '2013-06-01',
            'location': 'Currents New Media Festival',
            'description': '"Conglomeration," Currents New Media Festival, Show Catalog, 2013.',
            'url': ''
        },
        
        # 2012
        {
            'title': 'Transmodal Journeys: Digital Adventures - ISEA 2012',
            'category': 'Scholarship',
            'date': '2012-09-01',
            'location': 'Albuquerque, NM',
            'description': '"Transmodal Journeys: Digital Adventures," in International Symposium on Electronic Art (ISEA 2012) Conference program, Albuquerque, NM.',
            'url': ''
        },
        {
            'title': 'New Faculty - LSU College of Art & Design Annual Report',
            'category': 'Scholarship',
            'date': '2012-01-01',
            'location': 'LSU College of Art & Design',
            'description': '"New Faculty," LSU College of Art & Design Annual Report.',
            'url': ''
        },
        {
            'title': 'Click Here for Disorder - DIG Magazine',
            'category': 'Scholarship',
            'date': '2012-01-01',
            'location': 'DIG Magazine',
            'description': 'Kasha Lishman, "Click Here for Disorder" DIG Magazine. Art Review for social(dis)order curated by Derick Ostrenko & Margot Herster.',
            'url': ''
        },
        {
            'title': 'Social(dis)Order - 225Alive.com',
            'category': 'Scholarship',
            'date': '2012-01-01',
            'location': '225Alive.com',
            'description': 'Ben Aaron, "Social(dis)Order," 225Alive.com.',
            'url': ''
        },
        {
            'title': 'Social(dis)order - Culture Candy',
            'category': 'Scholarship',
            'date': '2012-01-01',
            'location': 'Culture Candy',
            'description': '"Social(dis)order," Culture Candy.',
            'url': ''
        },
        {
            'title': 'Movie Subz - OP3N R3P0 Catalog',
            'category': 'Scholarship',
            'date': '2012-01-01',
            'location': 'OP3N R3P0',
            'description': '"Movie Subz," OP3N R3P0, Catalog, 2012.',
            'url': ''
        },
        
        # 2011
        {
            'title': 'Tear Catchers - Beyond the Brickyard Catalog',
            'category': 'Scholarship',
            'date': '2011-01-01',
            'location': 'Archie Bray Foundation',
            'description': 'Tear Catchers, "Beyond the Brickyard," Catalog, Archie Bray Foundation.',
            'url': ''
        },
        
        # 2010
        {
            'title': 'Phone Talks - RISD XYZ Magazine',
            'category': 'Scholarship',
            'date': '2010-01-01',
            'location': 'RISD XYZ Magazine',
            'description': '"Phone Talks," RISD XYZ Magazine.',
            'url': ''
        },
        {
            'title': 'What is Digital Art? - DIG Magazine',
            'category': 'Scholarship',
            'date': '2010-01-01',
            'location': 'DIG Magazine',
            'description': '"What is Digital Art?," DIG Magazine.',
            'url': ''
        },
        {
            'title': 'Alumni Update - Derick Ostrenko - Stetson University',
            'category': 'Scholarship',
            'date': '2010-01-01',
            'location': 'Stetson University',
            'description': '"Alumni Update - Derick Ostrenko," Stetson University Digital Art.',
            'url': ''
        },
        
        # 2008
        {
            'title': 'The Year\'s Top 10 Visual Art Exhibit - Creative Loafing',
            'category': 'Scholarship',
            'date': '2008-12-24',
            'location': 'Creative Loafing',
            'description': 'Megan Voeller, "The Year\'s Top 10 Visual Art Exhibit," review of Mobile Performance Group by Matt Roberts, Derick Ostrenko, et al. Creative Loafing, December 24, 2008.',
            'url': ''
        },
        {
            'title': 'Mentored Field Experience in Brazil - Stetson Newsletter',
            'category': 'Scholarship',
            'date': '2008-01-01',
            'location': 'Stetson University',
            'description': '"Mentored Field Experience in Brazil," Stetson University Newsletter.',
            'url': ''
        },
        
        # 2007
        {
            'title': 'Students Study Art & Architecture - Brazilian Press',
            'category': 'Scholarship',
            'date': '2007-01-01',
            'location': 'Associação Brasileira de Imprensa',
            'description': '"Students Study Art & Architecture," Associação Brasileira de Imprensa (Brazilian Press Association).',
            'url': ''
        },
        {
            'title': 'Mobile Performance Group - Mercury News San Diego',
            'category': 'Scholarship',
            'date': '2007-01-01',
            'location': 'Mercury News San Diego City Beat',
            'description': '"Mobile Performance Group," Mercury News San Diego City Beat',
            'url': ''
        },
        {
            'title': 'Mobile Performance Group - Stetson Newsletter',
            'category': 'Scholarship',
            'date': '2007-01-01',
            'location': 'Stetson University',
            'description': '"Mobile Performance Group," Stetson University Newsletter.',
            'url': ''
        },
        
        # 2006
        {
            'title': 'Junk Parts + Creativity = Music',
            'category': 'Scholarship',
            'date': '2006-01-01',
            'location': 'Daytona Beach News Journal',
            'description': '"Junk Parts + Creativity = Music," Daytona Beach News Journal',
            'url': ''
        }
    ]
    
    # Process each entry
    for entry in entries:
        success = run_add_entry(entry)
        if success:
            successful_entries += 1
        else:
            failed_entries += 1
    
    # Print summary
    print("\n" + "=" * 70)
    print("BATCH ADD SUMMARY")
    print("=" * 70)
    print(f"Total entries processed: {len(entries)}")
    print(f"Successfully added: {successful_entries}")
    print(f"Failed to add: {failed_entries}")
    
    if failed_entries > 0:
        print(f"\n⚠️  {failed_entries} entries failed to add. Please check the output above for details.")
    else:
        print("\n✅ All media coverage and exhibition catalog entries added successfully!")
    
    print(f"\nBatch add completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
