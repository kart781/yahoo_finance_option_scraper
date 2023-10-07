Yahoo Finance Options Data Scraper

Overview

This project is a command-line tool that allows users to scrape options data from Yahoo Finance for selected stock ticker symbols using Selenium. The scraped data is then processed to extract desired values and save them into a CSV file. Additionally, the tool can send the CSV file via email to specified recipients.

Prerequisites

Before using this tool, ensure you have the following prerequisites installed:              

- Python 3.x
- Selenium
- Chrome WebDriver (or WebDriver for your preferred browser)
- pandas library
- smtplib for sending emails

Installation

- Python 3.x: If you don't have Python 3.x installed, download and install it from the official Python website.
  
- Selenium: You can install Selenium using pip:
  **pip install selenium**

- WebDriver: Download the WebDriver for your preferred browser (e.g., Chrome WebDriver) and ensure it's in your system's PATH. WebDriver download links can be found here:
  **Chrome WebDriver
  Firefox WebDriver
  **
  
- pandas library: You can install the pandas library using pip:
**  pip install pandas**

- smtplib for sending emails: smtplib is part of Python's standard library, so no additional installation is needed.

Output

The scraped options data will be processed and saved into a CSV file named options_data.csv in the project directory.

Email Notification

After scraping and processing, the tool will send the CSV file to the specified recipients via email.

Disclaimer

This tool is for educational and informational purposes only. Use it responsibly and ensure compliance with all relevant laws and regulations.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributors

karthikram781@gmail.com
Feel free to contribute to this project by submitting issues or pull requests.
