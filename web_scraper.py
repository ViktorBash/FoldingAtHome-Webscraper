"""
folding@home stats webscraper.
Uses requests-html library to load the Javascript to get the statistics.
Look at the bottom to see an example of how to use the code.
"""

from requests_html import HTMLSession


# Main webscraping method. Takes in URL of the statistics page
def webscrape(url):
    session = HTMLSession()

    # Start the session, run the javascript and get the HTML
    r = session.get(url)
    r.html.render()
    donor_info = r.html.find("#content", first=True)

    # Split the data into a list. Now every even index (0, 2, 4, ...) should contain a label while every odd index,
    # (1, 3, 5, ...) should contain the actual data. This will make it easy to work with the list.
    donor_info_list = donor_info.text.split("\n")

    # This turns the first item in the list from "Donor: <donor-name>" into two items, "Donor:" and "<donor-name">.
    # This is done to keep with the theme of every odd and every even index being a label or data.
    donor_info_list[0] = donor_info_list[0].split(" ")[1]
    donor_info_list.insert(0, "Donor")

    # End the session in case the script is run again
    session = None

    # Return the list
    return donor_info_list[0:14]


# Testing area
if __name__ == "__main__":
    # Example usage:
    data = webscrape("https://stats.foldingathome.org/donor/1437")
    print(data)

    import time

    for i in range(5):
        time.sleep(1)
        data = webscrape("https://stats.foldingathome.org/donor/1437")
        print(data)
