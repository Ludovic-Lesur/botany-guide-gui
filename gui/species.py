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
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTextEdit, QFileDialog
from PySide6.QtGui import QDesktopServices

from gui.single_slot_connector import SingleSlotConnector
from gui.species_edit_window_ui import Ui_SpeciesEditDialog
from gui.identification import Identification, IdentificationEditWindow, IdentificationView
from gui.image import Image

### SPECIES macros ###

SPECIES_DATA_FILE_EXTENSION = '.json'

SPECIES_JSON_KEY_TOP_LEVEL = 'species'

SPECIES_JSON_KEY_NAME = 'name'
SPECIES_JSON_KEY_NAME_LATIN = 'latin'
SPECIES_JSON_KEY_NAME_COMMON = 'common'
SPECIES_JSON_KEY_EDIBILITY = 'edibility'
SPECIES_JSON_KEY_REFERENCES = 'references'
SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_FLEURS = 'guideDelachauxFleurs'
SPECIES_JSON_KEY_REFERENCES_RECONNAITRE_700_PLANTES = 'reconnaitre700Plantes'
SPECIES_JSON_KEY_REFERENCES_DECOUVRIR_FLORE_PYRENEES = 'decouvrirFlorePyrenees'
SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_ARBRES = 'guideDelachauxArbres'
SPECIES_JSON_KEY_REFERENCES_GUIDE_CHAMPIGNONS = 'guideChampignons'

SPECIES_JSON_KEY_REQUIRED = [
    SPECIES_JSON_KEY_NAME,
]

SPECIES_JSON_KEY_NAME_REQUIRED = [
    SPECIES_JSON_KEY_NAME_LATIN,
    SPECIES_JSON_KEY_NAME_COMMON
]

### SPECIES classes ###

"""
* Species
* Data class containing the species data.
"""
class Species:

    def __init__(self) -> None :
        self.latin_name = ""
        self.common_name = ""
        self.edibility = ""
        self.references_guide_delachaux_fleurs = 0
        self.references_reconnaitre_700_plantes = 0
        self.references_decouvrir_flore_pyrenees = 0
        self.references_guide_delachaux_arbres = 0
        self.references_guide_champignons = 0
        self.creation_directory_path = ""

    def compute_json_file_name(self) -> str:
        try:
            json_file_name = self.latin_name.strip().lower()
        except Exception:
            return "invalid_latin_name.json"
        result = re.sub(r"\s+", "_", json_file_name)
        return (result + ".json")

