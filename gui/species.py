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
    
    def __init__(self, species_directory_path: str) -> bool:
        # Local variables.
        json_decoded = False
        image_found = False
        # Reset context.
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
    
    def _update_gui(self, gui: object, clear_flag: bool) -> None:
        # Set GUI labels text.
        gui.speciesLatinNameContentLabel.setText(self._latin_name if clear_flag == False else "")
        gui.speciesCommonNameContentLabel.setText(self._common_name if clear_flag == False else "")
        gui.speciesEdibilityContentLabel.setText(self._edibility if clear_flag == False else "")
        gui.speciesRefDelachauxFleursContentLabel.setText(self._ref_delachaux_fleurs if clear_flag == False else "")
        gui.speciesRefGuide700PlantesContentLabel.setText(self._ref_700_plantes if clear_flag == False else "")
        gui.speciesRefFlorePyreneesContentLabel.setText(self._ref_flore_pyrenees if clear_flag == False else "")
        gui.speciesRefDelachauxArbresContentLabel.setText(self._ref_delachaux_arbres if clear_flag == False else "")
        gui.speciesRefChampignonsContentLabel.setText(self._ref_champignons if clear_flag == False else "")
        # Print image.
        Image.display(gui.speciesPhotoGraphicsView, self._image_path if clear_flag == False else None)

    def display(self, gui: object) -> None:
        # Print GUI labels text.
        self._update_gui(gui, False)
    
    def clear(self, gui: object) -> None:
        # Clear GUI labels text.
        self._update_gui(gui, True)
            