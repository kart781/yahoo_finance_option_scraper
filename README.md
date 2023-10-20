<h1>Yahoo Finance Options Data Scraper </h1>

</h2><ins>Overview </ins></h2>

This project is a command-line tool that allows users to scrape options data from Yahoo Finance for selected stock ticker symbols using Selenium. The scraped data is then processed to extract desired values and save them into a CSV file. Additionally, the tool can send the CSV file via email to specified recipients.

</h2><ins>Prerequisites </ins></h2>

Before using this tool, ensure you have the following prerequisites installed:              

- Python 3.x
- Selenium
- Chrome WebDriver (or WebDriver for your preferred browser)
- pandas library
- smtplib for sending emails

</h2><ins>Installation </ins></h2>

Make sure you have the following packages installed before executing the files in this repository

- Python 3.x: If you don't have Python 3.x installed, download and install it from the official Python website.
- Selenium: You can install Selenium using pip:
  **pip install selenium**
- WebDriver: Download the WebDriver for your preferred browser (e.g., Chrome WebDriver) and ensure it's in your system's PATH. 
- pandas library: You can install the pandas library using pip:
**pip install pandas**
- smtplib for sending emails: smtplib is part of Python's standard library, so no additional installation is needed.

</h2><ins>Configuration </ins></h2>

Open the attachmentmail.py and option_scraper.py file and update the following settings:

- EMAIL_ADDRESS: Your email address for sending the CSV file.
- EMAIL_PASSWORD: Your email password or an application-specific password (if using Gmail).
- RECIPIENT_EMAILS: List of recipient email addresses to send the CSV file.
- TICKER_SYMBOLS: List of stock ticker symbols to scrape options data for. This is the user input which must be given in the command line while executing the program.

</h2><ins>Usage </ins></h2>

- Clone this repository to your local machine: **git clone https://github.com/kart781/yahoo_finance_option_scraper**
- Navigate to the project directory: **cd yahoo-finance-scraper**
- Edit the attachmentmail.py file to configure your email settings and specify the stock ticker symbols you want to scrape options data for while running it in the command line.
- Run the tool from the command line: **python options_scraper.py AAPL META TSLA GOOG AMZN**

</h2><ins>Additional Features </ins></h2><br>

Few of the changes in the past weeks are:<br />

<ins>Implied Volatility Trigger</ins> : A new addition to the tool is the trigger.py script. This script monitors the implied volatility difference for your selected stock ticker symbols. When the difference exceeds a specified limit, the script will trigger an email, alerting you to the significant change.
<br />

<ins>Cleaning CSV Files</ins> : You now have the option to easily manage your workspace with the shortcut.py script. Run it to remove all CSV files within the project folder, providing you with a clean slate for your data.
<br />

</h2><ins>Output </ins></h2>
 
The scraped options data will be processed and saved into a CSV file named options_data.csv in the project directory.

</h2><ins>Email Notification </ins></h2>
 
After scraping and processing, the tool will send the CSV file to the specified recipients via email.

</h2><ins>Disclaimer </ins></h2>
 
This tool is for educational and informational purposes only. Use it responsibly and ensure compliance with all relevant laws and regulations.

</h2><ins>Contributions </ins></h2>
 
karthikram781@gmail.com
Feel free to contribute to this project by submitting issues or pull requests.
