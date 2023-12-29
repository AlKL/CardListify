import csv
import os
from pprint import pprint
from ebaysdk.exception import ConnectionError
from ebaysdk.merchandising import Connection as Merchandising
from ebaysdk.trading import Connection as Trading

api = Trading(config_file="ebay.yaml", domain="api.ebay.com", warnings=False)

# #################################
# # Set your desired file name here
filename = 'ashura.csv'
# #################################

# # Construct the full file path
spreadsheetPath = './spreadsheets'
spreadsheetName = os.path.join(spreadsheetPath, filename)

# # Open the CSV file using the variable
with open(spreadsheetName, newline='') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)

    # Skip the header row
    header = next(csv_reader)

    # Iterate through each row of the CSV file
    for row in csv_reader:
        # Assign each column's data to a variable
        card_name, img_path, condition, rarity, edition, price, quantity, card_set, set_abbrv = row

        # Print the variables for each row
        print(f"card_name: {card_name}, img_path: {img_path}, condition: {condition}, rarity: {rarity}, edition: {edition}, price: {price}, quantity: {quantity}, card_set: {card_set}, set_abbrv: {set_abbrv}")

        try:
            # Upload image
            pictureData = {
                "WarningLevel": "High",
                "PictureName": card_name + " Picture"
            }

            filepath = "images/" + img_path
            files = {'file': ('EbayImage', open(filepath, 'rb'))}
            img_response = api.execute('UploadSiteHostedPictures', pictureData, files=files)
            response_dict = img_response.dict()
            # pprint(img_response.dict())
            imgUrl = response_dict['SiteHostedPictureDetails']['FullURL']
            # pprint(imgUrl)

            myitem = {
                    "Item": {
                        "Title": f"{card_name} - {condition} - {rarity}{' ' + edition if edition != 'Unlimited' else ''} - {set_abbrv} - YuGiOh",
                        "Description": "Shipped quickly within 24 hours and shipped safely with a top loader. Feel free to ask any questions!",
                        'PrimaryCategory': { 'CategoryID': '183454' },
                        "StartPrice": price,
                        "CategoryMappingAllowed": "true",
                        "Country": "CA",
                        "ConditionDescriptors": {
                            "ConditionDescriptor": {
                                'Name': '40001',
                                'Value': '400010'
                            }
                        },
                        "ConditionID": "4000",
                        "Currency": "CAD",
                        "DispatchTimeMax": "2",
                        "ListingDuration": "GTC",
                        "ListingType": "FixedPriceItem",
                        'Quantity': quantity,
                        'ReturnPolicy': {
                            'InternationalReturnsAcceptedOption': 'ReturnsNotAccepted',
                            'ReturnsAccepted': 'Returns Not Accepted',
                            'ReturnsAcceptedOption': 'ReturnsNotAccepted'
                        },
                        "ShippingDetails": [
                        {
                            "ShippingServiceOptions": {
                                "FreeShipping": "true",
                                "ShippingService": "CA_PostLettermail",
                                "ShippingServiceCost": "0"
                            }
                        }],
                        "PictureDetails": {"PictureURL": imgUrl}, # frontpic PLACEHOLDER
                        "PostalCode": "M3N2B1",
                        "ItemSpecifics": {
                            "NameValueList": [
                                {'Name': 'Game', 'Value': 'Yu-Gi-Oh! TCG'},
                                {'Name': 'Rarity', 'Value': rarity },
                                {'Name': 'Card Size', 'Value': 'Standard'},
                                {'Name': 'Set', 'Value': card_set},
                                {'Name': 'Features', 'Value': edition },
                                {'Name': 'Manufacturer', 'Value': 'Konami'},
                                {'Name': 'Material', 'Value': 'Card Stock'},
                                {'Name': 'Age Level', 'Value': '6+'},
                            ]
                        }
                    }
                }
            # theirItem = "<ItemID>225754961118</ItemID>"
            # response = api.execute("GetItem", theirItem)

            response = api.execute("AddItem", myitem)
            pprint(response.dict())
        except ConnectionError as e:
            print("Error:", e)