"""
* SpeciesEditWindow
* Graphic class to edit a species.
"""
class SpeciesEditWindow(QDialog, Ui_SpeciesEditDialog):

    def __init__(self, species: Species, new_mode: bool, creation_directory_path_default: str) -> None:
        # Init parent.
        super().__init__()
        # Store species.
        self._species = species
        # Setup window.
        self.setupUi(self)
        # Init context.
        self._has_changed = False
        self._creation_directory_path = creation_directory_path_default
        # Print current fields.
        if (new_mode == True):
            # Enable explorer.
            self.setWindowTitle("Nouvelle espèce")
            self.explorerPushButton.setEnabled(True)
            self.directoryContentLabel.setText(self._creation_directory_path)
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            # Print current fields.
            self.setWindowTitle("Edition espèce")
            self.latinNameTextEdit.setPlainText(self._species.latin_name)
            self.commonNameTextEdit.setPlainText(self._species.common_name)
            self.edibilityTextEdit.setPlainText(self._species.edibility)
            SpeciesEditWindow._display_page(self.refDelachauxFleursTextEdit, self._species.references_guide_delachaux_fleurs)
            SpeciesEditWindow._display_page(self.ref700PlantesTextEdit, self._species.references_reconnaitre_700_plantes)
            SpeciesEditWindow._display_page(self.refFlorePyreneesTextEdit, self._species.references_decouvrir_flore_pyrenees)
            SpeciesEditWindow._display_page(self.refDelachauxArbresTextEdit, self._species.references_guide_delachaux_arbres)
            SpeciesEditWindow._display_page(self.refChampignonsTextEdit, self._species.references_guide_champignons)
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
            self.explorerPushButton.setEnabled(False)
        # Update callbacks.
        self.explorerPushButton.clicked.connect(self._open_explorer_callback)
        self.latinNameTextEdit.textChanged.connect(self._check_all_fields)
        self.commonNameTextEdit.textChanged.connect(self._check_all_fields)
        self.edibilityTextEdit.textChanged.connect(self._check_all_fields)
        self.refDelachauxFleursTextEdit.textChanged.connect(self._check_all_fields)
        self.ref700PlantesTextEdit.textChanged.connect(self._check_all_fields)
        self.refFlorePyreneesTextEdit.textChanged.connect(self._check_all_fields)
        self.refDelachauxArbresTextEdit.textChanged.connect(self._check_all_fields)
        self.refChampignonsTextEdit.textChanged.connect(self._check_all_fields)

    @staticmethod
    def _display_page(text_edit: QTextEdit, page: int) -> None:
        text_edit.setPlainText(str(page) if (page > 0) else "")

    @staticmethod
    def _is_positive_decimal(s: str) -> bool:
        if (s == ""):
            return True
        if not re.fullmatch(r'[0-9]+', s):
            return False
        return int(s) > 0

    def _check_all_fields(self) -> None:
        # Update flag.
        self._has_changed = True
        valid = True
        # Check strings.
        if (self.latinNameTextEdit.toPlainText() == ""):
            valid = False
        if (self.commonNameTextEdit.toPlainText() == ""):
            valid = False
        # Check pages.
        if (SpeciesEditWindow._is_positive_decimal(self.refDelachauxFleursTextEdit.toPlainText()) == False):
            valid = False
        if (SpeciesEditWindow._is_positive_decimal(self.ref700PlantesTextEdit.toPlainText()) == False):
            valid = False
        if (SpeciesEditWindow._is_positive_decimal(self.refFlorePyreneesTextEdit.toPlainText()) == False):
            valid = False
        if (SpeciesEditWindow._is_positive_decimal(self.refDelachauxArbresTextEdit.toPlainText()) == False):
            valid = False
        if (SpeciesEditWindow._is_positive_decimal(self.refChampignonsTextEdit.toPlainText()) == False):
            valid = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(valid)

    def _open_explorer_callback(self):
        # Open explorer.
        new_directory_path = QFileDialog.getExistingDirectory(None, 'Select a folder', self._creation_directory_path, QFileDialog.ShowDirsOnly)
        # Check returned value.
        if ((new_directory_path is None) or (new_directory_path == "")):
            return
        # Update context.
        self._has_changed = True
        self._creation_directory_path = new_directory_path
        self.directoryContentLabel.setText(self._creation_directory_path)

    @staticmethod
    def _to_page(field: str) -> int:
        if ((field is None) or (field == "")):
            return 0
        return int(field)

    def accept(self) -> None:
        # Update parent species fields.
        self._species.latin_name = self.latinNameTextEdit.toPlainText()
        self._species.common_name = self.commonNameTextEdit.toPlainText()
        self._species.edibility = self.edibilityTextEdit.toPlainText()
        self._species.references_guide_delachaux_fleurs = SpeciesEditWindow._to_page(self.refDelachauxFleursTextEdit.toPlainText())
        self._species.references_reconnaitre_700_plantes = SpeciesEditWindow._to_page(self.ref700PlantesTextEdit.toPlainText())
        self._species.references_decouvrir_flore_pyrenees = SpeciesEditWindow._to_page(self.refFlorePyreneesTextEdit.toPlainText())
        self._species.references_guide_delachaux_arbres = SpeciesEditWindow._to_page(self.refDelachauxArbresTextEdit.toPlainText())
        self._species.references_guide_champignons = SpeciesEditWindow._to_page(self.refChampignonsTextEdit.toPlainText())
        self._species.creation_directory_path = self._creation_directory_path
        self.done(1)

    def reject(self) -> None:
        self._has_changed = False
        self.done(0)

