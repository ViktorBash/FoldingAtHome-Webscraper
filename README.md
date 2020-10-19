# Folding@Home GUI Webscraper
This is a Python webscraper for folding@home's statistics page. You can
use just the webscraper or the GUI to get data from your folding@home's statistics page.

### Requirements:
This script uses the ```requests-html``` and ```PyQt5``` libraries.

Run:
 ```pip install requests-html``` and
 ```pip install PyQt5```
 to get the libraries.

### GUI Example Usage:
Go into ```gui.py``` and change the ```statistics_link``` variable on line 15 to your folding@home statistics page. Now the GUI should display your statistics and update every 5 minutes.

**Optional:**
If you want to change the refresh rate of the program you can change 
```UPDATE_TIME_MIN``` on line 12
to any time that you want in minutes. 

### Webscraper Example Usage:
If you wish you can also just use the webscraper from the project instead of the GUI.
Look at ```example.py``` for an example on how to use the webscraper.

For instance:
```
from web_scraper import webscrape
data = webscrape("https://stats.foldingathome.org/donor/1437")
print(data)
```
The data is a list variable that contains information from the statistics page,
such as the donor's name, date of last work unit, total score, total WUs,
overall rank, active clients within 50 days and active clients within 7 days.