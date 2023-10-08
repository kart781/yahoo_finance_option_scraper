<h1>Yahoo Finance Options Data Scraper </h1>

</h3><ins>Overview </ins>ins></h3>

This project is a command-line tool that allows users to scrape options data from Yahoo Finance for selected stock ticker symbols using Selenium. The scraped data is then processed to extract desired values and save them into a CSV file. Additionally, the tool can send the CSV file via email to specified recipients.

</h3>Prerequisites </h3>
  
Before using this tool, ensure you have the following prerequisites installed:              

- Python 3.x
- Selenium
- Chrome WebDriver (or WebDriver for your preferred browser)
- pandas library
- smtplib for sending emails

</h3>Installation </h3>

Make sure you have the following packages installed before executing the files in this repository

- Python 3.x: If you don't have Python 3.x installed, download and install it from the official Python website.
- Selenium: You can install Selenium using pip:
  **pip install selenium**
- WebDriver: Download the WebDriver for your preferred browser (e.g., Chrome WebDriver) and ensure it's in your system's PATH. 
- pandas library: You can install the pandas library using pip:
**pip install pandas**
- smtplib for sending emails: smtplib is part of Python's standard library, so no additional installation is needed.

</h3>Configuration </h3>

Open the attachmentmail.py and option_scraper.py file and update the following settings:

- EMAIL_ADDRESS: Your email address for sending the CSV file.
- EMAIL_PASSWORD: Your email password or an application-specific password (if using Gmail).
- RECIPIENT_EMAILS: List of recipient email addresses to send the CSV file.
- TICKER_SYMBOLS: List of stock ticker symbols to scrape options data for.

</h3>Output </h3>
 
The scraped options data will be processed and saved into a CSV file named options_data.csv in the project directory.

</h3>Email Notification </h3>
 
After scraping and processing, the tool will send the CSV file to the specified recipients via email.

</h3>Disclaimer </h3>
 
This tool is for educational and informational purposes only. Use it responsibly and ensure compliance with all relevant laws and regulations.

</h3>Contributors </h3>
 
karthikram781@gmail.com
Feel free to contribute to this project by submitting issues or pull requests.
