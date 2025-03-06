# Web-Scraping-using-RE

📖 Project Overview

This Python project scrapes contact details (names, phone numbers, and cities) from Contact List Pro and saves the extracted data into a CSV file.

🔧 Features

✅ Scrapes data from the given URL✅ Extracts phone numbers, city names, and contact names✅ Cleans and processes the extracted data✅ Stores the data in a pandas DataFrame✅ Saves the data as a CSV file (output_csv)

🛠️ Setup and Installation

Step 1: Install Required Libraries

Before running the script, ensure you have the required libraries installed:

pip install pandas

Step 2: Run the Python Script

python web_scrapping.py

Step 3: Check the Output

The extracted data will be printed in the terminal

A CSV file output_csv will be created with the extracted data

📜 Code Explanation

1️⃣ Importing Required Libraries

import re  # Regular expressions for text extraction
import urllib
import pandas as pd
from urllib.request import urlopen

re: Used for pattern matching and text extraction

urllib: Used to open and read the webpage

pandas: Used to store and save the extracted data in a CSV file

2️⃣ Fetching HTML Content from the URL

url = 'https://www.contactlistpro.com/contact-list/3-columns/'
data = urlopen(url)  # Open the webpage
data = data.read().decode()  # Read and decode HTML data

urlopen(url): Opens the webpage

.read().decode(): Reads the HTML and decodes it to a readable format

3️⃣ Cleaning the HTML Content

data = re.sub('/+?.<>
', '', data)  # Remove special characters
data = re.sub('>', ' ', data)
data = re.sub('<', ' ', data)  # Remove HTML tags

The goal is to clean the raw HTML and remove unnecessary symbols.

4️⃣ Extracting Contact Numbers

tel_number = re.findall('(tel:[0-9]{10})', data)  # Find phone numbers
tel_number = " ".join(tel_number)  # Convert to string
tel_numer = re.sub('tel:', '', tel_number)  # Remove 'tel:' prefix
tel_numer = tel_numer.split(' ')  # Convert back to a list
del(tel_numer[-2:])  # Remove unnecessary data
print(len(tel_numer), tel_numer)

Uses re.findall('(tel:[0-9]{10})', data) to extract 10-digit phone numbers prefixed with "tel:"

Cleans the numbers and removes unwanted elements

Converts them into a list

5️⃣ Extracting City Names

city = re.findall('[a-zA-Z]{1,20}[,]\s[a-zA-Z]{1,20}[,]\s[a-zA-Z]{1,20}', data)
print(len(city), city)

Uses regex to match city names in the format "City, State, Country"

Example: "Los Angeles, California, USA"

6️⃣ Extracting Contact Names

names = re.findall('[A-Z][a-z]{1,20}\s[A-Z][a-z]{1,20}\s/div', data)  # Find names
names = ''.join(names)
name = re.sub(' /div', '  ', names)  # Remove extra HTML parts
name = name.split('  ')  # Convert to list
del(name[-3:])  # Remove extra data
print(len(name), name)

Uses regex to extract full names (assumed to be "First Last")

Cleans and processes the extracted names

7️⃣ Storing Extracted Data in a Dictionary

dict1 = {'Name': name, "Contact": tel_numer, "City": city}

Creates a dictionary with extracted names, contacts, and cities

8️⃣ Creating a Pandas DataFrame

df = pd.DataFrame(dict1, columns=dict1.keys())  # Create DataFrame
print(df)

Converts the dictionary into a structured DataFrame

9️⃣ Saving Data to a CSV File

df.to_csv('output_csv', index=False)

Saves the scraped data into output_csv
