# palinkeedin

This project is designed to crawl job postings from LinkedIn based on specified keywords or base (city/region), and organize the results into a CSV table.

## Features
- Input search keywords and base (optional)
- Automatically log in to LinkedIn (enter your username and password)
- Crawl job information: company, position, job description (JD), and job link
- Export results as a CSV file

## Installation
```bash
pip install -r requirements.txt
```

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the search keyword and base as prompted
3. Enter your LinkedIn username (email) and password
4. The browser will open automatically and log in to LinkedIn
5. The program will crawl job postings and save the results to `output/jobs.csv`

## Notes
- LinkedIn has strong anti-crawling measures. It is recommended to crawl at a low frequency to avoid account bans
- Please use your own LinkedIn account to log in
- This project is for learning and research purposes only. Do not use it for commercial purposes 