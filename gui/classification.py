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

from .species import Species

### CLASSIFICATION macros ###   

CLASSIFICATION_SPECIES_COLUMN = 6
CLASSIFICATION_DEPTH_MAX = 8

### CLASSIFICATION class definition ###   
        
class Classification:
    
    def __init__(self, gui: object, data_directory_path: str) -> None:
        # Local variables.
        item_count = array.array('I', (0 for i in range(0, CLASSIFICATION_DEPTH_MAX)))
        header = []
        # Init context.
        self._gui = gui
        self._current_species = None
        # Setup tree view.
        self._gui.classificationTreeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Read all data folder.
        for root, _, _ in os.walk(data_directory_path):
            # Compute directory depth.
            depth = (len(Path(os.path.join(root)).parents) - 1)
            if ((depth > 0) and (depth < CLASSIFICATION_DEPTH_MAX)):
                # Convert folder name in pretty format.
                pretty_name = str(os.path.basename(root).title()).replace("_", " ")
                # Add item.
                item = QTreeWidgetItem(gui.classificationTreeWidget)
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
        # Signals and slot.
        self._gui.classificationTreeWidget.itemClicked.connect(self._item_clicked_callback)
        
    def _item_clicked_callback(self, item, column):
        # Unused variable.
        _ = column
        # Check if a species has been clicked.
        if (item.text(CLASSIFICATION_SPECIES_COLUMN)):
            # Try creating species object.
            try:
                self._current_species = Species(self._gui, item.whatsThis(CLASSIFICATION_SPECIES_COLUMN))
                self._current_species.display()
            except Exception as e:
                raise ValueError(f"Species object creation failed: {e}")
            