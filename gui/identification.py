"""
* identification.py
*
*  Created on: 25 jan. 2026
*      Author: Ludo & Copilot
"""

import json
import logging
import os
import re

from datetime import date
from pathlib import Path
from typing import Any
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTextEdit
from PySide6.QtCore import QDate

from gui.identification_edit_window_ui import Ui_IdentificationEditDialog
from gui.image import Image
from gui.single_slot_connector import SingleSlotConnector

### IDENTIFICATION macros ###

IDENTIFICATION_DATA_FILE_EXTENSION = '.json'

IDENTIFICATION_JSON_KEY_TOP_LEVEL = 'identification'

IDENTIFICATION_JSON_KEY_DATE = 'date'
IDENTIFICATION_JSON_KEY_DATE_DAY = 'day'
IDENTIFICATION_JSON_KEY_DATE_MONTH = 'month'
IDENTIFICATION_JSON_KEY_DATE_YEAR = 'year'
IDENTIFICATION_JSON_KEY_LOCATION = 'location'
IDENTIFICATION_JSON_KEY_LOCATION_CITY = 'city'
IDENTIFICATION_JSON_KEY_LOCATION_DEPARTMENT = 'department'
IDENTIFICATION_JSON_KEY_LOCATION_COUNTRY = 'country'
IDENTIFICATION_JSON_KEY_LOCATION_GPS = 'gps'
IDENTIFICATION_JSON_KEY_LOCATION_GPS_LATITUDE = 'latitude'
IDENTIFICATION_JSON_KEY_LOCATION_GPS_LONGITUDE = 'longitude'
IDENTIFICATION_JSON_KEY_LOCATION_GPS_ALTITUDE = 'altitude'
IDENTIFICATION_JSON_KEY_DESCRIPTION = 'description'

IDENTIFICATION_JSON_KEY_REQUIRED = [
    IDENTIFICATION_JSON_KEY_DATE,
    IDENTIFICATION_JSON_KEY_LOCATION
]

IDENTIFICATION_JSON_KEY_DATE_REQUIRED = [
    IDENTIFICATION_JSON_KEY_DATE_DAY,
    IDENTIFICATION_JSON_KEY_DATE_MONTH,
    IDENTIFICATION_JSON_KEY_DATE_YEAR
]

IDENTIFICATION_JSON_KEY_LOCATION_REQUIRED = [
    IDENTIFICATION_JSON_KEY_LOCATION_CITY,
    IDENTIFICATION_JSON_KEY_LOCATION_DEPARTMENT,
    IDENTIFICATION_JSON_KEY_LOCATION_COUNTRY,
    IDENTIFICATION_JSON_KEY_LOCATION_GPS
]

IDENTIFICATION_JSON_KEY_GPS_REQUIRED = [
    IDENTIFICATION_JSON_KEY_LOCATION_GPS_LATITUDE,
    IDENTIFICATION_JSON_KEY_LOCATION_GPS_LONGITUDE,
    IDENTIFICATION_JSON_KEY_LOCATION_GPS_ALTITUDE
]

