"""
* species.py
*
*  Created on: 25 jan. 2026
*      Author: Ludo & Copilot
"""

import json
import logging
import os

from pathlib import Path
from typing import Any

from gui.identification import Identification
from gui.image import Image

### SPECIES macros ###

SPECIES_DATA_FILE_EXTENSION = '.json'

SPECIES_JSON_KEY_TOP_LEVEL = 'species'

SPECIES_JSON_KEY_LATIN_NAME = 'latinName'
SPECIES_JSON_KEY_COMMON_NAME = 'commonName'
SPECIES_JSON_KEY_EDIBILITY = 'edibility'
SPECIES_JSON_KEY_REF_DELACHAUX_FLEURS = 'refDelachauxFleurs'
SPECIES_JSON_KEY_REF_700_PLANTES = 'ref700Plantes'
SPECIES_JSON_KEY_REF_FLORE_PYRENEES = 'refFlorePyrenees'
SPECIES_JSON_KEY_REF_DELACHAUX_ARBRES = 'refDelachauxArbres'
SPECIES_JSON_KEY_REF_CHAMPIGNONS = 'refChampignons'

SPECIES_JSON_KEY_REQUIRED = [
    SPECIES_JSON_KEY_LATIN_NAME,
    SPECIES_JSON_KEY_COMMON_NAME
]

### SPECIES class ###

