"""
* classification.py
*
*  Created on: 26 jan. 2026
*      Author: Ludo
"""

import os
import array

from pathlib import Path
from PySide6.QtWidgets import QTreeWidgetItem, QHeaderView

from gui.species import Species, SpeciesEditWindow, SpeciesView

### CLASSIFICATION macros ###   

CLASSIFICATION_SPECIES_COLUMN = 6
CLASSIFICATION_DEPTH_MAX = 8

### CLASSIFICATION class definition ###
        
class ClassificationView:
    
    def __init__(self, gui: object, data_directory_path: str) -> None:
        # Init context.
        self._gui = gui
        self._current_species = None
        self._current_species_directory = os.getcwd()
        self._data_directory_path = data_directory_path
        # Setup tree view.
        self._gui.classificationTreeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self._gui.classificationTreeWidget.itemClicked.connect(self._item_clicked_callback)
        self._gui.classificationAddSpeciesPushButton.clicked.connect(self._add_species_callback)
        self._gui.classificationRefreshPushButton.clicked.connect(self._refresh_callback)
        # Init GUI.
        SpeciesView.clear(self._gui)
        self._refresh_callback()

    def _refresh_callback(self) -> None:
        # Local variables.
        header = []
        item_count = array.array('I', (0 for i in range(0, CLASSIFICATION_DEPTH_MAX)))
        data_directory_depth = len(Path(os.path.join(self._data_directory_path)).parents)
        # Reset tree.
        self._gui.classificationTreeWidget.clear()
        # Read all data folder.
        for root, _, _ in sorted(os.walk(self._data_directory_path)):
            # Compute directory depth.
            depth = (len(Path(os.path.join(root)).parents) - data_directory_depth)
            if ((depth > 0) and (depth < CLASSIFICATION_DEPTH_MAX)):
                # Convert folder name in pretty format.
                pretty_name = str(os.path.basename(root).title()).replace("_", " ")
                # Add item.
                item = QTreeWidgetItem(self._gui.classificationTreeWidget)
                item.setText((depth - 1), pretty_name)
                item.setWhatsThis((depth - 1), os.path.join(root))
                # Update item count.
                item_count[depth] += 1
        # Set header.
        header.append("Règne ("    + str(item_count[1]) + ")")
        header.append("Division (" + str(item_count[2]) + ")")
        header.append("Classe ("   + str(item_count[3]) + ")")
        header.append("Ordre ("    + str(item_count[4]) + ")")
        header.append("Famille ("  + str(item_count[5]) + ")")
        header.append("Genre ("    + str(item_count[6]) + ")")
        header.append("Espèce ("   + str(item_count[7]) + ")")
        self._gui.classificationTreeWidget.setHeaderLabels(header)
        
    def _item_clicked_callback(self, item, column) -> None:
        # Unused variable.
        _ = column
        # Check if a species has been clicked.
        if (item.text(CLASSIFICATION_SPECIES_COLUMN)):
            # Try creating species object.
            try:
                self._current_species_directory = item.whatsThis(CLASSIFICATION_SPECIES_COLUMN)
                self._current_species = SpeciesView(self._gui, self._current_species_directory)
                self._current_species.display()
            except Exception as e:
                raise ValueError(f"Species object creation failed: {e}")

    def _add_species_callback(self) -> None:
        # Create static object.
        new_species = Species()
        # Open new window.
        new_window = SpeciesEditWindow(new_species, True, self._current_species_directory)
        new_window.exec()
        # Check if any property has been modified.
        if (new_window._has_changed == True):
            # Create species object.
            new_species_view = SpeciesView(self._gui, new_species.creation_directory_path, new_species)
            _ = new_species_view
            # Refresh GUI.
            self._refresh_callback()
        new_window.close()
            