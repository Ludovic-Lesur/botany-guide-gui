"""
* species.py
*
*  Created on: 25 jan. 2026
*      Author: Ludo & Copilot
"""

import json
import logging
import os
import re

from pathlib import Path
from typing import Any
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTextEdit

from gui.species_edit_window_ui import Ui_SpeciesEditDialog
from gui.identification import Identification
from gui.image import Image

### SPECIES macros ###

SPECIES_DATA_FILE_EXTENSION = '.json'

SPECIES_JSON_KEY_TOP_LEVEL = 'species'

SPECIES_JSON_KEY_LATIN_NAME = 'latinName'
SPECIES_JSON_KEY_COMMON_NAME = 'commonName'
SPECIES_JSON_KEY_EDIBILITY = 'edibility'
SPECIES_JSON_KEY_REFERENCES = 'references'
SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_FLEURS = 'guideDelachauxFleurs'
SPECIES_JSON_KEY_REFERENCES_RECONNAITRE_700_PLANTES = 'reconnaitre700Plantes'
SPECIES_JSON_KEY_REFERENCES_DECOUVRIR_FLORE_PYRENEES = 'decouvrirFlorePyrenees'
SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_ARBRES = 'guideDelachauxArbres'
SPECIES_JSON_KEY_REFERENCES_GUIDE_CHAMPIGNONS = 'guideChampignons'

SPECIES_JSON_KEY_REQUIRED = [
    SPECIES_JSON_KEY_LATIN_NAME,
    SPECIES_JSON_KEY_COMMON_NAME
]

### SPECIES classes ###

"""
* SpeciesEditWindow
* Graphic class to edit a species.
"""
class SpeciesEditWindow(QDialog, Ui_SpeciesEditDialog):

    def __init__(self, species: object) -> None:
        # Init parent.
        super().__init__()
        # Store species.
        self._species = species
        # Setup window.
        self.setupUi(self)
        # Init context.
        self._has_changed = False
        # Print current fields.
        self.latinNameTextEdit.setPlainText(self._species._latin_name)
        self.commonNameTextEdit.setPlainText(self._species._common_name)
        self.edibilityTextEdit.setPlainText(self._species._edibility)
        SpeciesEditWindow._display_page(self.refDelachauxFleursTextEdit, self._species._ref_delachaux_fleurs)
        SpeciesEditWindow._display_page(self.ref700PlantesTextEdit, self._species._ref_700_plantes)
        SpeciesEditWindow._display_page(self.refFlorePyreneesTextEdit, self._species._ref_flore_pyrenees)
        SpeciesEditWindow._display_page(self.refDelachauxArbresTextEdit, self._species._ref_delachaux_arbres)
        SpeciesEditWindow._display_page(self.refChampignonsTextEdit, self._species._ref_champignons)
        # Update callbacks.
        self.latinNameTextEdit.textChanged.connect(self._latin_name_changed_callback)
        self.commonNameTextEdit.textChanged.connect(self._common_name_changed_callback)
        self.edibilityTextEdit.textChanged.connect(self._edibility_changed_callback)
        self.refDelachauxFleursTextEdit.textChanged.connect(self._ref_delachaux_fleurs_changed_callback)
        self.ref700PlantesTextEdit.textChanged.connect(self._ref_700_plantes_changed_callback)
        self.refFlorePyreneesTextEdit.textChanged.connect(self._ref_flore_pyrenees_changed_callback)
        self.refDelachauxArbresTextEdit.textChanged.connect(self._ref_delachaux_arbres_changed_callback)
        self.refChampignonsTextEdit.textChanged.connect(self._ref_champignons_changed_callback)

    @staticmethod
    def _is_positive_decimal(s: str) -> bool:
        if (s == ""):
            return True
        if not re.fullmatch(r'[0-9]+', s):
            return False
        return int(s) > 0

    @staticmethod
    def _display_page(text_edit: QTextEdit, page: int) -> None:
        text_edit.setPlainText(str(page) if (page > 0) else "")

    def _check_page(self, text_edit: QTextEdit) -> None:
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(SpeciesEditWindow._is_positive_decimal(text_edit.toPlainText()))

    def _latin_name_changed_callback(self) -> None:
        self._has_changed = True

    def _common_name_changed_callback(self) -> None:
        self._has_changed = True

    def _edibility_changed_callback(self) -> None:
        self._has_changed = True

    def _ref_delachaux_fleurs_changed_callback(self) -> None:
        self._has_changed = True
        self._check_page(self.refDelachauxFleursTextEdit)

    def _ref_700_plantes_changed_callback(self) -> None:
        self._has_changed = True
        self._check_page(self.ref700PlantesTextEdit)

    def _ref_flore_pyrenees_changed_callback(self) -> None:
        self._has_changed = True
        self._check_page(self.refFlorePyreneesTextEdit)

    def _ref_delachaux_arbres_changed_callback(self) -> None:
        self._has_changed = True
        self._check_page(self.refDelachauxArbresTextEdit)

    def _ref_champignons_changed_callback(self) -> None:
        self._has_changed = True
        self._check_page(self.refChampignonsTextEdit)

    @staticmethod
    def _to_page(field: str) -> int:
        if ((field is None) or (field == "")):
            return 0
        return int(field)

    def accept(self) -> None:
        # Update parent species fields.
        self._species._latin_name = self.latinNameTextEdit.toPlainText()
        self._species._common_name = self.commonNameTextEdit.toPlainText()
        self._species._edibility = self.edibilityTextEdit.toPlainText()
        self._species._ref_delachaux_fleurs = SpeciesEditWindow._to_page(self.refDelachauxFleursTextEdit.toPlainText())
        self._species._ref_700_plantes = SpeciesEditWindow._to_page(self.ref700PlantesTextEdit.toPlainText())
        self._species._ref_flore_pyrenees = SpeciesEditWindow._to_page(self.refFlorePyreneesTextEdit.toPlainText())
        self._species._ref_delachaux_arbres = SpeciesEditWindow._to_page(self.refDelachauxArbresTextEdit.toPlainText())
        self._species._ref_champignons = SpeciesEditWindow._to_page(self.refChampignonsTextEdit.toPlainText())
        self.done(1)

    def reject(self) -> None:
        self.done(0)