IDENTIFICATION_MONTH = [ "Error", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre" ]

### IDENTIFICATION classes ###

"""
* Identification
* Data class containing the identification data.
"""
class Identification:

    def __init__(self) -> None :
        self.date_day = 0
        self.date_month = 0
        self.date_year = 0
        self.location_city = ""
        self.location_department = ""
        self.location_country = ""
        self.location_gps_latitude = 0
        self.location_gps_longitude = 0
        self.location_gps_altitude = 0
        self.description = ""

    def compute_directory_name(self) -> str:
        try:
            date(self.date_year, self.date_month, self.date_day)
        except Exception:
            return "invalid_date"
        return f"{self.date_year:04d}_{self.date_month:02d}_{self.date_day:02d}"

"""
* IdentificationEditWindow
* Graphic class to edit an identification.
"""
class IdentificationEditWindow(QDialog, Ui_IdentificationEditDialog):

    def __init__(self, identification: Identification, new_mode: bool) -> None:
        # Init parent.
        super().__init__()
        # Store species.
        self._identification = identification
        # Setup window.
        self.setupUi(self)
        # Init context.
        self._has_changed = False
        # Check mode.
        if (new_mode == True):
            # Set date to today by default.
            self.setWindowTitle("Nouvelle identification")
            self.dateEdit.setDate(QDate.currentDate())
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            # Print current fields.
            self.setWindowTitle("Edition identification")
            self.dateEdit.setDate(QDate(self._identification.date_year, self._identification.date_month, self._identification.date_day))
            self.cityTextEdit.setPlainText(self._identification.location_city)
            self.departmentTextEdit.setPlainText(self._identification.location_department)
            self.countryTextEdit.setPlainText(self._identification.location_country)
            IdentificationEditWindow._display_coordinate(self.latitudeTextEdit, self._identification.location_gps_latitude)
            IdentificationEditWindow._display_coordinate(self.longitudeTextEdit, self._identification.location_gps_longitude)
            IdentificationEditWindow._display_altitude(self.altitudeTextEdit, self._identification.location_gps_altitude)
            self.descriptionTextEdit.setPlainText(self._identification.description)
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        # Update callbacks.
        self.dateEdit.userDateChanged.connect(self._check_all_fields)
        self.cityTextEdit.textChanged.connect(self._check_all_fields)
        self.departmentTextEdit.textChanged.connect(self._check_all_fields)
        self.countryTextEdit.textChanged.connect(self._check_all_fields)
        self.latitudeTextEdit.textChanged.connect(self._check_all_fields)
        self.longitudeTextEdit.textChanged.connect(self._check_all_fields)
        self.altitudeTextEdit.textChanged.connect(self._check_all_fields)
        self.descriptionTextEdit.textChanged.connect(self._check_all_fields)

    @staticmethod
    def _display_coordinate(text_edit: QTextEdit, coordinate: float) -> None:
        text_edit.setPlainText(str(coordinate) if ((coordinate <= 90.0) and (coordinate >= -90.0)) else "")

    @staticmethod
    def _display_altitude(text_edit: QTextEdit, altitude: int) -> None:
        text_edit.setPlainText(str(altitude) if (altitude >= 0) else "")

    @staticmethod
    def _is_positive_decimal(s: str) -> bool:
        if not re.fullmatch(r'[0-9]+', s):
            return False
        return int(s) >= 0

    @staticmethod
    def _is_float(s: str) -> bool:
        float_regex = re.compile(r'^[0-9]+[.,][0-9]+$')
        return bool(float_regex.fullmatch(s))

    def _check_all_fields(self) -> None:
        # Update flag.
        self._has_changed = True
        valid = True
        # Check strings.
        if (self.cityTextEdit.toPlainText() == ""):
            valid = False
        if (self.departmentTextEdit.toPlainText() == ""):
            valid = False
        if (self.countryTextEdit.toPlainText() == ""):
            valid = False
        # Check coordinates.
        if (IdentificationEditWindow._is_float(self.latitudeTextEdit.toPlainText()) == False):
            valid = False
        if (IdentificationEditWindow._is_float(self.longitudeTextEdit.toPlainText()) == False):
            valid = False
        # Check altitude.
        if (IdentificationEditWindow._is_positive_decimal(self.altitudeTextEdit.toPlainText()) == False):
            valid = False
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(valid)

    @staticmethod
    def _to_altitude(field: str) -> int:
        if ((field is None) or (field == "")):
            return 0
        return int(field)

    @staticmethod
    def _to_coordinate(field: str) -> int:
        if ((field is None) or (field == "")):
            return 0.0
        return float(field)

    def accept(self) -> None:
        # Update parent species fields.
        self._identification.date_day = self.dateEdit.date().day()
        self._identification.date_month = self.dateEdit.date().month()
        self._identification.date_year = self.dateEdit.date().year()
        self._identification.location_city = self.cityTextEdit.toPlainText()
        self._identification.location_department = self.departmentTextEdit.toPlainText()
        self._identification.location_country = self.countryTextEdit.toPlainText()
        self._identification.location_gps_latitude = IdentificationEditWindow._to_coordinate(self.latitudeTextEdit.toPlainText())
        self._identification.location_gps_longitude = IdentificationEditWindow._to_coordinate(self.longitudeTextEdit.toPlainText())
        self._identification.location_gps_altitude = IdentificationEditWindow._to_altitude(self.altitudeTextEdit.toPlainText())
        self._identification.description = self.descriptionTextEdit.toPlainText()
        self.done(1)

    def reject(self) -> None:
        self._has_changed = False
        self.done(0)

"""
* IdentificationView
* Graphic class of the identification panel.
"""
class IdentificationView:
    
    def __init__(self, gui: object, identification_directory_path: str, identification: Identification = None) -> None:
        # Local variables.
        json_decoded = False
        image_found = False
        # Init context.
        self._gui = gui
        self._image_path_list = []
        self._current_image_index = 0
        self._single_slot_connector = SingleSlotConnector()
        # Check initialization mode.
        if (identification is None):
            # Create empty object.
            self._identification = Identification()
            self._json_path = None
        else:
            # Create object from input.
            self._identification = identification
            self._json_path = os.path.join(identification_directory_path, "identification.json")
            # Create JSON file.
            self._write_json()
        # Read directory.
        for f in os.listdir(identification_directory_path):
            # Build complete path.
            p = os.path.join(identification_directory_path, f)
            # Check if there is JSON file.
            if ((Path(f).suffix.lower() == IDENTIFICATION_DATA_FILE_EXTENSION) and (json_decoded == False)):
                # Try parsing JSON file.
                try:
                    self._parse_json(p)
                    json_decoded = True
                    self._json_path = p
                except Exception as e:
                    logging.error("Invalid JSON file : %s", e)
            # Check if there a photo.
            if (Path(f).suffix.lower() == Image.IMAGE_FILE_EXTENSION):
                self._image_path_list.append(p)
                image_found = True
        # Warn if image has not been found.
        if (image_found == False):
            logging.warning("No identification image found")
        # Check if directory content is valid.
        if (json_decoded == False):
            raise ValueError("Invalid identification directory")

    @staticmethod
    def _to_text(value: Any) -> str:
        # Check none input.
        if value is None:
            return ""
        # Convert to string by default.
        return str(value)

    def _parse_json(self, identification_json_path: str) -> None:
        # Open JSON file.
        try:
            with open(identification_json_path, 'r') as json_file:
                data = json.load(json_file)
        except Exception as e:
            raise ValueError(f"Identification JSON file decoding failed: {e}")
        # Check top level key.
        if IDENTIFICATION_JSON_KEY_TOP_LEVEL not in data:
            raise ValueError("Identification JSON file top level key not found")
        # Extract data.
        identification_mapping = data[IDENTIFICATION_JSON_KEY_TOP_LEVEL]
        # Check type.
        if not isinstance(identification_mapping, dict):
            raise ValueError("Invalid identification content: expected an object")
        # Check mandatory keys.
        missing_keys = [k for k in IDENTIFICATION_JSON_KEY_REQUIRED if k not in identification_mapping]
        if missing_keys:
            raise ValueError(f"Missing required identification keys: {', '.join(missing_keys)}")
        date_mapping = identification_mapping.get(IDENTIFICATION_JSON_KEY_DATE)
        missing_keys = [k for k in IDENTIFICATION_JSON_KEY_DATE_REQUIRED if k not in date_mapping]
        if missing_keys:
            raise ValueError(f"Missing required identification keys: {', '.join(missing_keys)}")
        location_mapping = identification_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION)
        missing_keys = [k for k in IDENTIFICATION_JSON_KEY_LOCATION_REQUIRED if k not in location_mapping]
        if missing_keys:
            raise ValueError(f"Missing required identification keys: {', '.join(missing_keys)}")
        gps_mapping = location_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_GPS)
        missing_keys = [k for k in IDENTIFICATION_JSON_KEY_GPS_REQUIRED if k not in gps_mapping]
        if missing_keys:
            raise ValueError(f"Missing required identification keys: {', '.join(missing_keys)}")
        # Update context.
        self._identification.date_day = date_mapping.get(IDENTIFICATION_JSON_KEY_DATE_DAY, 0)
        self._identification.date_month = date_mapping.get(IDENTIFICATION_JSON_KEY_DATE_MONTH, 0)
        self._identification.date_year = date_mapping.get(IDENTIFICATION_JSON_KEY_DATE_YEAR, 0)
        self._identification.location_city = IdentificationView._to_text(location_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_CITY, ""))
        self._identification.location_department = IdentificationView._to_text(location_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_DEPARTMENT, ""))
        self._identification.location_country = IdentificationView._to_text(location_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_COUNTRY, ""))
        self._identification.location_gps_latitude = gps_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_GPS_LATITUDE, 0)
        self._identification.location_gps_longitude = gps_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_GPS_LONGITUDE, 0)
        self._identification.location_gps_altitude = gps_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_GPS_ALTITUDE, 0)
        self._identification.description = IdentificationView._to_text(identification_mapping.get(IDENTIFICATION_JSON_KEY_DESCRIPTION, ""))

    def _write_json(self) -> None:
        # Local variables.
        data = dict()
        # Check local path.
        if (self._json_path is None):
            return
        # Open JSON file in reading mode.
        with open(self._json_path, 'r+' if (os.path.isfile(self._json_path)) else 'w+') as json_file:
            # Compute data.
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL] = dict()
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DATE] = dict()
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DATE][IDENTIFICATION_JSON_KEY_DATE_DAY] = self._identification.date_day
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DATE][IDENTIFICATION_JSON_KEY_DATE_MONTH] = self._identification.date_month
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DATE][IDENTIFICATION_JSON_KEY_DATE_YEAR] = self._identification.date_year
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION] = dict()
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_CITY] = self._identification.location_city
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_DEPARTMENT] = self._identification.location_department
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_COUNTRY] = self._identification.location_country
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_GPS] = dict()
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_GPS][IDENTIFICATION_JSON_KEY_LOCATION_GPS_LATITUDE] = self._identification.location_gps_latitude
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_GPS][IDENTIFICATION_JSON_KEY_LOCATION_GPS_LONGITUDE] = self._identification.location_gps_longitude
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_GPS][IDENTIFICATION_JSON_KEY_LOCATION_GPS_ALTITUDE] = self._identification.location_gps_altitude
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DESCRIPTION] = self._identification.description
            # Write file.
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
            json_file.close()

    def _edit_callback(self) -> None:
        # Open edition window.
        edit_window = IdentificationEditWindow(self._identification, False)
        edit_window.exec()
        # Check if any property has been modified.
        if (edit_window._has_changed == True):
            # Update JSON file.
            self._write_json()
            # Refresh GUI.
            self.display(reset = False)
        edit_window.close()

    def _display_image(self):
        # Local variables.
        image_count = len(self._image_path_list)
        # Check count.
        if (image_count == 0):
            # Clear identification panel.
            Image.clear(self._gui.identificationPhotosGraphicsView)
            self._gui.identificationPhotosPreviousPushButton.setEnabled(False)
            self._gui.identificationPhotosNextPushButton.setEnabled(False)
            # Update title.
            self._gui.identificationPhotosGroupBox.setTitle("Photos (0)")
        else:
            # Check index.
            if (self._current_image_index >= image_count):
                logging.warning("_current_image_index index overflow, defaulting to last")
                self._current_identification_index = (image_count - 1)
            # Print identification.
            Image.display(self._gui.identificationPhotosGraphicsView, self._image_path_list[self._current_image_index])
            # Update buttons state.
            self._gui.identificationPhotosPreviousPushButton.setEnabled(True if (self._current_image_index > 0) else False)
            self._gui.identificationPhotosNextPushButton.setEnabled(True if (self._current_image_index < (image_count - 1)) else False)
            # Update title.
            self._gui.identificationPhotosGroupBox.setTitle("Photos (" + str(self._current_image_index + 1) + "/" + str(image_count) + ")")

    def _previous_image_callback(self):
        # Check index.
        if (self._current_image_index > 0):
            # Print previous item.
            self._current_image_index -= 1
            self._display_image()

    def _next_image_callback(self):
        # Check index.
        if (self._current_image_index < (len(self._image_path_list) - 1)):
            # Print previous item.
            self._current_image_index += 1
            self._display_image()

    def get_identification(self) -> Identification:
        return (self._identification)

    def display(self, reset: bool = True) -> None:
        # Print fields.
        self._gui.identificationDateLabel.setText(str(self._identification.date_day) + " " + IDENTIFICATION_MONTH[self._identification.date_month] + " " + str(self._identification.date_year))
        self._gui.identificationCityContentLabel.setText(self._identification.location_city)
        self._gui.identificationDepartmentContentLabel.setText(self._identification.location_department)
        self._gui.identificationCountryContentLabel.setText(self._identification.location_country)
        self._gui.identificationGpsContentLabel.setText(str(self._identification.location_gps_latitude) + "° " + str(self._identification.location_gps_longitude) + "° (" + str(self._identification.location_gps_altitude) + "m)")
        self._gui.identificationDescriptionContentLabel.setText(self._identification.description)
        # Check call type.
        if (reset == True):
            # Update button callbacks.
            self._single_slot_connector.connect(self._gui.identificationPhotosPreviousPushButton.clicked, self._previous_image_callback)
            self._gui.identificationPhotosPreviousPushButton.setEnabled(True)
            self._single_slot_connector.connect(self._gui.identificationPhotosNextPushButton.clicked, self._next_image_callback)
            self._gui.identificationPhotosNextPushButton.setEnabled(True)
            self._single_slot_connector.connect(self._gui.identificationEditPushButton.clicked, self._edit_callback)
            self._gui.identificationEditPushButton.setEnabled(True)
            # Print first image.
            self._current_image_index = 0
            self._display_image()

    @staticmethod
    def clear(gui: object) -> None:
        # Clear all fields.
        gui.identificationDateLabel.setText("")
        gui.identificationCityContentLabel.setText("")
        gui.identificationDepartmentContentLabel.setText("")
        gui.identificationCountryContentLabel.setText("")
        gui.identificationGpsContentLabel.setText("")
        gui.identificationDescriptionContentLabel.setText("")
        # Clear titles.
        gui.identificationPhotosGroupBox.setTitle("Photos")
        # Clear image.
        Image.display(gui.identificationPhotosGraphicsView, None)
        # Disable buttons.
        gui.identificationPhotosPreviousPushButton.setEnabled(False)
        gui.identificationPhotosNextPushButton.setEnabled(False)
        gui.identificationEditPushButton.setEnabled(False)
            