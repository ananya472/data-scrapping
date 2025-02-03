import os
import time
import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to get BSE Code and NSE Symbol for each company
def get_codes(company_name):
    bse_url = "https://www.bseindia.com/corporates/List_Scrips.html"
    nse_url = "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm"

    try:
        bse_response = requests.get(bse_url)
        bse_response.raise_for_status()  # Raise an error for bad responses
        bse_soup = BeautifulSoup(bse_response.text, 'html.parser')
        bse_code = "BSE12345"  # Simulated code for testing
    except requests.exceptions.RequestException as e:
        print(f"Error fetching BSE data for {company_name}: {e}")
        bse_code = None

    try:
        nse_response = requests.get(nse_url)
        nse_response.raise_for_status()  # Raise an error for bad responses
        nse_soup = BeautifulSoup(nse_response.text, 'html.parser')
        nse_symbol = "NSE12345"  # Simulated symbol for testing
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NSE data for {company_name}: {e}")
        nse_symbol = None
    
    return bse_code, nse_symbol

# Function to extract data from BSE (simulate actual data extraction)
def extract_bse_data(bse_code):
    # Simulated data files for testing
    bse_files = [f"BSE_File_{bse_code}_2023.pdf", f"BSE_File_{bse_code}_2024.pdf"]
    return bse_files

# Function to extract data from NSE (simulate actual data extraction)
def extract_nse_data(nse_symbol):
    # Simulated data files for testing
    nse_files = [f"NSE_File_{nse_symbol}_2023.pdf", f"NSE_File_{nse_symbol}_2024.pdf"]
    return nse_files

# Main script execution
if __name__ == "__main__":
    os.makedirs('BSE', exist_ok=True)

    # Read companies from the Excel file
    companies_df = pd.read_excel(r'C:\Users\anany\Desktop\data_scraping\companies.xlsx')
    print("Columns in DataFrame:", companies_df.columns)
    companies_df.columns = companies_df.columns.str.strip()

    if 'Name' not in companies_df.columns:
        raise KeyError("Column 'Name' not found in DataFrame.")

    # Get BSE and NSE codes for each company
    companies_df[['BSE_Code', 'NSE_Symbol']] = companies_df['Name'].apply(get_codes).apply(pd.Series)

    # Initialize an empty list for log entries
    log_entries = []

    # Process each company
    for index, row in companies_df.iterrows():
        print(f"Processing {row['Name']}...")

        # Extract data from BSE if BSE Code is available
        if row['BSE_Code']:
            bse_files = extract_bse_data(row['BSE_Code'])  # Call BSE extraction function
            for file in bse_files:
                log_entries.append({
                    'Company': row['Name'],
                    'BSE_Code': row['BSE_Code'],
                    'File_Name': file,
                    'Download_Date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'Source': 'BSE'
                })

        # Extract data from NSE if NSE Symbol is available
        if row['NSE_Symbol']:
            nse_files = extract_nse_data(row['NSE_Symbol'])  # Call NSE extraction function
            for file in nse_files:
                log_entries.append({
                    'Company': row['Name'],
                    'NSE_Symbol': row['NSE_Symbol'],
                    'File_Name': file,
                    'Download_Date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'Source': 'NSE'
                })

        # Pause to avoid overwhelming the servers (to avoid IP blocking)
        time.sleep(5)

    # Create a DataFrame from log entries
    log_df = pd.DataFrame(log_entries)

    # Save the log DataFrame to a CSV file
    log_df.to_csv('download_log.csv', index=False)

    print("Log file 'download_log.csv' has been created.")
