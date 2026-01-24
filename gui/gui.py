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
GUI_DATA_FILE_EXTENSION = '.json'

GUI_DATA_FILE_KEY_SPECIES = 'species'
GUI_DATA_FILE_KEY_LATIN_NAME = 'latinName'
GUI_DATA_FILE_KEY_COMMON_NAME = 'commonName'
GUI_DATA_FILE_KEY_EDIBILITY = 'edibility'
GUI_DATA_FILE_KEY_REF_DELACHAUX_FLEURS = 'refDelachauxFleurs'
GUI_DATA_FILE_KEY_REF_700_PLANTES = 'ref700Plantes'
GUI_DATA_FILE_KEY_REF_FLORE_PYRENEES = 'refFlorePyrenees'
GUI_DATA_FILE_KEY_REF_DELACHAUX_ARBRES = 'refDelachauxArbres'
GUI_DATA_FILE_KEY_REF_CHAMPIGNONS = 'refChampignons'

GUI_CLASSIFICATION_SPECIES_COLUMN = 6

### GUI local global variables ###

botany_guide_gui = None
species_directory_path = ""

### GUI functions ###

"""
parseSpeciesJsonFile
    Parse a species JSON file and print the content on the GUI.
"""
def parseSpeciesJsonFile(species_json_file):
    # Global variables.
    global botany_guide_gui
    # Parse JSON file.
    try:
        species_json = json.load(species_json_file)
    except:
        print("* ERROR * Species JSON file decoding failed")
        return (-1)
    # Check top level key.
    if GUI_DATA_FILE_KEY_SPECIES not in species_json:
        print("* ERROR * Species JSON file top level key not found")
        return (-2)
    # Get items.
    species_data = species_json[GUI_DATA_FILE_KEY_SPECIES]
    print("* INFO ** JSON data: " + json.dumps(species_data, indent=4))
    # Latin name.
    raw = species_data[GUI_DATA_FILE_KEY_LATIN_NAME] if (GUI_DATA_FILE_KEY_LATIN_NAME in species_data) else ""
    text = str(raw) if (isinstance(raw, int)) else raw
    botany_guide_gui.speciesLatinNameContentLabel.setText(text)
    # Common name.
    raw = species_data[GUI_DATA_FILE_KEY_COMMON_NAME] if (GUI_DATA_FILE_KEY_COMMON_NAME in species_data) else ""
    text = str(raw) if (isinstance(raw, int)) else raw
    botany_guide_gui.speciesCommonNameContentLabel.setText(text)
    # Edibility.
    raw = species_data[GUI_DATA_FILE_KEY_EDIBILITY] if (GUI_DATA_FILE_KEY_EDIBILITY in species_data) else ""
    text = str(raw) if (isinstance(raw, int)) else raw
    botany_guide_gui.speciesEdibilityContentLabel.setText(text)
    # Reference Delachaux Fleurs.
    raw = species_data[GUI_DATA_FILE_KEY_REF_DELACHAUX_FLEURS] if (GUI_DATA_FILE_KEY_REF_DELACHAUX_FLEURS in species_data) else ""
    text = ("p. " + str(raw)) if (isinstance(raw, int)) else raw
    botany_guide_gui.speciesRefDelachauxFleursContentLabel.setText(text)
    # Reference Guide 700 Plantes.
    raw = species_data[GUI_DATA_FILE_KEY_REF_700_PLANTES] if (GUI_DATA_FILE_KEY_REF_700_PLANTES in species_data) else ""
    text = ("p. " + str(raw)) if (isinstance(raw, int)) else raw
    botany_guide_gui.speciesRefGuide700PlantesContentLabel.setText(text)
    # Reference Flore Pyrenees.
    raw = species_data[GUI_DATA_FILE_KEY_REF_FLORE_PYRENEES] if (GUI_DATA_FILE_KEY_REF_FLORE_PYRENEES in species_data) else ""
    text = ("p. " + str(raw)) if (isinstance(raw, int)) else raw
    botany_guide_gui.speciesRefFlorePyreneesContentLabel.setText(text)
    # Reference Delachaux Arbres.
    raw = species_data[GUI_DATA_FILE_KEY_REF_DELACHAUX_ARBRES] if (GUI_DATA_FILE_KEY_REF_DELACHAUX_ARBRES in species_data) else ""
    text = ("p. " + str(raw)) if (isinstance(raw, int)) else raw
    botany_guide_gui.speciesRefDelachauxArbresContentLabel.setText(text)
    # Reference Champignons
    raw = species_data[GUI_DATA_FILE_KEY_REF_CHAMPIGNONS] if (GUI_DATA_FILE_KEY_REF_CHAMPIGNONS in species_data) else ""
    text = ("p. " + str(raw)) if (isinstance(raw, int)) else raw
    botany_guide_gui.speciesRefChampignonsContentLabel.setText(text)
    return 0

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
            # Check if there is JSON file.
            if (Path(species_file).suffix == GUI_DATA_FILE_EXTENSION):
                print("* INFO ** JSON file found: " + str(species_file))
                try:
                    with open(os.path.join(species_directory_path, species_file), 'r') as species_json_file:
                        if (parseSpeciesJsonFile(species_json_file) == 0):
                            return
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
    botany_guide_gui = BotanyGuideGui()
    botany_guide_gui.show()
    # Start application.
    sys.exit(app.exec())
    