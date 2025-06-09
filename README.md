# OAA Directory Scraper (Playwright Version)

This script uses [Playwright](https://playwright.dev/python/) to scrape contact information for architectural practices from the Ontario Association of Architects (OAA) directory.

It extracts the practice name, address, phone number, and email address from a user-specified range of pages and saves the results to a CSV file.

---

## Prerequisites

- Python 3.8 or higher

---

## Installation

1. **Clone or download this repository** (or just this script):
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip3 install playwright
   pip3 install csv  # csv is part of Python's standard library, so this is just for clarity
   ```

4. **Install Playwright browsers:**
   ```bash
   python3 -m playwright install
   ```

---

## Usage

Run the script with:
```bash
python3 oaa_playwright_scraper.py
```

You will be prompted to enter the start and end page numbers (e.g., 1 and 3 to scrape pages 1, 2, and 3).

The script will:
- Visit each page in the specified range
- Scrape the practice name, address, phone, and email for each entry
- Append the results to a file called `oaa_contacts.csv`

---

## Output

The output CSV file will have the following columns:
- practice name
- address
- phone number
- e-mail

---

## Troubleshooting

- **No data or errors?**
  - Make sure the OAA directory website is accessible.
  - Ensure you have installed Playwright and run `playwright install`.
  - Check that all dependencies are installed in your virtual environment.

- **Want to see the browser window?**
  - Change `headless=True` to `headless=False` in the script to watch the scraping in action.

---

## License
This script is for educational and personal use. Please respect the terms of service of the OAA directory. 
