import csv
from ebaysdk.merchandising import Connection

# Read a given csv
# api = Connection(config_file='ebay.yaml')
# most_watched = api.execute('getMostWatchedItems', {})
# most_watched

import csv
import os

#################################
# Set your desired file name here
filename = 'ashura.csv'
#################################

# Construct the full file path
spreadsheetPath = './spreadsheets'
spreadsheetName = os.path.join(spreadsheetPath, filename)

# Open the CSV file using the variable
with open(spreadsheetName, newline='') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)

    # Skip the header row
    header = next(csv_reader)

    # Iterate through each row of the CSV file
    for row in csv_reader:
        # Assign each column's data to a variable
        col1, col2, col3, col4 = row

        # Print the variables for each row
        print(f"Column 1: {col1}, Column 2: {col2}, Column 3: {col3}, Column 4: {col4}")
