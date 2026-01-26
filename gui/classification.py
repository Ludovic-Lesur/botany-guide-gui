"""
* classification.py
*
*  Created on: 26 jan. 2026
*      Author: Ludo
"""

import os

from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QHeaderView

from .species import Species

### CLASSIFICATION macros ###   

GUI_CLASSIFICATION_SPECIES_COLUMN = 6

### CLASSIFICATION class definition ###   
        
class Classification:
    
    def __init__(self, gui: QMainWindow, data_directory_path: str) -> None:
        # Store GUI object.
        self._gui = gui
        # Setup tree view.
        gui.classificationTreeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Read all data folder.
        for root, _, _ in os.walk(data_directory_path):
            # Compute directory depth.
            depth = (len(Path(os.path.join(root)).parents) - 1)
            if ((depth > 0) and (depth < 8)):
                # Convert folder name in pretty format.
                pretty_name = str(os.path.basename(root).title()).replace("_", " ")
                # Add item.
                item = QTreeWidgetItem(gui.classificationTreeWidget)
                item.setText((depth - 1), pretty_name)
                item.setWhatsThis((depth - 1), os.path.join(root))
        # Signals and slot.
        gui.classificationTreeWidget.itemClicked.connect(self._item_clicked)
        
    def _item_clicked(self, item, column):
        # Unused variable.
        _ = column
        # Check if a species has been clicked.
        if (item.text(GUI_CLASSIFICATION_SPECIES_COLUMN)):
            # Try creating species object.
            try:
                species = Species(item.whatsThis(GUI_CLASSIFICATION_SPECIES_COLUMN))
                species.display(self._gui)
            except Exception as e:
                raise ValueError(f"Species object creation failed: {e}")
            