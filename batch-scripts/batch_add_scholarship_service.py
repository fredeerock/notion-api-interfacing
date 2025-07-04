#!/usr/bin/env python3
"""
Batch script to add scholarship entries to Notion database.
This script adds entries under various "1.3 Scholarship" and "1.4 Service" categories.

Based on add_notion_entry.py structure with updated comments.
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
DATABASE_ID = os.getenv("DATABASE_ID")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_API_URL = "https://api.notion.com/v1"

# Check if required environment variables are set
if not DATABASE_ID or not NOTION_TOKEN:
    print("❌ Error: Missing required environment variables.")
    print("Please make sure DATABASE_ID and NOTION_TOKEN are set in your .env file.")
    exit(1)

# Headers for Notion API
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Scholarship and service entries
# Following updated guidelines:
# - Name: Descriptive and concise, no year in title
# - Description: Short description expanding on title when necessary
# - Location: Defaults to Baton Rouge LA
# - Role: Most appropriate role (PI, Co-PI, Presenter, etc.) when applicable
# - Date: YYYY-MM-DD format, defaults to January 1st if month/day not specified
# - URL: Optional, but if used should also be included in description
# - Show Page Contents: Generally False to avoid duplication
SCHOLARSHIP_ENTRIES = [
    # 1.3.1.2 Shorter Works
    {
        "Name": "Digital Power: Activism, Advocacy, and the Influence of Women Online",
        "Description": "ACM SIGGRAPH Digital Arts Community, Web Designer for Online Exhibition Catalog, available at https://dac.siggraph.org/exhibition/2021-digital-power.",
        "Category": "1.3.1.2 Shorter Works",
        "Location": "Baton Rouge LA",
        "Role": "Co-organizer",
        "Date": "2021-01-01",
        "URL": "https://dac.siggraph.org/exhibition/2021-digital-power",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Origins and Journeys: A Juried Online Exhibition",
        "Description": "ACM SIGGRAPH Digital Arts Community, Web Designer for Online Exhibition Catalog, available at https://dac.siggraph.org/exhibition/2018-origins-and-journeys/.",
        "Category": "1.3.1.2 Shorter Works",
        "Location": "Baton Rouge LA",
        "Role": "Co-organizer",
        "Date": "2018-01-01",
        "URL": "https://dac.siggraph.org/exhibition/2018-origins-and-journeys/",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "The Urgency of Reality: in a Hyper-Connected Age",
        "Description": "ACM SIGGRAPH Digital Arts Community, Web Designer for Online Exhibition Catalog, available at https://dac.siggraph.org/exhibition/2018-the-urgency-of-reality-in-a-hyper-connected-age.",
        "Category": "1.3.1.2 Shorter Works",
        "Location": "Baton Rouge LA",
        "Role": "Co-organizer",
        "Date": "2018-01-01",
        "URL": "https://dac.siggraph.org/exhibition/2018-the-urgency-of-reality-in-a-hyper-connected-age",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Creative Data Mining Diamonds in Dystopia: An Interactive Poetry Web Application",
        "Description": "Jesse Allison, Derick Ostrenko, Vincent Cellucci, in 'Uncovering News: Reporting and Forms of New Media' ed. Kevin Hamilton, Media-N 12, no. 3 (2017).",
        "Category": "1.3.1.2 Shorter Works",
        "Location": "Baton Rouge LA",
        "Date": "2017-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Immersive Expressions Online Exhibition Catalog",
        "Description": "ACM SIGGRAPH Digital Arts Community, Curator & Designer, Online Exhibition Catalog, available at https://dac.siggraph.org/exhibition/2017-06-immersive-expressions-virtual-reality-on-the-web.",
        "Category": "1.3.1.2 Shorter Works",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2017-01-01",
        "URL": "https://dac.siggraph.org/exhibition/2017-06-immersive-expressions-virtual-reality-on-the-web",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Art of the App Exhibition Catalog",
        "Description": "Art of the App. Baton Rouge: Louisiana State University, 2016. Edited by Derick Ostrenko and Sarah Ferguson. Exhibition Catalog.",
        "Category": "1.3.1.2 Shorter Works",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2016-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "15th International Conference on New Interfaces for Musical Expression Program Book",
        "Description": "Edited by Jesse Allison, Edgar Berdahl, Stephen David Beck, Derick Ostrenko, Hye Yeon Nam, Esteban Maestre, Daniel Shannahan. Published in conjunction with the NIME 2015 conference.",
        "Category": "1.3.1.2 Shorter Works",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2015-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Social(DIS)Order Online Exhibition Catalog",
        "Description": "Social(DIS)Order Online. Baton Rouge: Louisiana State University, 2012. Edited by Derick Ostrenko and Margot Herster. Online Exhibition Catalog.",
        "Category": "1.3.1.2 Shorter Works",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2012-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.1.5 Recordings
    {
        "Name": "Shell 360 - Virtual Reality Video",
        "Description": "360 degree video made for Shell at their chemical plant in Geismar. Oversaw students: Daniel Davis and Khoa Bui.",
        "Category": "1.3.1.5 Recordings",
        "Location": "Baton Rouge LA",
        "Date": "2019-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Reflection: Interactive Experiential Collaboration",
        "Description": "Sandra Parks, Derick Ostrenko, Hye Yeon Nam, Jesse Allison. Interactive dance performance at TEDxLSU, Baton Rouge, LA. June 2, 2017.",
        "Category": "1.3.1.5 Recordings",
        "Location": "Baton Rouge LA",
        "Role": "Presenter",
        "Date": "2017-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Baton Rouge Arts Council Radio Show Interview",
        "Description": "iHeartMedia Stations. Interviewed about Red Stick International Festival.",
        "Category": "1.3.1.5 Recordings",
        "Location": "Baton Rouge LA",
        "Date": "2017-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "An Interactive Poetry Experiment",
        "Description": "Vincent Cellucci, Jesse Allison, Derick Ostrenko. Interactive poetry reading presented at TEDxLSU, Baton Rouge, LA. March 5, 2016.",
        "Category": "1.3.1.5 Recordings",
        "Location": "Baton Rouge LA",
        "Role": "Presenter",
        "Date": "2016-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "P.S. 425 - Of Moving Colors Production",
        "Description": "Of Moving Colors, Manship Theater at Shaw Center for the Arts, Producer.",
        "Category": "1.3.1.5 Recordings",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Rashaad Newsome's King of Arms Co-Production",
        "Description": "Rashaad Newsome's King of Arms, New Orleans Museum of Art, Co-Producer.",
        "Category": "1.3.1.5 Recordings",
        "Location": "Baton Rouge LA",
        "Role": "Co-organizer",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Surreal Salon Soiree Production",
        "Description": "Surreal Salon Soiree, Baton Rouge Gallery, Producer.",
        "Category": "1.3.1.5 Recordings",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Poison for the Impressionable: Art By Robert Williams Production",
        "Description": "Poison for the Impressionable: Art By Robert Williams, Producer.",
        "Category": "1.3.1.5 Recordings",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2012-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.1.6 Exhibition Catalogs, Newspaper / Magazine Reviews
    {
        "Name": "LSU is on the Frontier of Virtual Production",
        "Description": "Newspaper Article, Jordan LaHaye Fontenot, Country Roads, 26 Oct 2023, available at https://countryroadsmagazine.com/art-and-culture/visual-performing-arts/lsu-is-on-the-frontier-of-virtual-production.",
        "Category": "1.3.1.6 Exhibition Catalogs, Newspaper / Magazine Reviews, Conference Proceedings",
        "Location": "Baton Rouge LA",
        "Date": "2023-01-01",
        "URL": "https://countryroadsmagazine.com/art-and-culture/visual-performing-arts/lsu-is-on-the-frontier-of-virtual-production",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "How is Baton Rouge's recent film boom impacting city culture?",
        "Description": "Newspaper Article, Domenic Purdy, 225 Magazine, 30 Jan 2023, available at https://www.225batonrouge.com/our-city/baton-rouges-recent-film-boom-impacting-city-culture.",
        "Category": "1.3.1.6 Exhibition Catalogs, Newspaper / Magazine Reviews, Conference Proceedings",
        "Location": "Baton Rouge LA",
        "Date": "2023-01-01",
        "URL": "https://www.225batonrouge.com/our-city/baton-rouges-recent-film-boom-impacting-city-culture",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "New Technologies Training Next Generation of Filmmakers",
        "Description": "Newspaper Article, Domenic Purdy, 225 Magazine, 06 Oct 2022, available at https://www.225batonrouge.com/our-city/new-technologies-training-next-generation-filmmakers-live-work-right-louisiana.",
        "Category": "1.3.1.6 Exhibition Catalogs, Newspaper / Magazine Reviews, Conference Proceedings",
        "Location": "Baton Rouge LA",
        "Date": "2022-01-01",
        "URL": "https://www.225batonrouge.com/our-city/new-technologies-training-next-generation-filmmakers-live-work-right-louisiana",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.1.7 Electronic dissemination of research
    {
        "Name": "OSC Sender and Receiver Custom Software",
        "Description": "Custom Software, Derick Ostrenko, available at https://github.com/fredeerock/Simple-OSC-Sender-and-Receiver.",
        "Category": "1.3.1.7 Electronic dissemination of research",
        "Location": "Baton Rouge LA",
        "Date": "2024-01-01",
        "URL": "https://github.com/fredeerock/Simple-OSC-Sender-and-Receiver",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Simple Unreal Switchboard Custom Software",
        "Description": "Custom Software, Derick Ostrenko, available at https://github.com/fredeerock/simpleUnrealSwitchboard.",
        "Category": "1.3.1.7 Electronic dissemination of research",
        "Location": "Baton Rouge LA",
        "Date": "2024-01-01",
        "URL": "https://github.com/fredeerock/simpleUnrealSwitchboard",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Images to Video Custom Software",
        "Description": "Custom Software, Derick Ostrenko, available at https://github.com/fredeerock/imagesToVideo.",
        "Category": "1.3.1.7 Electronic dissemination of research",
        "Location": "Baton Rouge LA",
        "Date": "2024-01-01",
        "URL": "https://github.com/fredeerock/imagesToVideo",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "DMX Visualizer Custom Software",
        "Description": "Custom Software, Derick Ostrenko, available at https://github.com/fredeerock/simpleDmxVisualizer.",
        "Category": "1.3.1.7 Electronic dissemination of research",
        "Location": "Baton Rouge LA",
        "Date": "2024-01-01",
        "URL": "https://github.com/fredeerock/simpleDmxVisualizer",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "NASA TwinLink Digital Twin Platform",
        "Description": "Greg Porter, Marc Aubanel, Gary Innerarity, Derick Ostrenko, Sidney Church, Jason Jamerson, Nick Lavergne, Chris Tranchina, available at http://pixels.ncam-dt.com.",
        "Category": "1.3.1.7 Electronic dissemination of research",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2023-01-01",
        "URL": "http://pixels.ncam-dt.com",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.3.1 Original works presented
    {
        "Name": "Journey to Wellness Artwork Commission",
        "Description": "Artwork Commission, Mary Bird Perkins Cancer Center, Baton Rouge, LA.",
        "Category": "1.3.3.1 Original works presented",
        "Location": "Baton Rouge LA",
        "Date": "2019-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Diamonds in Dystopia at SXSW",
        "Description": "Diamonds in Dystopia, South by Southwest (SXSW). Austin, TX.",
        "Category": "1.3.3.1 Original works presented",
        "Location": "Baton Rouge LA",
        "Role": "Presenter",
        "Date": "2017-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Causeway at Louisiana Contemporary",
        "Description": "Causeway, Louisiana Contemporary, Ogden Museum of Southern Art, Baton Rouge, LA.",
        "Category": "1.3.3.1 Original works presented",
        "Location": "Baton Rouge LA",
        "Role": "Presenter",
        "Date": "2016-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.3.2 Other creative activities
    {
        "Name": "Immersive Expressions ACM SIGGRAPH Online Exhibition",
        "Description": "Immersive Expressions, ACM SIGGRAPH Digital Arts Community Online Exhibition. Curator.",
        "Category": "1.3.3.2 Other creative activities",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2017-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Art of the App Exhibition Co-Curation",
        "Description": "Art of the App, LSU Student Union Gallery, Baton Rouge, LA, Co-curator.",
        "Category": "1.3.3.2 Other creative activities",
        "Location": "Baton Rouge LA",
        "Role": "Co-organizer",
        "Date": "2016-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "social(dis)order Exhibition Co-Curation",
        "Description": "social(dis)order with work by J. DeLappe, N. Bookchin, J. Cohen, Glassell Gallery, Baton Rouge, LA, Co-Curator.",
        "Category": "1.3.3.2 Other creative activities",
        "Location": "Baton Rouge LA",
        "Role": "Co-organizer",
        "Date": "2012-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.4 Participation in Other Professional Meetings
    {
        "Name": "Digital Twin Fundamentals in Manufacturing Presentation",
        "Description": "Digital Twin Fundamentals in Manufacturing: Building an Industrial Twin of Twins for NASA, Digital Twin Consortium Q1 Member Meeting, Presentation by Greg Porter on behalf of Louisiana State University collaboration.",
        "Category": "1.3.4 Participation in Other Professional Meetings, Symposia, Workshops, and Conferences",
        "Location": "Baton Rouge LA",
        "Role": "Presenter",
        "Date": "2024-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Digital Twin Consortium Panel - NASA Digital Twin Project",
        "Description": "Digital Twin Consortium Panel - NASA Digital Twin Project, invited speaker, 14 Dec 2023, Derick Ostrenko, Marc Aubanel, Jason Jamerson.",
        "Category": "1.3.4 Participation in Other Professional Meetings, Symposia, Workshops, and Conferences",
        "Location": "Baton Rouge LA",
        "Role": "Presenter",
        "Date": "2023-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "ACM SIGGRAPH Immersive Expressions Panel Chair",
        "Description": "ACM SIGGRAPH. Panel Session of the ACM SIGGRAPH Digital Arts Community. 'Immersive Expressions: Virtual Reality on the Web.' Panel Chair. Los Angeles, CA.",
        "Category": "1.3.4 Participation in Other Professional Meetings, Symposia, Workshops, and Conferences",
        "Location": "Baton Rouge LA",
        "Role": "Organizer",
        "Date": "2017-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.5.1 Membership in professional organizations
    {
        "Name": "Association for Computing Machinery Membership",
        "Description": "Association for Computing Machinery member.",
        "Category": "1.3.5.1 Membership in professional organizations",
        "Location": "Baton Rouge LA",
        "Date": "2015-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "New Media Caucus Membership",
        "Description": "New Media Caucus, 2012 - Present.",
        "Category": "1.3.5.1 Membership in professional organizations",
        "Location": "Baton Rouge LA",
        "Date": "2012-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "SIGGRAPH Digital Arts Community Committee Member",
        "Description": "SIGGRAPH Digital Arts Community. Committee Member.",
        "Category": "1.3.5.1 Membership in professional organizations",
        "Location": "Baton Rouge LA",
        "Date": "2015-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.3.7 Other research Support/Grant Activities
    {
        "Name": "Urban-level Digital Twin and AI Technology for Scalable Education",
        "Description": "LSU Student Technology Fee, $144,269, Yongcheol Lee (PI), Derick Ostrenko, Nina S Lam, Thomas Douthat, Z. George Xue, Paul Miller, Kisung Lee, Chao Sun, Sabarethinam Kameshwar, Jason Jamerson, Soo J Jo, Fabiana Trindade da Silva, Mostafiz, Rubayet Bin.",
        "Category": "1.3.7 Other research Support/Grant Activities",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2024-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Phase 2: Digital Twin: Building next-generation visualization talent for NASA",
        "Description": "$2,500,000, National Aeronautics & Space Administration (NASA), Co-PI.",
        "Category": "1.3.7 Other research Support/Grant Activities",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2023-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "LSU DDEM Esports & Video Games Initiative",
        "Description": "$50,000, DXC Technology, PI.",
        "Category": "1.3.7 Other research Support/Grant Activities",
        "Location": "Baton Rouge LA",
        "Role": "PI",
        "Date": "2023-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Digital Twins: The New Frontier in Manufacturing",
        "Description": "$5,000,000, National Aeronautics & Space Administration (NASA), Co-PI.",
        "Category": "1.3.7 Other research Support/Grant Activities",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2022-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "The Virtual Production Program at LSU",
        "Description": "Training and Reskilling Future Filmmakers of Louisiana in Emerging Media, $1,250,000, Louisiana Department of Economic Development (LED), Co-PI.",
        "Category": "1.3.7 Other research Support/Grant Activities",
        "Location": "Baton Rouge LA",
        "Role": "Co-PI",
        "Date": "2021-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.4.1 Student organizations advised
    {
        "Name": "Digital Art and Design Association Faculty Advisor",
        "Description": "2011 - Present: Digital Art and Design Association, Faculty Advisor.",
        "Category": "1.4.1 Student organizations advised",
        "Location": "Baton Rouge LA",
        "Date": "2011-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "ACM SIGGRAPH LSU Student Chapter Advisor",
        "Description": "2016 - 2019: ACM SIGGRAPH LSU Student Chapter advisor.",
        "Category": "1.4.1 Student organizations advised",
        "Location": "Baton Rouge LA",
        "Date": "2016-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Black Artist Initiative Faculty Advisor",
        "Description": "2013 - 2019: Black Artist Initiative, Faculty Advisor.",
        "Category": "1.4.1 Student organizations advised",
        "Location": "Baton Rouge LA",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.4.3 University service
    {
        "Name": "LSU School of Art Curriculum Committee Chair",
        "Description": "2015 - Present: LSU School of Art Curriculum Committee, Chair.",
        "Category": "1.4.3 University service",
        "Location": "Baton Rouge LA",
        "Date": "2015-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Bachelor in Screen Arts Interdisciplinary Degree Program Steering Committee",
        "Description": "2014 - Present: Bachelor in Screen Arts Interdisciplinary Degree Program Steering Committee, LSU, Member.",
        "Category": "1.4.3 University service",
        "Location": "Baton Rouge LA",
        "Date": "2014-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "Digital Media Arts & Engineering Faculty Review Committee",
        "Description": "2013 - Present: Digital Media Arts & Engineering Faculty Review Committee, Member.",
        "Category": "1.4.3 University service",
        "Location": "Baton Rouge LA",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    {
        "Name": "University Moodle Development Advisory Committee",
        "Description": "2012 - Present: University Moodle Development Advisory Committee, LSU, Member.",
        "Category": "1.4.3 University service",
        "Location": "Baton Rouge LA",
        "Date": "2012-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    },
    # 1.4.4.1 Advisory boards, commissions, or agencies
    {
        "Name": "Museum of Science & Industry Advisory Council on STEAM Zone",
        "Description": "Museum of Science & Industry Advisory Council on Science, Technology, Art, Engineering, and Math (STEAM) Zone, Tampa, FL, Member.",
        "Category": "1.4.4.1 Advisory boards, commissions, or agencies",
        "Location": "Baton Rouge LA",
        "Date": "2013-01-01",
        "Show Page Contents": False,
        "Pinned": False,
        "page_content": []
    }
]


def create_notion_page(entry_data):
    """Create a new page in the Notion database with the specified data."""
    
    # Build the page content blocks
    children = []
    for content_item in entry_data.get("page_content", []):
        if content_item["type"] == "paragraph":
            children.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content_item["text"]}
                    }]
                }
            })
        elif content_item["type"] == "heading_2":
            children.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content_item["text"]}
                    }]
                }
            })
        elif content_item["type"] == "heading_1":
            children.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content_item["text"]}
                    }]
                }
            })
        elif content_item["type"] == "heading_3":
            children.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": content_item["text"]}
                    }]
                }
            })
    
    # Build the page data
    page_data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {},
        "children": children
    }
    
    # Add properties based on what's provided in entry_data
    if "Name" in entry_data:
        page_data["properties"]["Name"] = {
            "title": [{
                "text": {"content": entry_data["Name"]}
            }]
        }
    
    if "Description" in entry_data:
        page_data["properties"]["Description"] = {
            "rich_text": [{
                "text": {"content": entry_data["Description"]}
            }]
        }
    
    if "Category" in entry_data:
        page_data["properties"]["Category"] = {
            "select": {"name": entry_data["Category"]}
        }
    
    if "Location" in entry_data:
        page_data["properties"]["Location"] = {
            "select": {"name": entry_data["Location"]}
        }
    
    if "Role" in entry_data:
        page_data["properties"]["Role"] = {
            "select": {"name": entry_data["Role"]}
        }
    
    if "Date" in entry_data:
        page_data["properties"]["Date"] = {
            "date": {"start": entry_data["Date"]}
        }
    
    if "URL" in entry_data:
        page_data["properties"]["URL"] = {
            "url": entry_data["URL"]
        }
    
    if "Show Page Contents" in entry_data:
        page_data["properties"]["Show Page Contents"] = {
            "checkbox": entry_data["Show Page Contents"]
        }
    
    if "Pinned" in entry_data:
        page_data["properties"]["Pinned"] = {
            "checkbox": entry_data["Pinned"]
        }
    
    # Make the API request
    response = requests.post(
        f"{NOTION_API_URL}/pages",
        headers=HEADERS,
        json=page_data
    )
    
    if response.status_code == 200:
        result = response.json()
        page_id = result.get("id", "Unknown")
        page_url = result.get("url", "Unknown")
        print(f"✅ Successfully created: {entry_data['Name']}")
        return True
    else:
        print(f"❌ Failed to create: {entry_data['Name']}")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        
        # Try to parse error details
        try:
            error_data = response.json()
            if "message" in error_data:
                print(f"   Error Message: {error_data['message']}")
        except:
            pass
        return False


def main():
    """Main function to run the batch script."""
    print("🚀 Adding scholarship and service entries to Notion database...")
    print(f"   Database ID: {DATABASE_ID}")
    print(f"   Total entries to add: {len(SCHOLARSHIP_ENTRIES)}")
    print("-" * 60)
    
    success_count = 0
    category_counts = {}
    
    for i, entry in enumerate(SCHOLARSHIP_ENTRIES, 1):
        print(f"[{i}/{len(SCHOLARSHIP_ENTRIES)}] Adding: {entry['Name']}")
        
        if create_notion_page(entry):
            success_count += 1
            category = entry['Category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        print()  # Add spacing between entries
    
    print("-" * 60)
    print(f"Completed! Successfully added {success_count}/{len(SCHOLARSHIP_ENTRIES)} entries.")
    
    # Show breakdown by category
    if category_counts:
        print(f"📊 Category breakdown:")
        for category, count in sorted(category_counts.items()):
            print(f"   • {category}: {count}")
    
    if success_count < len(SCHOLARSHIP_ENTRIES):
        print("⚠️  Some entries failed to add. Check the error messages above.")
    else:
        print("🎉 All scholarship and service entries added successfully!")


if __name__ == "__main__":
    main()
