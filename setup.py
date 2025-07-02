#!/usr/bin/env python3
"""
Setup script for new users to configure the project.
"""

import os
import shutil

def setup_project():
    """Set up the project for a new user."""
    print("🚀 Setting up Notion API Interfacing Project")
    print("=" * 50)
    
    # Check if .env already exists
    if os.path.exists('.env'):
        print("✅ .env file already exists")
    else:
        # Copy .env.example to .env
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            print("✅ Created .env file from .env.example")
        else:
            print("❌ .env.example file not found")
            return
    
    print("\n📝 Next steps:")
    print("1. Edit the .env file and add your Notion credentials:")
    print("   - NOTION_TOKEN: Get from https://www.notion.so/my-integrations")
    print("   - DATABASE_ID: Get from your Notion database URL")
    print()
    print("2. Install dependencies:")
    print("   pipenv install")
    print()
    print("3. Test the setup:")
    print("   pipenv run python simple_query.py")
    print()
    print("🔐 Security reminder: Never commit your .env file to git!")

if __name__ == "__main__":
    setup_project()