class Species:
    
    def __init__(self, gui: object, species_directory_path: str) -> None:
        # Local variables.
        json_decoded = False
        image_found = False
        # Init context.
        self._gui = gui
        self._identification_list = []
        self._current_identification_index = 0
        self._latin_name = ""
        self._common_name = ""
        self._image_path = None
        self._edibility = ""
        self._ref_delachaux_fleurs = ""
        self._ref_700_plantes = ""
        self._ref_flore_pyrenees = ""
        self._ref_delachaux_arbres = ""
        self._ref_champignons = ""
        # Read directory.
        for f in os.listdir(species_directory_path):
            # Build complete path.
            p = os.path.join(species_directory_path, f)
            # Check if there is JSON file.
            if ((Path(f).suffix.lower() == SPECIES_DATA_FILE_EXTENSION) and (json_decoded == False)):
                # Try parsing JSON file.
                try:
                    self._parse_json(p)
                    json_decoded = True
                except Exception as e:
                    logging.error("Invalid JSON file : %s", e)
            # Check if there a photo.
            if ((Path(f).suffix.lower() == Image.IMAGE_FILE_EXTENSION) and (image_found == False)):
                self._image_path = p
                image_found = True
            # Check identifications sub-directories.
            if (os.path.isdir(p)):
                try:
                    identification = Identification(self._gui, p)
                    self._identification_list.append(identification)
                except Exception as e:
                    logging.error("Invalid species sub-directory : %s", e)
        # Warn if image has not been found.
        if (image_found == False):
            logging.warning("No species image found")
        # Check if directory content is valid.
        if (json_decoded == False):
            raise ValueError("Invalid species directory")
        
    @staticmethod
    def _to_text(value: Any, prefix_page: bool = False) -> str:
        # Check none input.
        if value is None:
            return ""
        # Specific format for page.
        if isinstance(value, int) and prefix_page:
            return f"p. {value}"
        # Convert to string by default.
        return str(value)

    def _parse_json(self, species_json_path: str) -> None:
        # Open JSON file.
        try:
            with open(species_json_path, 'r') as json_file:
                data = json.load(json_file)
        except Exception as e:
            raise ValueError(f"Species JSON file decoding failed: {e}")
        # Check top level key.
        if SPECIES_JSON_KEY_TOP_LEVEL not in data:
            raise ValueError("Species JSON file top level key not found")
        # Extract data.
        species_mapping = data[SPECIES_JSON_KEY_TOP_LEVEL]
        # Check type.
        if not isinstance(species_mapping, dict):
            raise ValueError("Invalid species content: expected an object")
        # Check mandatory keys.
        missing_keys = [k for k in SPECIES_JSON_KEY_REQUIRED if k not in species_mapping]
        if missing_keys:
            raise ValueError(f"Missing required species keys: {', '.join(missing_keys)}")
        # Update context.
        self._latin_name = self._to_text(species_mapping.get(SPECIES_JSON_KEY_LATIN_NAME))
        self._common_name = self._to_text(species_mapping.get(SPECIES_JSON_KEY_COMMON_NAME))
        self._edibility = self._to_text(species_mapping.get(SPECIES_JSON_KEY_EDIBILITY))
        self._ref_delachaux_fleurs = self._to_text(species_mapping.get(SPECIES_JSON_KEY_REF_DELACHAUX_FLEURS), prefix_page=True)
        self._ref_700_plantes = self._to_text(species_mapping.get(SPECIES_JSON_KEY_REF_700_PLANTES), prefix_page=True)
        self._ref_flore_pyrenees = self._to_text(species_mapping.get(SPECIES_JSON_KEY_REF_FLORE_PYRENEES), prefix_page=True)
        self._ref_delachaux_arbres = self._to_text(species_mapping.get(SPECIES_JSON_KEY_REF_DELACHAUX_ARBRES), prefix_page=True)
        self._ref_champignons = self._to_text(species_mapping.get(SPECIES_JSON_KEY_REF_CHAMPIGNONS), prefix_page=True)

    def _display_identification(self):
        # Local variables.
        identification_count = len(self._identification_list)
        # Check count.
        if (identification_count == 0):
            # Clear identification panel.
            Identification.clear(self._gui)
            self._gui.identificationListPreviousPushButton.setEnabled(False)
            self._gui.identificationListNextPushButton.setEnabled(False)
            # Update title.
            self._gui.identificationListGroupBox.setTitle("Liste (0)")
        else:
            # Check index.
            if (self._current_identification_index >= identification_count):
                logging.warning("Identification index overflow, defaulting to last")
                self._current_identification_index = (identification_count - 1)
            # Print identification.
            self._identification_list[self._current_identification_index].display()
            # Update buttons state.
            self._gui.identificationListPreviousPushButton.setEnabled(True if (self._current_identification_index > 0) else False)
            self._gui.identificationListNextPushButton.setEnabled(True if (self._current_identification_index < (identification_count - 1)) else False)
            # Update title.
            self._gui.identificationListGroupBox.setTitle("Liste (" + str(self._current_identification_index + 1) + "/" + str(identification_count) + ")")

    def _previous_identification_callback(self):
        # Check index.
        if (self._current_identification_index > 0):
            # Print previous item.
            self._current_identification_index -= 1
            self._display_identification()

    def _next_identification_callback(self):
        # Check index.
        if (self._current_identification_index < (len(self._identification_list) - 1)):
            # Print previous item.
            self._current_identification_index += 1
            self._display_identification()

    def display(self) -> None:
        # Print fields.
        self._gui.speciesLatinNameContentLabel.setText(self._latin_name)
        self._gui.speciesCommonNameContentLabel.setText(self._common_name)
        self._gui.speciesEdibilityContentLabel.setText(self._edibility)
        self._gui.speciesRefDelachauxFleursContentLabel.setText(self._ref_delachaux_fleurs)
        self._gui.speciesRefGuide700PlantesContentLabel.setText(self._ref_700_plantes)
        self._gui.speciesRefFlorePyreneesContentLabel.setText(self._ref_flore_pyrenees)
        self._gui.speciesRefDelachauxArbresContentLabel.setText(self._ref_delachaux_arbres)
        self._gui.speciesRefChampignonsContentLabel.setText(self._ref_champignons)
        # Update image.
        Image.display(self._gui.speciesPhotoGraphicsView, self._image_path)
        # Update button callbacks.
        self._gui.identificationListPreviousPushButton.clicked.connect(self._previous_identification_callback)
        self._gui.identificationListNextPushButton.clicked.connect(self._next_identification_callback)
        # Print first identification.
        self._current_identification_index = 0
        self._display_identification()

    @staticmethod
    def clear(gui: object) -> None:
        # Clear all fields.
        gui.speciesLatinNameContentLabel.setText("")
        gui.speciesCommonNameContentLabel.setText("")
        gui.speciesEdibilityContentLabel.setText("")
        gui.speciesRefDelachauxFleursContentLabel.setText("")
        gui.speciesRefGuide700PlantesContentLabel.setText("")
        gui.speciesRefFlorePyreneesContentLabel.setText("")
        gui.speciesRefDelachauxArbresContentLabel.setText("")
        gui.speciesRefChampignonsContentLabel.setText("")
        # Clear image.
        Image.display(gui.speciesPhotoGraphicsView, None)
        # Disable buttons.
        gui.identificationListPreviousPushButton.clicked.connect(None)
        gui.identificationListPreviousPushButton.setEnabled(False)
        gui.identificationListNextPushButton.clicked.connect(None)
        gui.identificationListNextPushButton.setEnabled(False)
        # Print first identification if it exists.
        Identification.clear(gui)
            