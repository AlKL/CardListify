import csv
import os
from pprint import pprint
from ebaysdk.exception import ConnectionError
from ebaysdk.merchandising import Connection as Merchandising
from ebaysdk.trading import Connection as Trading

# example
# try:
    # myitem = {'maxResults': 10}         # here I have the dict converted from XML
    # api = Merchandising(appid="Alexandr-CardList-PRD-4a11a70e7-208fecc8")
    # response = api.execute("getMostWatchedItems", myitem)               # VerifyAddItem same problem as AddItem
    # pprint(response.dict())

try:
    myitem = {}
    api = Trading(config_file="ebay.yaml", domain="api.sandbox.ebay.com")
    response = api.execute("VerifyAddItem", myitem)
    pprint(response.dict())
except ConnectionError as e:
    print("Error:", e)

# #################################
# # Set your desired file name here
# filename = 'ashura.csv'
# #################################

# # Construct the full file path
# spreadsheetPath = './spreadsheets'
# spreadsheetName = os.path.join(spreadsheetPath, filename)

# # Open the CSV file using the variable
# with open(spreadsheetName, newline='') as csvfile:
#     # Create a CSV reader object
#     csv_reader = csv.reader(csvfile)

#     # Skip the header row
#     header = next(csv_reader)

#     # Iterate through each row of the CSV file
#     for row in csv_reader:
#         # Assign each column's data to a variable
#         col1, col2, col3, col4 = row

#         # Print the variables for each row
#         print(f"Column 1: {col1}, Column 2: {col2}, Column 3: {col3}, Column 4: {col4}")

