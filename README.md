# CardListify
Run with
python3 ./src/app.py

Features:
- SEO
- Promote some listings
- Update listings
- Connect to sqlite to automatically manage inventory, check profits and losses over a year
- When a card has sold, remove that from the inventory db and record profits

Steps
1. Read a CSV
2. Columns should include everything required by eBay to list
3. Ignore 1st row for columns
4. Itr through the rest of the file
5. Separate columns required into variables
6. Call the addItem/addItems API with the variables passed as parameters

Todo:
-