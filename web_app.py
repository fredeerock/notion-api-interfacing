#!/usr/bin/env python3
"""
Notion Markdown Preview Web Application

A local web application that allows you to:
1. Paste markdown content
2. Preview the rendered markdown
3. Edit entry details (title, category, date, etc.)
4. Submit to your Notion database

Usage: pipenv run python web_app.py
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import markdown
import json
import subprocess
import sys
import os
from datetime import datetime

app = Flask(__name__)

# Get available categories from notion_categories.md
def get_categories():
    """Extract categories from notion_categories.md file"""
    categories = []
    try:
        with open('notion_categories.md', 'r') as f:
            content = f.read()
            # Extract category lines that start with numbers
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if line and (line.startswith('####') or line.startswith('###')) and any(char.isdigit() for char in line):
                    # Remove markdown headers and clean up
                    category = line.replace('####', '').replace('###', '').strip()
                    if category and not category.startswith('#'):
                        categories.append(category)
    except FileNotFoundError:
        # Fallback categories if file not found
        categories = [
            "1.3.1.1 Peer-Reviewed Publications",
            "1.3.1.4 Creative Works and Exhibitions", 
            "1.3.1.7 Electronic Dissemination of Research",
            "1.3.1.9 Media Coverage of Scholarship",
            "1.3.3.1 Original Creative Works & Presentations",
            "1.3.3.2 Curation and Event Organization",
            "1.3.4 Participation in Professional Academic Events"
        ]
    return sorted(categories)

@app.route('/')
def index():
    """Main page with markdown input form"""
    categories = get_categories()
    return render_template('index.html', categories=categories)

@app.route('/preview', methods=['POST'])
def preview():
    """Convert markdown to HTML and show preview with edit form"""
    data = request.get_json()
    markdown_content = data.get('markdown', '')
    
    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code'])
    
    return jsonify({
        'html': html_content,
        'success': True
    })

@app.route('/submit', methods=['POST'])
def submit_to_notion():
    """Submit the entry to Notion database"""
    try:
        # Get form data
        title = request.form.get('title', '').strip()
        category = request.form.get('category', '').strip()
        date = request.form.get('date', '').strip()
        location = request.form.get('location', '').strip()
        description = request.form.get('description', '').strip()
        url = request.form.get('url', '').strip()
        role = request.form.get('role', '').strip()
        
        # Validate required fields
        if not all([title, category, date, description]):
            return jsonify({
                'success': False,
                'error': 'Missing required fields: title, category, date, and description are required.'
            })
        
        # Build command to call add_notion_entry.py
        cmd = [
            sys.executable,
            'add_notion_entry.py',
            '--title', title,
            '--category', category,
            '--date', date,
            '--location', location,
            '--description', description
        ]
        
        # Add optional fields
        if url:
            cmd.extend(['--url', url])
        if role:
            cmd.extend(['--role', role])
        
        # Execute the command
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        return jsonify({
            'success': True,
            'message': f'Successfully added "{title}" to Notion database!',
            'output': result.stdout
        })
        
    except subprocess.CalledProcessError as e:
        return jsonify({
            'success': False,
            'error': f'Error adding to Notion: {e}',
            'output': e.stdout,
            'stderr': e.stderr
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        })

if __name__ == '__main__':
    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("🚀 Starting Notion Markdown Preview Web Application...")
    print("📝 Open your browser to: http://localhost:5001")
    print("⏹️  Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5001)
