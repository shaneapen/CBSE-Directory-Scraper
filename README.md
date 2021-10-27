# CBSE-Directory-Scraper
A Python script to scrape contact details of schools from CBSE directory using Selenium and BeautifulSoup

The script will scrape details from http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx into a sheet.

### How to Run the app?
1) Install selenium
2) Install Chrome Webdriver
3) Run `scrape_cbse.py`
4) The results will be extracted to `COMPLETE.CSV`

The `single-page.py` was made to test scraping from an individual page (`samplePage.txt` here) and output to `details.csv`

### Install Chrome Webdriver
1) Download chrome webdriver from http://chromedriver.chromium.org/downloads
2) Copy it into `/usr/local/bin/chromedriver on macOS`

OR Use `brew cask install chromedriver`
