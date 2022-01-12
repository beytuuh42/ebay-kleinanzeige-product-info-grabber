# Product info grabber for ebay-kleinanzeige

## Description
This is for purposes of re-instating items for sale.
It grabs the title, photos, price and descprition of a listed item and saves them in a folder named after the respective listed item title. All items are saved in a folder named _products_, which is created at the location of the python-file.
The photos are numered starting from _0_ as _.jpgs_ and there is a textfile _description.txt_, with the info in it.

## How-to
Put each URL of a listed item in a seperate line in _links.txt_ textfile, as shown in the file iteself.
Install the required packages by running the command `pip3 install -r requirements.txt` and run the script with the command `python main.py`.