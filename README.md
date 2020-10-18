# Folding@Home Webscraper
This is a python webscraper for folding@home's statistics page.

### Requirements:
This script uses the ```requests-html``` library.

Run ```pip install requests-html``` to get the library.

### Example Usage:
Look at ```example.py``` for an example on how to use this script.

For instance:
```
from web_scraper import webscrape
data = webscrape("https://stats.foldingathome.org/donor/1437")
print(data)
```
Data is a dictionary that contains the donor's name, date of last work unit, score, rank, active clients within 50 days and active clients within 7 days
