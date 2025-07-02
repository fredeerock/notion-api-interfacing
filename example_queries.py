#!/usr/bin/env python3
"""
Example Analysis Queries

This file shows examples of how to use the analysis functions
to answer specific questions about your academic database.

You can modify these examples or ask VS Code chatbot to help
create new queries based on these patterns.
"""

from simple_query import *

def example_graduate_committees_analysis():
    """Example: Detailed graduate committee analysis."""
    print("🎓 GRADUATE COMMITTEES ANALYSIS")
    print("=" * 40)
    
    count, matches = count_graduate_committees()
    print(f"Total graduate committees: {count}")
    
    # Count by role
    roles = {}
    for match in matches:
        role = match.get('role', 'Unknown')
        if 'Chair' in role:
            roles['Chair'] = roles.get('Chair', 0) + 1
        elif 'Member' in role:
            roles['Member'] = roles.get('Member', 0) + 1
        else:
            roles['Other'] = roles.get('Other', 0) + 1
    
    print(f"Breakdown by role:")
    for role, count in roles.items():
        print(f"  {role}: {count}")
    
    # Count by year
    years = {}
    for match in matches:
        date = match.get('date')
        if date:
            year = date[:4]  # Extract year from YYYY-MM-DD
            years[year] = years.get(year, 0) + 1
    
    print(f"\nBreakdown by year:")
    for year in sorted(years.keys(), reverse=True):
        print(f"  {year}: {years[year]}")

def example_teaching_timeline():
    """Example: Teaching activities timeline."""
    print("\n👨‍🏫 TEACHING ACTIVITIES TIMELINE")
    print("=" * 40)
    
    teaching_entries = filter_by_category("1.2")
    year_data = get_entries_by_year()
    
    print("Teaching activities by year:")
    for year in sorted(year_data.keys(), reverse=True):
        teaching_this_year = [entry for entry in year_data[year] 
                             if entry['category'] and '1.2' in entry['category']]
        if teaching_this_year:
            print(f"  {year}: {len(teaching_this_year)} activities")

def example_conference_presentations():
    """Example: Find conference presentations."""
    print("\n🎤 CONFERENCE PRESENTATIONS")
    print("=" * 40)
    
    # Search for presentations
    presentations = search_text("presentation")
    conferences = search_text("conference")
    
    # Combine and deduplicate
    all_ids = set()
    unique_presentations = []
    
    for match in presentations + conferences:
        page_id = match['page']['id']
        if page_id not in all_ids:
            all_ids.add(page_id)
            # Only include if it seems like a presentation
            name = match.get('name', '').lower()
            description = match.get('description', '').lower()
            if 'present' in name or 'present' in description or 'conference' in name:
                unique_presentations.append(match)
    
    print(f"Found {len(unique_presentations)} potential presentations:")
    for match in unique_presentations[:10]:  # Show first 10
        print(f"  • {match['name']} ({match['date'] or 'No date'})")
    
    if len(unique_presentations) > 10:
        print(f"  ... and {len(unique_presentations) - 10} more")

def example_custom_search():
    """Example: Custom search for specific terms."""
    print("\n🔍 CUSTOM SEARCH EXAMPLES")
    print("=" * 40)
    
    # Search for specific programs or degrees
    digital_media = search_text("Digital Media Arts")
    print(f"Digital Media Arts & Engineering related: {len(digital_media)}")
    
    studio_art = search_text("Studio Art")
    print(f"Studio Art related: {len(studio_art)}")
    
    experimental_music = search_text("Experimental Music")
    print(f"Experimental Music related: {len(experimental_music)}")

def example_annual_summary(year=2023):
    """Example: Summary for a specific year."""
    print(f"\n📅 ANNUAL SUMMARY FOR {year}")
    print("=" * 40)
    
    year_data = get_entries_by_year()
    entries_this_year = year_data.get(year, [])
    
    print(f"Total activities in {year}: {len(entries_this_year)}")
    
    # Categorize
    categories = {}
    for entry in entries_this_year:
        category = entry['category'] or 'Uncategorized'
        # Get the main category (first part before first period)
        main_category = category.split('.')[0] if '.' in category else category
        categories[main_category] = categories.get(main_category, 0) + 1
    
    print(f"Breakdown by main category:")
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count}")

if __name__ == "__main__":
    print("📊 EXAMPLE ANALYSIS QUERIES")
    print("=" * 50)
    
    # Run all examples
    example_graduate_committees_analysis()
    example_teaching_timeline()
    example_conference_presentations()
    example_custom_search()
    example_annual_summary(2023)
    
    print("\n" + "=" * 50)
    print("💡 TIPS FOR VS CODE CHATBOT:")
    print("- Copy these examples and ask chatbot to modify them")
    print("- Ask: 'Help me find all [specific activity] in [year]'")
    print("- Ask: 'Count how many times I was [role] on committees'")
    print("- Ask: 'Show me my [category] activities by year'")
    print("- Use the simple_query.py functions as building blocks")
