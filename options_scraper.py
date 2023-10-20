from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import csv
import os
import pandas as pd
from subprocess import call
 
options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
# if there are no CLI parameters
if len(sys.argv) <= 1:
    print('Ticker symbol CLI argument missing!')
    sys.exit(2)

# read the ticker from the CLI argument
ticker_symbol = sys.argv[1]


def scrape_stock(driver, ticker_symbol):
    url = f'https://finance.yahoo.com/quote/{ticker_symbol}/options?p={ticker_symbol}'

    # initialize a web driver instance to control a Chrome window
    driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
    )
    # set up the window size of the controlled browser
    driver.set_window_size(1920, 1080)
    # visit the target page
    driver.get(url)

    regular_market_price = driver \
            .find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="regularMarketPrice"]') \
            .text

    # Find the table element by its HTML structure or using XPath/CSS selector
    table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Col1-1-OptionContracts-Proxy"]/section/section[1]/div[2]/div/table/tbody'))
    )

    data = []
    # Iterate through the rows of the table
    for row in table.find_elements(By.TAG_NAME, "tr"):
        # Extract text from the <tr> element itself
        row_text = row.text
        data.append(row_text)

    driver.quit()

    final_data = []

    for i in data:
        input_string = i
        values_list = input_string.split()
        combined_element = ' '.join(map(str, values_list[1:4]))
        values_list = values_list[:1] + values_list[4:]
        values_list.insert(1, combined_element)
        output_string = values_list
        final_data.append(output_string)

    fields = ['Contract Name', 'Last Trade Date', 'Strike', 'Last Price', 'Bid', 'Ask', 'Change', '% Change', 'Volume', 'Open Interest', 'Implied Volatility']
    
    # data rows of csv file
    rows = final_data
    
    with open('Options.csv', 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(rows)

    with open('Options.csv', 'r') as input_file:
        reader = csv.reader(input_file)
        rows = [row for row in reader if any(field.strip() for field in row)]

    # Open a new CSV file for writing (or overwrite the input file)
    with open('output.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        
        # Write the filtered rows to the output CSV file
        for row in rows:
            writer.writerow(row)

    os.remove(r"C:\Users\karth\yahoo-finance-scraper\Options.csv")
    os.rename('output.csv', 'Options.csv')

    value = float(regular_market_price)
    df = pd.read_csv(r"C:\Users\karth\yahoo-finance-scraper\Options.csv")

    m = (df.iloc[(df['Strike']-value).abs().argsort()[:1]])
    index = (m.index).astype('int')
    a = index - 5
    new_df = pd.DataFrame(df.iloc[a-1])

    for i in range(12):
        f = df.iloc[a+i]
        new_df = new_df._append(f)

    new_df.to_csv(f"Required_Options_{ticker_symbol}.csv", index=False)

stocks = []

# scraping all market securities
for ticker_symbol in sys.argv[1:]:
    stocks.append(scrape_stock(driver, ticker_symbol))

os.remove(r"C:\Users\karth\yahoo-finance-scraper\Options.csv")

# def attachment_mail():
#     call(["python", "attachmentmail.py"])

# attachment_mail()