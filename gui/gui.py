"""
* gui.py
*
*  Created on: 21 dec. 2025
*      Author: Ludo
"""

import os
import sys
import json

from os import listdir
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QHeaderView
from main_window_ui import Ui_MainWindow

### GUI macros ###

GUI_DATA_PATH = './data'
GUI_CLASSIFICATION_SPECIES_COLUMN = 6
GUI_SPECIES_FILE_EXTENSION = '.json'

### GUI local global variables ###

species_directory_path = ""

### GUI functions ###

"""
classificationItemClicked
    Function called when a species is clicked on the classification panel.
    The whatsThis property of the item contains the path to the species.
"""
def classificationItemClicked(item, column):
    # Global variables.
    global species_directory_path
    # Check if a species has been clicked.
    if (item.text(GUI_CLASSIFICATION_SPECIES_COLUMN)):
        # Read path.
        species_directory_path = item.whatsThis(GUI_CLASSIFICATION_SPECIES_COLUMN)
        print("* INFO ** Species clicked callback: " + item.text(GUI_CLASSIFICATION_SPECIES_COLUMN) + " (" + species_directory_path + ")")
        # Read directory.
        for species_file in listdir(species_directory_path):
            # Check if there is JSON file.)
            if (Path(species_file).suffix == GUI_SPECIES_FILE_EXTENSION):
                print("* INFO ** JSON file found: " + str(species_file))
                try:
                    with open(os.path.join(species_directory_path, species_file), 'r') as species_json_file:
                        species_data = json.load(species_json_file)  
                        print(json.dumps(species_data, indent=4))
                except:
                    print("* ERROR * Species JSON file opening failed")

### GUI class definition ###   
        
"""
BotanyGuideGui
    Main GUI class definition.
"""
class BotanyGuideGui(QMainWindow, Ui_MainWindow):
    # Constructor.
    def __init__(self):
        # Init parent.
        super().__init__()
        # Window properties.
        self.setupUi(self)
        self.setWindowTitle("Botany Guide GUI")
        # Setup tree view.
        self.classificationTreeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Read all data folder.
        for root, _, _ in os.walk(GUI_DATA_PATH):
            # Compute directory depth.
            depth = (len(Path(os.path.join(root)).parents) - 1)
            if ((depth > 0) and (depth < 8)):
                # Convert folder name in pretty format.
                pretty_name = str(os.path.basename(root).title()).replace("_", " ")
                # Add item.
                item = QTreeWidgetItem(self.classificationTreeWidget)
                item.setText((depth - 1), pretty_name)
                item.setWhatsThis((depth - 1), os.path.join(root))
        # Signals and slot.
        self.classificationTreeWidget.itemClicked.connect(classificationItemClicked)
            
### GUI main function ###

if __name__ == "__main__":
    # Create application.
    app = QApplication(sys.argv)
    # Instantiate and show window.
    botanyGuideGui = BotanyGuideGui()
    botanyGuideGui.show()
    # Start application.
    sys.exit(app.exec())
    