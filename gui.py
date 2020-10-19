import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from web_scraper import webscrape
from PyQt5.QtCore import QTimer


# Main class for the GUI
class MainGUI(QWidget):
    data = None
    # Default is 5 (meaning the GUI will update every 5 minutes). Choose whatever number you want
    UPDATE_TIME_MIN = 5
    statistics_link = "https://stats.foldingathome.org/donor/1437"

    # Initialize and set settings
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folding@home Statistics")

        # Set central widget and layout
        self.generalLayout = QGridLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.generalLayout)

        # Get and display data
        self.get_data()
        self.display_data()

        # Size of window is set to fit the size of the widgets
        self.setMinimumSize(self.generalLayout.sizeHint())

        # Create a QTimer to periodically update the data
        self.qTimer = QTimer()
        self.qTimer.setInterval(self.UPDATE_TIME_MIN*60*1000)
        self.qTimer.timeout.connect(self.update_data)
        self.qTimer.start()

    # Get data from webscraper function as a list
    def get_data(self):
        self.data = webscrape(self.statistics_link)

    # Loop through data list and add to the window as label widgets
    def display_data(self):
        for i in range(0, len(self.data)-1, 2):
            self.label = QLabel(f"{self.data[i]}: {self.data[i+1]}")
            self.label.setFixedHeight(25)
            self.generalLayout.addWidget(self.label, int(i/2), 0)

    # Delete all the widgets, get new data, display the new data and print to terminal when done.
    def update_data(self):
        for i in reversed(range(self.generalLayout.count())):
            self.generalLayout.itemAt(i).widget().setParent(None)
        self.get_data()
        self.display_data()
        print("Data updated")


# Function to run and display the GUI
def main():
    stat_gui = QApplication(sys.argv)
    view = MainGUI()
    view.show()
    sys.exit(stat_gui.exec_())


if __name__ == "__main__":
    main()