"""
* Species
* Main species class.
"""
class Species:

    def __init__(self, gui: object, species_directory_path: str) -> None:
        # Local variables.
        json_decoded = False
        image_found = False
        # Init context.
        self._gui = gui
        self._json_path = None
        self._image_path = None
        self._internal_call = False
        self._identification_list = []
        self._current_identification_index = 0
        self._latin_name = ""
        self._common_name = ""
        self._edibility = ""
        self._ref_delachaux_fleurs = 0
        self._ref_700_plantes = 0
        self._ref_flore_pyrenees = 0
        self._ref_delachaux_arbres = 0
        self._ref_champignons = 0
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
                    self._json_path = p
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
    def _to_text(value: Any) -> str:
        if value is None:
            return ""
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
        self._latin_name = self._to_text(species_mapping.get(SPECIES_JSON_KEY_LATIN_NAME, ""))
        self._common_name = self._to_text(species_mapping.get(SPECIES_JSON_KEY_COMMON_NAME, ""))
        self._edibility = self._to_text(species_mapping.get(SPECIES_JSON_KEY_EDIBILITY, ""))
        self._ref_delachaux_fleurs = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_FLEURS, 0)
        self._ref_700_plantes = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_RECONNAITRE_700_PLANTES, 0)
        self._ref_flore_pyrenees = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_DECOUVRIR_FLORE_PYRENEES, 0)
        self._ref_delachaux_arbres = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_ARBRES, 0)
        self._ref_champignons = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_GUIDE_CHAMPIGNONS, 0)

    def _write_json(self) -> None:
        # Check local path.
        if (self._json_path is None):
            return
        # Open JSON file.
        with open(self._json_path, 'r+') as json_file:
            # Load data.
            data = json.load(json_file)
            # Update data.
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_LATIN_NAME] = self._latin_name
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_COMMON_NAME] = self._common_name
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_EDIBILITY] = self._edibility
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_FLEURS] = self._ref_delachaux_fleurs
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_RECONNAITRE_700_PLANTES] = self._ref_700_plantes
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_DECOUVRIR_FLORE_PYRENEES] = self._ref_flore_pyrenees
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_ARBRES] = self._ref_delachaux_arbres
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_GUIDE_CHAMPIGNONS] = self._ref_champignons
            # Write file.
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
            json_file.close()

    def _edit_callback(self) -> None:
        # Open edition window.
        edit_window = SpeciesEditWindow(self)
        edit_window.exec()
        # Check if any property has been modified.
        if (edit_window._has_changed == True):
            # Update JSON file.
            self._write_json()
            # Refresh GUI.
            self._internal_call = True
            self.display()
            self._internal_call = False
        edit_window.close()

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

    @staticmethod
    def _display_page(page: int) -> str:
        if ((page is None) or (page == 0)):
            return ""
        return ("p. " + str(page))

    def display(self) -> None:
        # Print fields.
        self._gui.speciesLatinNameContentLabel.setText(self._latin_name)
        self._gui.speciesCommonNameContentLabel.setText(self._common_name)
        self._gui.speciesEdibilityContentLabel.setText(self._edibility)
        self._gui.speciesRefDelachauxFleursContentLabel.setText(Species._display_page(self._ref_delachaux_fleurs))
        self._gui.speciesRefGuide700PlantesContentLabel.setText(Species._display_page(self._ref_700_plantes))
        self._gui.speciesRefFlorePyreneesContentLabel.setText(Species._display_page(self._ref_flore_pyrenees))
        self._gui.speciesRefDelachauxArbresContentLabel.setText(Species._display_page(self._ref_delachaux_arbres))
        self._gui.speciesRefChampignonsContentLabel.setText(Species._display_page(self._ref_champignons))
        # Check call type.
        if (self._internal_call == False):
            # Update image.
            Image.display(self._gui.speciesPhotoGraphicsView, self._image_path)
            # Update buttons callbacks.
            self._gui.identificationListPreviousPushButton.clicked.disconnect()
            self._gui.identificationListPreviousPushButton.clicked.connect(self._previous_identification_callback)
            self._gui.identificationListNextPushButton.clicked.disconnect()
            self._gui.identificationListNextPushButton.clicked.connect(self._next_identification_callback)
            self._gui.speciesEditPushButton.clicked.disconnect()
            self._gui.speciesEditPushButton.clicked.connect(self._edit_callback)
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
        # Update title.
        gui.identificationListGroupBox.setTitle("Liste")
        # Clear image.
        Image.display(gui.speciesPhotoGraphicsView, None)
        # Disable buttons.
        gui.identificationListPreviousPushButton.clicked.connect(None)
        gui.identificationListPreviousPushButton.setEnabled(False)
        gui.identificationListNextPushButton.clicked.connect(None)
        gui.identificationListNextPushButton.setEnabled(False)
        gui.speciesEditPushButton.clicked.connect(None)
        gui.speciesEditPushButton.clicked.setEnabled(False)
        # Print first identification if it exists.
        Identification.clear(gui)
            