# data-scrapping

Overview

This script extracts company data from the Bombay Stock Exchange (BSE) and National Stock Exchange (NSE) using web scraping and stores the downloaded file information in a log file.

Setup & Installation

Prerequisites

Ensure you have Python installed on your system. You can download and install Python from python.org.

Dependencies

Install the required Python libraries by running: 

pip install pandas requests beautifulsoup4 openpyxl

Usage

Prepare the company list:

Ensure companies.xlsx is in the same directory as the script.

The Excel file should contain a column named Name with company names.

Run the script:

python main.py

Check the log file:

After execution, a file named download_log.csv will be created, containing details of the extracted data.


Output

The download_log.csv file will have the following columns:

Company - Name of the company

BSE_Code - Extracted BSE Code

NSE_Symbol - Extracted NSE Symbol

File_Name - Name of the downloaded file (if applicable)

Download_Date - Timestamp of the extraction

Source - Indicates whether the data is from BSE or NSE
