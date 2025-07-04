#!/usr/bin/env python3
"""
Batch Add Scholarship and Service Entries
=========================================

This script adds various scholarship and service entries to the Notion CV database:
- Publications (Shorter Works)
- Recordings
- Exhibition Catalogs/Reviews/Conference Proceedings
- Electronic dissemination of research
- Original works presented
- Other creative activities (Curation, Event Organization)
- Participation in Professional Meetings
- Other scholarly or creative activities
- Service activities

Run with: python batch_add_scholarship_service_final.py
or with pipenv: pipenv run python batch_add_scholarship_service_final.py
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
    """Main function to batch add all scholarship and service entries"""
    
    print("Starting batch add for Scholarship and Service entries...")
    print("=" * 60)
    
    # Track success/failure
    successful_entries = 0
    failed_entries = 0
    
    # Define all entries to add
    entries = [
        # 1.3.1.2 Shorter Works - Publications
        {
            'title': 'Digital Power: Activism, Advocacy, and the Influence of Women Online - Web Designer',
            'category': 'Scholarship',
            'date': '2021-01-01',
            'location': 'ACM SIGGRAPH Digital Arts Community',
            'description': 'Web Designer for Online Exhibition Catalog for Digital Power: Activism, Advocacy, and the Influence of Women Online, ACM SIGGRAPH Digital Arts Community. URL: https://dac.siggraph.org/exhibition/2021-digital-power',
            'url': 'https://dac.siggraph.org/exhibition/2021-digital-power'
        },
        {
            'title': 'Origins and Journeys: A Juried Online Exhibition - Web Designer',
            'category': 'Scholarship',
            'date': '2018-01-01',
            'location': 'ACM SIGGRAPH Digital Arts Community',
            'description': 'Web Designer for Online Exhibition Catalog for Origins and Journeys: A Juried Online Exhibition, ACM SIGGRAPH Digital Arts Community. URL: https://dac.siggraph.org/exhibition/2018-origins-and-journeys/',
            'url': 'https://dac.siggraph.org/exhibition/2018-origins-and-journeys/'
        },
        {
            'title': 'The Urgency of Reality: in a Hyper-Connected Age - Web Designer',
            'category': 'Scholarship',
            'date': '2018-01-01',
            'location': 'ACM SIGGRAPH Digital Arts Community',
            'description': 'Web Designer for Online Exhibition Catalog for The Urgency of Reality: in a Hyper-Connected Age, ACM SIGGRAPH Digital Arts Community. URL: https://dac.siggraph.org/exhibition/2018-the-urgency-of-reality-in-a-hyper-connected-age',
            'url': 'https://dac.siggraph.org/exhibition/2018-the-urgency-of-reality-in-a-hyper-connected-age'
        },
        {
            'title': 'Creative Data Mining Diamonds in Dystopia: An Interactive Poetry Web Application',
            'category': 'Scholarship',
            'date': '2017-01-01',
            'location': 'Media-N Journal',
            'description': 'Jesse Allison, Derick Ostrenko, Vincent Cellucci, "Creative Data Mining Diamonds in Dystopia: An Interactive Poetry Web Application," in "Uncovering News: Reporting and Forms of New Media" ed. Kevin Hamilton, Media-N 12, no. 3 (2017).',
            'url': ''
        },
        {
            'title': 'Immersive Expressions - Curator & Designer',
            'category': 'Scholarship',
            'date': '2017-06-01',
            'location': 'ACM SIGGRAPH Digital Arts Community',
            'description': 'Immersive Expressions. ACM SIGGRAPH Digital Arts Community, Curator & Designer, Online Exhibition Catalog. URL: https://dac.siggraph.org/exhibition/2017-06-immersive-expressions-virtual-reality-on-the-web',
            'url': 'https://dac.siggraph.org/exhibition/2017-06-immersive-expressions-virtual-reality-on-the-web'
        },
        {
            'title': 'Art of the App - Exhibition Catalog',
            'category': 'Scholarship',
            'date': '2016-01-01',
            'location': 'Louisiana State University',
            'description': 'Art of the App. Baton Rouge: Louisiana State University, 2016. Edited by Derick Ostrenko and Sarah Ferguson. Exhibition Catalog.',
            'url': ''
        },
        {
            'title': '15th International Conference on New Interfaces for Musical Expression Program Book',
            'category': 'Scholarship',
            'date': '2015-01-01',
            'location': 'Louisiana State University',
            'description': '15th International Conference on New Interfaces for Musical Expression Program Book. Edited by Jesse Allison, Edgar Berdahl, Stephen David Beck, Derick Ostrenko, Hye Yeon Nam, Esteban Maestre, Daniel Shannahan. Published in conjunction with the NIME 2015 conference and art exhibitions, shown at the Shaw Center for the Arts and Louisiana State University in Baton Rouge, LA.',
            'url': ''
        },
        {
            'title': 'Social(DIS)Order Online - Exhibition Catalog',
            'category': 'Scholarship',
            'date': '2012-01-01',
            'location': 'Louisiana State University',
            'description': 'Social(DIS)Order Online. Baton Rouge: Louisiana State University, 2012. Edited by Derick Ostrenko and Margot Herster. Online Exhibition Catalog.',
            'url': ''
        },
        
        # 1.3.1.5 Recordings
        {
            'title': 'Shell 360 - Virtual Reality Video',
            'category': 'Scholarship',
            'date': '2019-01-01',
            'location': 'Shell Chemical Plant, Geismar',
            'description': 'Shell 360 - Virtual Reality Video. 360 degree video made for Shell at their chemical plant in Geismar. Oversaw students: Daniel Davis and Khoa Bui.',
            'url': ''
        },
        {
            'title': 'Reflection: Interactive Experiential Collaboration',
            'category': 'Scholarship',
            'date': '2017-06-02',
            'location': 'TEDxLSU, Baton Rouge, LA',
            'description': 'Sandra Parks, Derick Ostrenko, Hye Yeon Nam, Jesse Allison. "Reflection: Interactive Experiential Collaboration" Interactive dance performance at TEDxLSU, Baton Rouge, LA. June 2, 2017.',
            'url': ''
        },
        {
            'title': 'Baton Rouge Arts Council Radio Show Interview',
            'category': 'Scholarship',
            'date': '2017-01-01',
            'location': 'iHeartMedia Stations',
            'description': 'Baton Rouge Arts Council Radio Show. iHeartMedia Stations. Interviewed about Red Stick International Festival.',
            'url': ''
        },
        {
            'title': 'An Interactive Poetry Experiment',
            'category': 'Scholarship',
            'date': '2016-03-05',
            'location': 'TEDxLSU, Baton Rouge, LA',
            'description': 'Vincent Cellucci, Jesse Allison, Derick Ostrenko. "An Interactive Poetry Experiment," Interactive poetry reading presented at TEDxLSU, Baton Rouge, LA. March 5, 2016.',
            'url': ''
        },
        {
            'title': 'P.S. 425 - Producer',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'Manship Theater at Shaw Center for the Arts',
            'description': '"P.S. 425," Of Moving Colors, Manship Theater at Shaw Center for the Arts, Producer',
            'url': ''
        },
        {
            'title': 'Rashaad Newsome\'s King of Arms - Co-Producer',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'New Orleans Museum of Art',
            'description': 'Rashaad Newsome\'s King of Arms, New Orleans Museum of Art, Co-Producer',
            'url': ''
        },
        {
            'title': 'Surreal Salon Soiree - Producer',
            'category': 'Scholarship',
            'date': '2013-01-01',
            'location': 'Baton Rouge Gallery',
            'description': 'Surreal Salon Soiree, Baton Rouge Gallery, Producer',
            'url': ''
        },
        {
            'title': 'Poison for the Impressionable: Art By Robert Williams - Producer',
            'category': 'Scholarship',
            'date': '2012-01-01',
            'location': 'Baton Rouge',
            'description': 'Poison for the Impressionable: Art By Robert Williams, Producer',
            'url': ''
        },
        
        # 1.3.1.6 Exhibition Catalogs, Reviews, Conference Proceedings (Sample - key entries)
        {
            'title': 'LSU is on the Frontier of Virtual Production - Article Feature',
            'category': 'Scholarship',
            'date': '2023-10-26',
            'location': 'Country Roads Magazine',
            'description': 'LSU is on the Frontier of Virtual Production, Newspaper Article, Jordan LaHaye Fontenot, Country Roads, 26 Oct 2023. URL: https://countryroadsmagazine.com/art-and-culture/visual-performing-arts/lsu-is-on-the-frontier-of-virtual-production',
            'url': 'https://countryroadsmagazine.com/art-and-culture/visual-performing-arts/lsu-is-on-the-frontier-of-virtual-production'
        },
        {
            'title': 'How is Baton Rouge\'s recent film boom impacting city culture? - Article Feature',
            'category': 'Scholarship',
            'date': '2023-01-30',
            'location': '225 Magazine',
            'description': 'How is Baton Rouge\'s recent film boom impacting city culture?, Newspaper Article, Domenic Purdy, 225 Magazine, 30 Jan 2023. URL: https://www.225batonrouge.com/our-city/baton-rouges-recent-film-boom-impacting-city-culture',
            'url': 'https://www.225batonrouge.com/our-city/baton-rouges-recent-film-boom-impacting-city-culture'
        },
        {
            'title': 'NEW TECHNOLOGIES ARE TRAINING THE NEXT GENERATION OF FILMMAKERS - Article Feature',
            'category': 'Scholarship',
            'date': '2022-10-06',
            'location': '225 Magazine',
            'description': 'NEW TECHNOLOGIES ARE TRAINING THE NEXT GENERATION OF FILMMAKERS—TO LIVE AND WORK RIGHT HERE IN LOUISIANA, Newspaper Article, Domenic Purdy, 225 Magazine, 06 Oct 2022. URL: https://www.225batonrouge.com/our-city/new-technologies-training-next-generation-filmmakers-live-work-right-louisiana',
            'url': 'https://www.225batonrouge.com/our-city/new-technologies-training-next-generation-filmmakers-live-work-right-louisiana'
        },
        {
            'title': 'NASA AWARDS $5 MILLION TO LSU FOR NEW DIGITAL FACILITY - Article Feature',
            'category': 'Scholarship',
            'date': '2022-09-02',
            'location': '225 Magazine',
            'description': 'NASA AWARDS $5 MILLION TO LSU FOR NEW DIGITAL FACILITY, Newspaper Article, 225 Magazine, 02 Sep 2022. URL: https://www.225batonrouge.com/our-city/lsu-create-digital-twin-nasas-michoud-assembly-facility',
            'url': 'https://www.225batonrouge.com/our-city/lsu-create-digital-twin-nasas-michoud-assembly-facility'
        },
        {
            'title': 'Diamonds in Dystopia - Conference Proceedings',
            'category': 'Scholarship',
            'date': '2017-08-01',
            'location': 'Web Audio Conference, London',
            'description': 'Jesse Allison, Derick Ostrenko, Vincent Cellucci. "Diamonds in Dystopia" Proceedings of 3rd Web Audio Conference, London, August 2017;82.',
            'url': ''
        },
        
        # 1.3.1.7 Electronic dissemination of research
        {
            'title': 'OSC Sender and Receiver - Custom Software',
            'category': 'Scholarship',
            'date': '2024-01-01',
            'location': 'GitHub',
            'description': 'OSC Sender and Receiver, Custom Software, Derick Ostrenko. URL: https://github.com/fredeerock/Simple-OSC-Sender-and-Receiver',
            'url': 'https://github.com/fredeerock/Simple-OSC-Sender-and-Receiver'
        },
        {
            'title': 'Simple Unreal Switchboard - Custom Software',
            'category': 'Scholarship',
            'date': '2024-01-01',
            'location': 'GitHub',
            'description': 'Simple Unreal Switchboard, Custom Software, Derick Ostrenko. URL: https://github.com/fredeerock/simpleUnrealSwitchboard',
            'url': 'https://github.com/fredeerock/simpleUnrealSwitchboard'
        },
        {
            'title': 'Images to Video - Custom Software',
            'category': 'Scholarship',
            'date': '2024-01-01',
            'location': 'GitHub',
            'description': 'Images to Video, Custom Software, Derick Ostrenko. URL: https://github.com/fredeerock/imagesToVideo',
            'url': 'https://github.com/fredeerock/imagesToVideo'
        },
        {
            'title': 'DMX Visualizer - Custom Software',
            'category': 'Scholarship',
            'date': '2024-01-01',
            'location': 'GitHub',
            'description': 'DMX Visualizer, Custom Software, Derick Ostrenko. URL: https://github.com/fredeerock/simpleDmxVisualizer',
            'url': 'https://github.com/fredeerock/simpleDmxVisualizer'
        },
        {
            'title': 'NASA TwinLink Digital Twin Platform',
            'category': 'Scholarship',
            'date': '2023-01-01',
            'location': 'NASA',
            'description': 'NASA TwinLink Digital Twin Platform, Greg Porter, Marc Aubanel, Gary Innerarity, Derick Ostrenko, Sidney Church, Jason Jamerson, Nick Lavergne, Chris Tranchina. URL: http://pixels.ncam-dt.com',
            'url': 'http://pixels.ncam-dt.com'
        },
        {
            'title': 'ACM SIGGRAPH Digital Arts Community Website',
            'category': 'Scholarship',
            'date': '2021-01-01',
            'location': 'ACM SIGGRAPH',
            'description': 'ACM SIGGRAPH Digital Arts Community Website, Web Designer / Developer.',
            'url': ''
        },
        {
            'title': 'Diamonds in Dystopia - Documentation Website',
            'category': 'Scholarship',
            'date': '2016-01-01',
            'location': 'Online',
            'description': 'Diamonds in Dystopia, Documentation of original work. URL: http://diamonds.emdm.io',
            'url': 'http://diamonds.emdm.io'
        },
        {
            'title': 'Causeway - Documentation Website',
            'category': 'Scholarship',
            'date': '2015-01-01',
            'location': 'Online',
            'description': 'Causeway, Documentation of original work. URL: http://causeway.emdm.io',
            'url': 'http://causeway.emdm.io'
        },
        {
            'title': 'Poe\'s Magazines: Glimpses of Antebellum Print Culture',
            'category': 'Scholarship',
            'date': '2015-01-01',
            'location': 'LSU Center for Computation & Technology',
            'description': 'Poe\'s Magazines: Glimpses of Antebellum Print Culture, Digital Humanities Website. URL: http://literati.cct.lsu.edu/poesmagazineworld/',
            'url': 'http://literati.cct.lsu.edu/poesmagazineworld/'
        },
        {
            'title': 'Humming Mississippi Desktop Data Visualization',
            'category': 'Scholarship',
            'date': '2015-01-01',
            'location': 'Online',
            'description': 'Humming Mississippi Desktop Data Visualization, Real-time Interactive Data Visualization. URL: http://2.hmiss.in',
            'url': 'http://2.hmiss.in'
        },
        
        # 1.3.3.1 Original works presented (Sample - key entries)
        {
            'title': 'Journey to Wellness - Artwork Commission',
            'category': 'Creative Work',
            'date': '2019-01-01',
            'location': 'Mary Bird Perkins Cancer Center, Baton Rouge, LA',
            'description': 'Journey to Wellness, Artwork Commission, Mary Bird Perkins Cancer Center, Baton Rouge, LA.',
            'url': ''
        },
        {
            'title': 'Diamonds in Dystopia - SXSW Presentation',
            'category': 'Creative Work',
            'date': '2017-01-01',
            'location': 'South by Southwest (SXSW), Austin, TX',
            'description': 'Diamonds in Dystopia, South by Southwest (SXSW). Austin, TX.',
            'url': ''
        },
        {
            'title': 'Causeway - Louisiana Contemporary',
            'category': 'Creative Work',
            'date': '2016-01-01',
            'location': 'Ogden Museum of Southern Art, Baton Rouge, LA',
            'description': 'Causeway, Louisiana Contemporary, Ogden Museum of Southern Art, Baton Rouge, LA',
            'url': ''
        },
        {
            'title': 'Reflection - LSU Annual Dance Concert',
            'category': 'Creative Work',
            'date': '2016-04-01',
            'location': 'Shaver Theater, Baton Rouge, LA',
            'description': 'Reflection, LSU Annual Dance Concert, Shaver Theater, Baton Rouge, LA',
            'url': ''
        },
        {
            'title': 'Humming Mississippi - ISEA Dubai',
            'category': 'Creative Work',
            'date': '2014-01-01',
            'location': 'New York University Art Center Project Space, Abu Dhabi, UAE',
            'description': 'Humming Mississippi, Resonance, ISEA: International Symposium for Electronic Art, New York University Art Center Project Space, Abu Dhabi, United Arab Emirates.',
            'url': ''
        },
        
        # 1.3.3.2 Other creative activities - Curation, Event Organization
        {
            'title': 'Immersive Expressions - Online Exhibition Curator',
            'category': 'Service',
            'date': '2017-01-01',
            'location': 'ACM SIGGRAPH Digital Arts Community',
            'description': 'Immersive Expressions, ACM SIGGRAPH Digital Arts Community Online Exhibition. Curator.',
            'url': ''
        },
        {
            'title': 'Art of the App - Exhibition Co-curator',
            'category': 'Service',
            'date': '2016-01-01',
            'location': 'LSU Student Union Gallery, Baton Rouge, LA',
            'description': 'Art of the App, LSU Student Union Gallery, Baton Rouge, LA, Co-curator',
            'url': ''
        },
        {
            'title': 'Kids Lab: Light and Shadow Play - Co-Organizer',
            'category': 'Service',
            'date': '2016-01-01',
            'location': 'Goodwood Library, Baton Rouge, LA',
            'description': 'Kids Lab: Light and Shadow Play, collaboration with Knock Knock Children\'s Museum for Red Stick International Festival, Goodwood Library Baton Rouge, LA. Co-Organizer.',
            'url': ''
        },
        {
            'title': 'NIME 2015 Installations - Curator',
            'category': 'Service',
            'date': '2015-01-01',
            'location': 'Shaw Center for the Arts, Baton Rouge, LA',
            'description': 'New Interfaces for Musical Expression 2015 Installations, Shaw Center for the Arts, Baton Rouge, LA. Curator.',
            'url': ''
        },
        {
            'title': 'Prospect 3+ Satellite Festival - Co-Organizer',
            'category': 'Service',
            'date': '2014-01-01',
            'location': 'Baton Rouge, LA',
            'description': 'Prospect 3+ Satellite Festival, Baton Rouge, LA, Co-Organizer.',
            'url': ''
        },
        {
            'title': 'social(dis)order Exhibition - Co-Curator',
            'category': 'Service',
            'date': '2012-01-01',
            'location': 'Glassell Gallery, Baton Rouge, LA',
            'description': 'social(dis)order with work by J. DeLappe, N. Bookchin, J. Cohen, Glassell Gallery, Baton Rouge, LA, Co-Curator',
            'url': ''
        },
        
        # 1.3.4 Professional Meetings and Conferences (Sample - key entries)
        {
            'title': 'Digital Twin Fundamentals in Manufacturing - NASA Presentation',
            'category': 'Service',
            'date': '2024-01-01',
            'location': 'Digital Twin Consortium Q1 Member Meeting',
            'description': 'Digital Twin Fundamentals in Manufacturing: Building an Industrial Twin of Twins for NASA, Digital Twin Consortium Q1 Member Meeting, Presentation by Greg Porter on behalf of Louisiana State University collaboration.',
            'url': ''
        },
        {
            'title': 'Digital Twin Consortium Panel - NASA Digital Twin Project',
            'category': 'Service',
            'date': '2023-12-14',
            'location': 'Digital Twin Consortium',
            'description': 'Digital Twin Consortium Panel - NASA Digital Twin Project, invited speaker, 14 Dec 2023, Derick Ostrenko, Marc Aubanel, Jason Jamerson.',
            'url': ''
        },
        {
            'title': 'Immersive Expressions: Virtual Reality on the Web - Panel Chair',
            'category': 'Service',
            'date': '2017-01-01',
            'location': 'ACM SIGGRAPH, Los Angeles, CA',
            'description': 'ACM SIGGRAPH. Panel Session of the ACM SIGGRAPH Digital Arts Community. "Immersive Expressions: Virtual Reality on the Web." Panel Chair. Los Angeles, CA.',
            'url': ''
        },
        {
            'title': 'Diamonds in Dystopia - SXSW Panel Member',
            'category': 'Service',
            'date': '2017-01-01',
            'location': 'South by Southwest (SXSW), Austin TX',
            'description': 'South by Southwest (SXSW). "Diamonds in Dystopia: A Poetry Performance Web App." Panel Member. Austin TX.',
            'url': ''
        },
        {
            'title': 'NIME 2015 Conference - Art Co-Chair',
            'category': 'Service',
            'date': '2015-05-31',
            'location': 'Louisiana State University, Baton Rouge, LA',
            'description': 'The 15th International Conference on New Interfaces for Musical Expression, May 31 - June 3, 2015, Louisiana State University, Baton Rouge, LA. Art Co-Chair.',
            'url': ''
        },
        
        # 1.3.5 Other scholarly activities
        {
            'title': 'Association for Computing Machinery - Member',
            'category': 'Service',
            'date': '2012-01-01',
            'location': 'Professional Organization',
            'description': 'Association for Computing Machinery - Professional membership',
            'url': ''
        },
        {
            'title': 'New Media Caucus - Member',
            'category': 'Service',
            'date': '2012-01-01',
            'location': 'Professional Organization',
            'description': 'New Media Caucus, 2012 - Present - Professional membership',
            'url': ''
        },
        {
            'title': 'SIGGRAPH Digital Arts Community - Committee Member',
            'category': 'Service',
            'date': '2012-01-01',
            'location': 'Professional Organization',
            'description': 'SIGGRAPH Digital Arts Community. Committee Member.',
            'url': ''
        },
        {
            'title': 'Manager, Media Research Studio',
            'category': 'Service',
            'date': '2012-01-01',
            'location': 'Louisiana State University',
            'description': '2012 - 15: Manager, Media Research Studio',
            'url': ''
        },
        {
            'title': 'Art Chair, NIME: New Interfaces for Musical Expression',
            'category': 'Service',
            'date': '2014-01-01',
            'location': 'Louisiana State University',
            'description': '2014 - 15: Art Chair, NIME: New Interfaces for Musical Expression',
            'url': ''
        },
        {
            'title': 'Co-manager, Art & Technology Lab',
            'category': 'Service',
            'date': '2013-01-01',
            'location': 'Louisiana State University',
            'description': '2013 - 15: Co-manager, Art & Technology Lab',
            'url': ''
        },
        
        # New standard testing methods/equipment
        {
            'title': 'Titan Computer System Setup for Machine Learning in Arts',
            'category': 'Service',
            'date': '2016-01-01',
            'location': 'Louisiana State University',
            'description': 'Set up a new computer system called "Titan" for experimentation on applications in machine learning in visual and sonic arts. Made possible by a grant from the La. Board of Regents.',
            'url': ''
        },
        {
            'title': 'K2 Computer System Setup for Grid Computing',
            'category': 'Service',
            'date': '2016-01-01',
            'location': 'Louisiana State University',
            'description': 'Set up a new computer system called "K2" for experimentation on grid computing applications in the arts.',
            'url': ''
        },
        {
            'title': 'Cloud-based Render Farm Construction',
            'category': 'Service',
            'date': '2015-01-01',
            'location': 'Louisiana State University',
            'description': 'Constructed a cloud based render farm using the OpenStack cloud platform for use with 3D graphics software such as Maya, Houdini, and Nuke.',
            'url': ''
        },
        {
            'title': 'HIVE Initiative - High-performance Interactive Visualization and Electroacoustics',
            'category': 'Service',
            'date': '2015-01-01',
            'location': 'Louisiana State University',
            'description': 'Started a new initiative called HIVE: High-performance Interactive Visualization and Electroacoustics. HIVE houses several new platforms for research existing between art and high-performance computing.',
            'url': ''
        },
        
        # 1.4 Service - Student organizations advised
        {
            'title': 'Digital Art and Design Association - Faculty Advisor',
            'category': 'Service',
            'date': '2011-01-01',
            'location': 'Louisiana State University',
            'description': '2011 - Present: Digital Art and Design Association, Faculty Advisor',
            'url': ''
        },
        {
            'title': 'ACM SIGGRAPH LSU Student Chapter - Faculty Advisor',
            'category': 'Service',
            'date': '2016-01-01',
            'location': 'Louisiana State University',
            'description': '2016 - 2019: ACM SIGGRAPH LSU Student Chapter',
            'url': ''
        },
        {
            'title': 'Black Artist Initiative - Faculty Advisor',
            'category': 'Service',
            'date': '2013-01-01',
            'location': 'Louisiana State University',
            'description': '2013 - 2019: Black Artist Initiative, Faculty Advisor',
            'url': ''
        },
        
        # University service (Sample - key entries)
        {
            'title': 'LSU School of Art Curriculum Committee - Chair',
            'category': 'Service',
            'date': '2015-01-01',
            'location': 'Louisiana State University',
            'description': '2015 - Present: LSU School of Art Curriculum Committee, Chair',
            'url': ''
        },
        {
            'title': 'Bachelor in Screen Arts Interdisciplinary Degree Program Steering Committee',
            'category': 'Service',
            'date': '2014-01-01',
            'location': 'Louisiana State University',
            'description': '2014 - Present: Bachelor in Screen Arts Interdisciplinary Degree Program Steering Committee, LSU, Member',
            'url': ''
        },
        {
            'title': 'Digital Media Arts & Engineering Faculty Review Committee',
            'category': 'Service',
            'date': '2013-01-01',
            'location': 'Louisiana State University',
            'description': '2013 - Present: Digital Media Arts & Engineering Faculty Review Committee, Member',
            'url': ''
        },
        {
            'title': 'University Moodle Development Advisory Committee',
            'category': 'Service',
            'date': '2012-01-01',
            'location': 'Louisiana State University',
            'description': '2012 - Present: University Moodle Development Advisory Committee, LSU, Member',
            'url': ''
        },
        {
            'title': 'CxC College of Art and Design Advisory Committee',
            'category': 'Service',
            'date': '2011-01-01',
            'location': 'Louisiana State University',
            'description': '2011 - Present: CxC College of Art and Design Advisory Committee, LSU, Member',
            'url': ''
        },
        
        # External service and judging
        {
            'title': 'Museum of Science & Industry STEAM Zone Advisory Council',
            'category': 'Service',
            'date': '2013-01-01',
            'location': 'Tampa, FL',
            'description': '2013: Museum of Science & Industry Advisory Council on Science, Technology, Art, Engineering, and Math (STEAM) Zone, Tampa, FL, Member',
            'url': ''
        },
        {
            'title': 'Women in Computer Science Game Jam - Judge',
            'category': 'Service',
            'date': '2015-01-01',
            'location': 'Louisiana State University',
            'description': '2015: Women in Computer Science Game Jam, Judge',
            'url': ''
        },
        {
            'title': 'LSU Summer Undergraduate Research Forum - Judge',
            'category': 'Service',
            'date': '2015-01-01',
            'location': 'Louisiana State University',
            'description': '2015: LSU Summer Undergraduate Research Forum, Judge',
            'url': ''
        },
        {
            'title': 'Stetson Digital Media Festival - Judge',
            'category': 'Service',
            'date': '2015-01-01',
            'location': 'Stetson University',
            'description': '2015: Stetson Digital Media Festival, Judge',
            'url': ''
        },
        {
            'title': 'Baton Rouge Arts Council Decentralized Arts Funding - Judge',
            'category': 'Service',
            'date': '2015-01-01',
            'location': 'Baton Rouge, LA',
            'description': '2015: Baton Rouge Arts Council Decentralized Arts Funding, Judge',
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
    print("\n" + "=" * 60)
    print("BATCH ADD SUMMARY")
    print("=" * 60)
    print(f"Total entries processed: {len(entries)}")
    print(f"Successfully added: {successful_entries}")
    print(f"Failed to add: {failed_entries}")
    
    if failed_entries > 0:
        print(f"\n⚠️  {failed_entries} entries failed to add. Please check the output above for details.")
    else:
        print("\n✅ All scholarship and service entries added successfully!")
    
    print(f"\nBatch add completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
