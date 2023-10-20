import pandas as pd

# Sample DataFrame
df = pd.read_csv(r'C:\Users\karth\yahoo-finance-scraper\Required_Options_AAPL.csv')

df['Implied Volatility'] = df['Implied Volatility'].apply(lambda x: float(x.replace('%', '')))

value = df.iloc[6, 10]

results = []

# Iterate through each row and subtract the user variable from the existing column
for index, row in df.iterrows():
    result =  "{:.2f}".format(row['Implied Volatility'] - value)
    results.append(result)

# Add the results to the DataFrame as a new column
df['New_Column'] = results

# Display the updated DataFrame
df.to_csv(f"scrap.csv", index=False)