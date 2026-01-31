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

from pathlib import Path
from typing import Any
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTextEdit
from PySide6.QtCore import QDate

from gui.identification_edit_window_ui import Ui_IdentificationEditDialog
from gui.image import Image

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
* IdentificationEditWindow
* Graphic class to edit an identification.
"""
class IdentificationEditWindow(QDialog, Ui_IdentificationEditDialog):

    def __init__(self, identification: object) -> None:
        # Init parent.
        super().__init__()
        # Store species.
        self._identification = identification
        # Setup window.
        self.setupUi(self)
        # Init context.
        self._has_changed = False
        # Print current fields.
        self.dateEdit.setDate(QDate(self._identification._date_year, self._identification._date_month, self._identification._date_day))
        self.cityTextEdit.setPlainText(self._identification._location_city)
        self.departmentTextEdit.setPlainText(self._identification._location_department)
        self.countryTextEdit.setPlainText(self._identification._location_country)
        IdentificationEditWindow._display_coordinate(self.latitudeTextEdit, self._identification._location_gps_latitude)
        IdentificationEditWindow._display_coordinate(self.longitudeTextEdit, self._identification._location_gps_longitude)
        IdentificationEditWindow._display_altitude(self.altitudeTextEdit, self._identification._location_gps_altitude)
        self.descriptionTextEdit.setPlainText(self._identification._description)
        # Update callbacks.
        self.dateEdit.userDateChanged.connect(self._date_changed_callback)
        self.cityTextEdit.textChanged.connect(self._city_changed_callback)
        self.departmentTextEdit.textChanged.connect(self._department_changed_callback)
        self.countryTextEdit.textChanged.connect(self._country_changed_callback)
        self.latitudeTextEdit.textChanged.connect(self._latitude_changed_callback)
        self.longitudeTextEdit.textChanged.connect(self._longitude_changed_callback)
        self.altitudeTextEdit.textChanged.connect(self._altitude_changed_callback)
        self.descriptionTextEdit.textChanged.connect(self._description_changed_callback)

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

    def _check_coordinate(self, text_edit: QTextEdit) -> None:
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(IdentificationEditWindow._is_float(text_edit.toPlainText()))

    def _check_altitude(self, text_edit: QTextEdit) -> None:
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(IdentificationEditWindow._is_positive_decimal(text_edit.toPlainText()))

    def _date_changed_callback(self) -> None:
        self._has_changed = True

    def _city_changed_callback(self) -> None:
        self._has_changed = True

    def _department_changed_callback(self) -> None:
        self._has_changed = True

    def _country_changed_callback(self) -> None:
        self._has_changed = True

    def _latitude_changed_callback(self) -> None:
        self._has_changed = True
        self._check_coordinate(self.latitudeTextEdit)

    def _longitude_changed_callback(self) -> None:
        self._has_changed = True
        self._check_coordinate(self.longitudeTextEdit)

    def _altitude_changed_callback(self) -> None:
        self._has_changed = True
        self._check_altitude(self.altitudeTextEdit)

    def _description_changed_callback(self) -> None:
        self._has_changed = True

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
        self._identification._date_day = self.dateEdit.date().day()
        self._identification._date_month = self.dateEdit.date().month()
        self._identification._date_year = self.dateEdit.date().year()
        self._identification._location_city = self.cityTextEdit.toPlainText()
        self._identification._location_department = self.departmentTextEdit.toPlainText()
        self._identification._location_country = self.countryTextEdit.toPlainText()
        self._identification._location_gps_latitude = IdentificationEditWindow._to_coordinate(self.latitudeTextEdit.toPlainText())
        self._identification._location_gps_longitude = IdentificationEditWindow._to_coordinate(self.longitudeTextEdit.toPlainText())
        self._identification._location_gps_altitude = IdentificationEditWindow._to_altitude(self.altitudeTextEdit.toPlainText())
        self._identification._description = self.descriptionTextEdit.toPlainText()
        self.done(1)

    def reject(self) -> None:
        self.done(0)

"""
* Identification
* Main identification class.
"""
class Identification:
    
    def __init__(self, gui: object, identification_directory_path: str) -> None:
        # Local variables.
        json_decoded = False
        image_found = False
        # Init context.
        self._gui = gui
        self._json_path = None
        self._image_path_list = []
        self._internal_call = False
        self._current_image_index = 0
        self._date_day = 0
        self._date_month = 0
        self._date_year = 0
        self._location_city = ""
        self._location_department = ""
        self._location_country = ""
        self._location_gps_latitude = 0
        self._location_gps_longitude = 0
        self._location_gps_altitude = 0
        self._description = ""
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
        self._date_day = date_mapping.get(IDENTIFICATION_JSON_KEY_DATE_DAY, 0)
        self._date_month = date_mapping.get(IDENTIFICATION_JSON_KEY_DATE_MONTH, 0)
        self._date_year = date_mapping.get(IDENTIFICATION_JSON_KEY_DATE_YEAR, 0)
        self._location_city = self._to_text(location_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_CITY, ""))
        self._location_department = self._to_text(location_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_DEPARTMENT, ""))
        self._location_country = self._to_text(location_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_COUNTRY, ""))
        self._location_gps_latitude = gps_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_GPS_LATITUDE, 0)
        self._location_gps_longitude = gps_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_GPS_LONGITUDE, 0)
        self._location_gps_altitude = gps_mapping.get(IDENTIFICATION_JSON_KEY_LOCATION_GPS_ALTITUDE, 0)
        self._description = self._to_text(identification_mapping.get(IDENTIFICATION_JSON_KEY_DESCRIPTION, ""))

    def _write_json(self) -> None:
        # Check local path.
        if (self._json_path is None):
            return
        # Open JSON file.
        with open(self._json_path, 'r+') as json_file:
            # Load data.
            data = json.load(json_file)
            # Update data.
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DATE][IDENTIFICATION_JSON_KEY_DATE_DAY] = self._date_day
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DATE][IDENTIFICATION_JSON_KEY_DATE_MONTH] = self._date_month
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DATE][IDENTIFICATION_JSON_KEY_DATE_YEAR] = self._date_year
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_CITY] = self._location_city
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_DEPARTMENT] = self._location_department
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_COUNTRY] = self._location_country
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_GPS][IDENTIFICATION_JSON_KEY_LOCATION_GPS_LATITUDE] = self._location_gps_latitude
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_GPS][IDENTIFICATION_JSON_KEY_LOCATION_GPS_LONGITUDE] = self._location_gps_longitude
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_LOCATION][IDENTIFICATION_JSON_KEY_LOCATION_GPS][IDENTIFICATION_JSON_KEY_LOCATION_GPS_ALTITUDE] = self._location_gps_altitude
            data[IDENTIFICATION_JSON_KEY_TOP_LEVEL][IDENTIFICATION_JSON_KEY_DESCRIPTION] = self._description
            # Write file.
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
            json_file.close()

    def _edit_callback(self) -> None:
        # Open edition window.
        edit_window = IdentificationEditWindow(self)
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

    def display(self) -> None:
        # Print fields.
        self._gui.identificationDateLabel.setText(str(self._date_day) + " " + IDENTIFICATION_MONTH[self._date_month] + " " + str(self._date_year))
        self._gui.identificationCityContentLabel.setText(self._location_city)
        self._gui.identificationDepartmentContentLabel.setText(self._location_department)
        self._gui.identificationCountryContentLabel.setText(self._location_country)
        self._gui.identificationGpsContentLabel.setText(str(self._location_gps_latitude) + "° " + str(self._location_gps_longitude) + "° (" + str(self._location_gps_altitude) + "m)")
        self._gui.identificationDescriptionContentLabel.setText(self._description)
        # Enable edit button.
        self._gui.identificationEditPushButton.setEnabled(True)
        # Check call type.
        if (self._internal_call == False):
            # Update button callbacks.
            self._gui.identificationPhotosPreviousPushButton.clicked.disconnect()
            self._gui.identificationPhotosPreviousPushButton.clicked.connect(self._previous_image_callback)
            self._gui.identificationPhotosNextPushButton.clicked.disconnect()
            self._gui.identificationPhotosNextPushButton.clicked.connect(self._next_image_callback)
            self._gui.identificationEditPushButton.clicked.disconnect()
            self._gui.identificationEditPushButton.clicked.connect(self._edit_callback)
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
        # Disable edit button.
        gui.identificationEditPushButton.setEnabled(False)
            