"""
* Species
* Main species class.
"""
class SpeciesView:

    def __init__(self, gui: object, species_directory_path: str, species: Species = None) -> None:
        # Local variables.
        json_decoded = False
        image_found = False
        # Init context.
        self._gui = gui
        self._directory_path = species_directory_path
        self._image_path = None
        self._identification_view_list = []
        self._current_identification_index = 0
        self._single_slot_connector = SingleSlotConnector()
        # Check initialization mode.
        if (species is None):
            # Create empty object.
            self._species = Species()
            self._json_path = None
        else:
            # Create object from input.
            self._species = species
            self._json_path = os.path.join(species_directory_path, self._species.compute_json_file_name())
            # Create JSON file.
            self._write_json()
        # Read directory.
        for f in sorted(os.listdir(species_directory_path)):
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
                    identification_view = IdentificationView(self._gui, p)
                    self._identification_view_list.append(identification_view)
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
        name_mapping = species_mapping.get(SPECIES_JSON_KEY_NAME)
        missing_keys = [k for k in SPECIES_JSON_KEY_NAME_REQUIRED if k not in name_mapping]
        if missing_keys:
            raise ValueError(f"Missing required identification keys: {', '.join(missing_keys)}")
        # Update context.
        self._species.latin_name = self._to_text(name_mapping.get(SPECIES_JSON_KEY_NAME_LATIN, ""))
        self._species.common_name = self._to_text(name_mapping.get(SPECIES_JSON_KEY_NAME_COMMON, ""))
        self._species.edibility = self._to_text(species_mapping.get(SPECIES_JSON_KEY_EDIBILITY, ""))
        self._species.references_guide_delachaux_fleurs = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_FLEURS, 0)
        self._species.references_reconnaitre_700_plantes = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_RECONNAITRE_700_PLANTES, 0)
        self._species.references_decouvrir_flore_pyrenees = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_DECOUVRIR_FLORE_PYRENEES, 0)
        self._species.references_guide_delachaux_arbres = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_ARBRES, 0)
        self._species.references_guide_champignons = species_mapping.get(SPECIES_JSON_KEY_REFERENCES).get(SPECIES_JSON_KEY_REFERENCES_GUIDE_CHAMPIGNONS, 0)

    def _write_json(self) -> None:
        # Local variables.
        data = dict()
        # Check local path.
        if (self._json_path is None):
            return
        # Open JSON file.
        with open(self._json_path, 'r+' if (os.path.isfile(self._json_path)) else 'w+') as json_file:
            # Compute data.
            data[SPECIES_JSON_KEY_TOP_LEVEL] = dict()
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_NAME]= dict()
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_NAME][SPECIES_JSON_KEY_NAME_LATIN] = self._species.latin_name
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_NAME][SPECIES_JSON_KEY_NAME_COMMON] = self._species.common_name
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_EDIBILITY] = self._species.edibility
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES] = dict()
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_FLEURS] = self._species.references_guide_delachaux_fleurs
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_RECONNAITRE_700_PLANTES] = self._species.references_reconnaitre_700_plantes
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_DECOUVRIR_FLORE_PYRENEES] = self._species.references_decouvrir_flore_pyrenees
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_GUIDE_DELACHAUX_ARBRES] = self._species.references_guide_delachaux_arbres
            data[SPECIES_JSON_KEY_TOP_LEVEL][SPECIES_JSON_KEY_REFERENCES][SPECIES_JSON_KEY_REFERENCES_GUIDE_CHAMPIGNONS] = self._species.references_guide_champignons
            # Write file.
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
            json_file.close()

    def _edit_callback(self) -> None:
        # Open edition window.
        edit_window = SpeciesEditWindow(self._species, False, None)
        edit_window.exec()
        # Check if any property has been modified.
        if (edit_window._has_changed == True):
            # Update JSON file.
            self._write_json()
            # Refresh GUI.
            self.display(update_identification = False, reset_identification = False)
        edit_window.close()

    def _open_directory_callback(self) -> None:
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(Path(self._directory_path).resolve())))

    def _add_identification_callback(self) -> None:
        # Create static object.
        new_identification = Identification()
        # Open new window.
        new_window = IdentificationEditWindow(new_identification, True)
        new_window.exec()
        # Check if any property has been modified.
        if (new_window._has_changed == True):
            # Check if date is new.
            for identification_view in self._identification_view_list:
                if ((new_identification.date_day == identification_view.get_identification().date_day) and
                    (new_identification.date_month == identification_view.get_identification().date_month) and
                    (new_identification.date_year == identification_view.get_identification().date_year)):
                    print("Error same date")
                    return
            # Compute directory name.
            identification_directory_path = os.path.join(self._directory_path, new_identification.compute_directory_name())
            # Check if folder already exists.
            if os.path.exists(identification_directory_path):
                print("Error directory already exists")
                return
            # Create folder.
            os.makedirs(identification_directory_path)
            # Create identification object.
            new_identification_view = IdentificationView(self._gui, identification_directory_path, new_identification)
            self._identification_view_list.append(new_identification_view)
            # Refresh GUI.
            self.display(update_identification = True, reset_identification = False)
        new_window.close()

    def _display_identification(self):
        # Local variables.
        identification_count = len(self._identification_view_list)
        # Check count.
        if (identification_count == 0):
            # Clear identification panel.
            IdentificationView.clear(self._gui)
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
            self._identification_view_list[self._current_identification_index].display()
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
        if (self._current_identification_index < (len(self._identification_view_list) - 1)):
            # Print previous item.
            self._current_identification_index += 1
            self._display_identification()

    @staticmethod
    def _display_page(page: int) -> str:
        if ((page is None) or (page == 0)):
            return ""
        return ("p. " + str(page))

    def display(self, update_identification: bool = True, reset_identification: bool = True) -> None:
        # Print fields.
        self._gui.speciesLatinNameContentLabel.setText(self._species.latin_name)
        self._gui.speciesCommonNameContentLabel.setText(self._species.common_name)
        self._gui.speciesEdibilityContentLabel.setText(self._species.edibility)
        self._gui.speciesRefDelachauxFleursContentLabel.setText(SpeciesView._display_page(self._species.references_guide_delachaux_fleurs))
        self._gui.speciesRefGuide700PlantesContentLabel.setText(SpeciesView._display_page(self._species.references_reconnaitre_700_plantes))
        self._gui.speciesRefFlorePyreneesContentLabel.setText(SpeciesView._display_page(self._species.references_decouvrir_flore_pyrenees))
        self._gui.speciesRefDelachauxArbresContentLabel.setText(SpeciesView._display_page(self._species.references_guide_delachaux_arbres))
        self._gui.speciesRefChampignonsContentLabel.setText(SpeciesView._display_page(self._species.references_guide_champignons))
        # Update image.
        Image.display(self._gui.speciesPhotoGraphicsView, self._image_path)
        # Check call type.
        if (update_identification == True):
            # Update buttons callbacks.
            self._single_slot_connector.connect(self._gui.speciesEditPushButton.clicked, self._edit_callback)
            self._gui.speciesEditPushButton.setEnabled(True)
            self._single_slot_connector.connect(self._gui.speciesOpenDirectoryPushButton.clicked, self._open_directory_callback)
            self._gui.speciesOpenDirectoryPushButton.setEnabled(True)
            self._single_slot_connector.connect(self._gui.identificationAddPushButton.clicked, self._add_identification_callback)
            self._gui.identificationAddPushButton.setEnabled(True)
            self._single_slot_connector.connect(self._gui.identificationListPreviousPushButton.clicked, self._previous_identification_callback)
            self._single_slot_connector.connect(self._gui.identificationListNextPushButton.clicked, self._next_identification_callback)
            # Print first identification in case of reset.
            if (reset_identification == True):
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
        gui.speciesEditPushButton.setEnabled(False)
        gui.speciesOpenDirectoryPushButton.setEnabled(False)
        gui.identificationAddPushButton.setEnabled(False)
        gui.identificationListPreviousPushButton.setEnabled(False)
        gui.identificationListNextPushButton.setEnabled(False)
        # Print first identification if it exists.
        IdentificationView.clear(gui)
            