# 🏠 Zillow Property Data Scraper

A Python script that scrapes property listings from a Zillow clone website and automatically submits the data to a Google Form.

## 🛠️ Prerequisites

- Python 3.x
- Chrome browser installed
- ChromeDriver (compatible with your Chrome version)

## 📦 Required Packages

```bash
pip install beautifulsoup4
pip install selenium
pip install requests
```

## 🔧 Setup & Configuration

1. Install all required packages using pip
2. Ensure ChromeDriver is installed and in your system PATH
3. Configure the target URLs in the script:
   - Zillow clone URL
   - Google Form URL

## 🚀 How It Works

The script performs two main functions:

### 1. Web Scraping 🕷️
- Fetches property data from the Zillow clone website
- Extracts:
  - Property addresses
  - Price information
  - Property listing links

### 2. Form Automation 📝
- Opens each form in Chrome browser
- Automatically fills in:
  - Address field
  - Price field
  - Property link
- Submits the form
- Repeats for all scraped properties

## 📋 Usage

Simply run the script:

```bash
python zillow_scraper.py
```

## ⚠️ Important Notes

- The script includes waiting times to handle page loading
- Browser window will be maximized during automation
- Chrome will remain open after execution (detach option enabled)
- Form submission is set to work with a Bulgarian submit button ("Изпращане")


## 🤝 Contributing

Feel free to fork and adapt this script for your own use case. Remember to respect websites' terms of service and implement appropriate delays between requests.
