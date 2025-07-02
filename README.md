# Notion Database Entry & Analysis Tool

This project provides scripts to easily add entries to your Notion database and analyze existing data. Perfect for managing academic CV databases with categories like teaching, scholarship, and service activities.

## � Table of Contents

- [Quick Start](#-quick-start)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
  - [Adding New Entries](#adding-new-entries)
- [Database Analysis](#-database-analysis)
  - [Interactive Analysis Tool](#interactive-analysis-tool)
  - [Simple Query Tool](#simple-query-tool)
  - [VS Code Chatbot Integration](#vs-code-chatbot-integration)
- [Customizing Entry Data](#customizing-entry-data)
- [Configuration](#️-configuration)
- [Managing Dependencies](#-managing-dependencies)

## �🚀 Quick Start

1. **Clone and setup:**
   ```bash
   git clone <your-repo-url>
   cd notion-api-interfacing
   python setup.py  # This will guide you through setup
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   ```

3. **Configure your credentials:**
   - Edit `.env` with your Notion token and database ID
   - See [Configuration](#configuration) section below

4. **Test it works:**
   ```bash
   pipenv run python simple_query.py
   ```

## 📦 Installation & Setup

### Initial Setup (one time only)

1. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your actual Notion token and database ID:
   ```
   NOTION_TOKEN=your_notion_bearer_token_here
   DATABASE_ID=your_database_id_here
   ```

2. **Install dependencies using pipenv:**
   ```bash
   pipenv install
   ```

3. **Make scripts executable (optional):**
   ```bash
   chmod +x *.py
   ```

### Running Scripts

There are two main ways to run the scripts with pipenv:

#### Method 1: Using `pipenv run` (recommended for single commands)
```bash
# Add a new entry to Notion
pipenv run python add_notion_entry.py

# Run database analysis
pipenv run python simple_query.py
pipenv run python analyze_database.py

# Inspect database schema
pipenv run python inspect_database.py

# Run example queries
pipenv run python example_queries.py
```

#### Method 2: Using `pipenv shell` (for multiple commands)
```bash
pipenv shell                    # Activate virtual environment
python add_notion_entry.py     # Run any script
python simple_query.py         # Run another script
exit                           # Exit when done
```

## 📝 Usage

### Adding New Entries

1. Open `add_notion_entry.py` in your editor
2. Modify the `ENTRY_DATA` dictionary (around line 25) with your desired values:
   - `Name`: The title of your entry
   - `Description`: A description for your entry  
   - `Category`: Choose from available academic CV categories
   - `Location`: Providence RI or Baton Rouge LA
   - `Role`: Presenter, Organizer, Co-organizer, Guest Critic, Guest Lecture
   - `Date`: Date in YYYY-MM-DD format
   - `page_content`: Array of content blocks for the page body

3. Run the script using pipenv:
   ```bash
   pipenv run python add_notion_entry.py
   ```

## 📊 Database Analysis

### Interactive Analysis Tool

Run the comprehensive analysis tool:

```bash
pipenv run python analyze_database.py
```

This provides an interactive menu with options to:
- Count entries by category, location, or role
- Search for specific terms
- Filter by categories
- Analyze by year
- Specific analyses (graduate committees, teaching, etc.)

### Simple Query Tool

For quick queries and VS Code chatbot integration:

```bash
pipenv run python simple_query.py
```

This script provides simple functions you can use:

```python
# Import the functions (in pipenv shell or using pipenv run python)
from simple_query import *

# Quick queries
count_total()                    # Total entries
count_graduate_committees()      # Graduate committee count
search_text("presentation")      # Search for text
filter_by_category("teaching")   # Filter by category
get_entries_by_year()           # Group by year

# Quick summaries
quick_graduate_committees()      # Graduate committee analysis
quick_teaching_summary()         # Teaching activities summary
quick_scholarship_summary()      # Scholarship summary
quick_service_summary()         # Service summary
```

### VS Code Chatbot Integration

You can ask the VS Code chatbot to help you write custom queries using the `simple_query.py` functions. For example:

- "Using simple_query.py, help me find all presentations I gave in 2023"
- "Write a query to count how many courses I've created"
- "Help me analyze my conference participation over the years"

#### Interactive Python (for VS Code chatbot queries)
```bash
# Start Python in the pipenv environment
pipenv run python

# Then in Python:
>>> from simple_query import *
>>> count_graduate_committees()
>>> search_text("conference")
>>> quit()
```

### Database Schema Inspector

To see all available properties and their options in your database, run:

```bash
pipenv run python inspect_database.py
```

This will show you the current database schema, property types, and available options for select fields.

## 🔧 Managing Dependencies

```bash
pipenv install requests         # Add a new package
pipenv install --dev pytest    # Add development dependency
pipenv uninstall package_name  # Remove a package
pipenv graph                   # Show dependency tree
pipenv check                   # Check for security vulnerabilities
```

## 🛠️ Useful Commands

```bash
pipenv --venv                  # Show virtual environment path
pipenv --py                    # Show Python interpreter path
pipenv clean                   # Remove unused packages
```

## Customizing Entry Data

The `ENTRY_DATA` dictionary contains the following available properties:

```python
ENTRY_DATA = {
    "Name": "Your Entry Title",                    # Required: Title of the entry
    "Description": "Your entry description",       # Optional: Rich text description
    "Category": "1. Documentation",               # Optional: Select from available categories
    "Location": "Providence RI",                  # Optional: Providence RI or Baton Rouge LA
    "Role": "Presenter",                          # Optional: Presenter, Organizer, Co-organizer, Guest Critic, Guest Lecture
    "Date": "2025-07-02",                        # Optional: Date in YYYY-MM-DD format
    "URL": "https://example.com",                 # Optional: URL link
    "Show Page Contents": True,                   # Optional: True/False checkbox
    "Pinned": False,                             # Optional: True/False checkbox
    "page_content": [
        {
            "type": "paragraph",
            "text": "Your paragraph content"
        },
        {
            "type": "heading_2",
            "text": "Your Heading"
        }
        # Add more content blocks as needed
    ]
}
```

### Available Category Options

The Category property supports many academic CV categories. Run `python inspect_database.py` to see the full list, but common ones include:
- `1. Documentation`
- `1.2 Teaching`
- `1.3 Scholarship`
- `1.4 Service`
- `2. Supporting Material`

### Location Options
- `Providence RI`
- `Baton Rouge LA`

### Role Options
- `Presenter`
- `Organizer`
- `Co-organizer`
- `Guest Critic`
- `Guest Lecture`

### Supported Content Types

- `paragraph`: Regular text paragraph
- `heading_1`: Large heading
- `heading_2`: Medium heading  
- `heading_3`: Small heading

## Example

```python
ENTRY_DATA = {
    "Name": "Conference Presentation - July 2, 2025",
    "Description": "Presented research on machine learning applications in education",
    "Category": "1.3.4 Participation in Professional Academic Events",
    "Location": "Providence RI",
    "Role": "Presenter",
    "Date": "2025-07-02",
    "URL": "https://conference-website.com",
    "Show Page Contents": True,
    "Pinned": False,
    "page_content": [
        {
            "type": "heading_1",
            "text": "ML in Education Conference - July 2, 2025"
        },
        {
            "type": "paragraph", 
            "text": "Today I presented my research on applying machine learning techniques to personalized learning systems."
        },
        {
            "type": "heading_2",
            "text": "Key Points Covered"
        },
        {
            "type": "paragraph",
            "text": "• Adaptive learning algorithms\n• Student performance prediction\n• Personalized content recommendation"
        }
    ]
}
```

## ⚙️ Configuration

### Environment Variables

The project uses environment variables to keep sensitive information secure:

- `NOTION_TOKEN`: Your Notion integration bearer token
- `DATABASE_ID`: Your Notion database ID

These are loaded from a `.env` file that should NOT be committed to git.

### Getting Your Credentials

1. **Notion Token**: 
   - Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
   - Create a new integration
   - Copy the "Internal Integration Token"

2. **Database ID**: 
   - Open your Notion database in a browser
   - Copy the 32-character string from the URL after the last slash

### Security Note

Never commit your `.env` file to git. The `.gitignore` file is configured to exclude it automatically.
