# GetSuggestedCategories
myQuery = "<Query>Ashura King - Near Mint - Secret Rare 1st Edition - YuGiOh</Query>"
api = Trading(config_file="ebay.yaml", domain="api.ebay.com", warnings=False)
response = api.execute("GetSuggestedCategories", myQuery)
pprint(response.dict())

# GetSellerList
response = items = api.execute('GetSellerList', {
    'StartTimeFrom': "2023-11-30T00:00:00",
    'StartTimeTo': "2024-01-01T00:00:00",
    "Pagination": {
        "EntriesPerPage":
            100,
        "PageNumber": 1
    },
        'DetailLevel': 'ReturnAll'
    }
)
pprint(response.dict())

# Image upload response from UploadSiteHostedPictures

{'Ack': 'Success',
 'Build': 'mediasvcs-5.0.29_20231208001455673',
 'PictureSystemVersion': '2',
 'SiteHostedPictureDetails': {'BaseURL': 'https://i.ebayimg.com/00/s/MTMzOFg5NzA=/z/XV4AAOSwT4lljfl6/$_',
                              'FullURL': 'https://i.ebayimg.com/00/s/MTMzOFg5NzA=/z/XV4AAOSwT4lljfl6/$_1.PNG?set_id=2',
                              'PictureFormat': 'PNG',
                              'PictureName': 'Card game',
                              'PictureSet': 'Standard',
                              'PictureSetMember': [{'MemberURL': 'https://i.ebayimg.com/00/s/MTMzOFg5NzA=/z/XV4AAOSwT4lljfl6/$_1.PNG',
                                                    'PictureHeight': '400',
                                                    'PictureWidth': '289'}],
                              'UseByDate': '2024-01-27T22:40:57.026Z'},
 'Timestamp': '2023-12-28T22:40:58.727Z',
 'Version': '0'}