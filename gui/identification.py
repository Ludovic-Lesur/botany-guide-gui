"""
* identification.py
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

### IDENTIFICATION macros ###

IDENTIFICATION_DATA_FILE_EXTENSION = '.json'

IDENTIFICATION_JSON_KEY_TOP_LEVEL = 'identification'

IDENTIFICATION_JSON_KEY_DATE = 'date'
IDENTIFICATION_JSON_KEY_CITY = 'city'
IDENTIFICATION_JSON_KEY_DEPARTMENT = 'department'
IDENTIFICATION_JSON_KEY_COUNTRY = 'country'
IDENTIFICATION_JSON_KEY_GPS = 'gps'
IDENTIFICATION_JSON_KEY_LATITUDE = 'latitude'
IDENTIFICATION_JSON_KEY_LONGITUDE = 'longitude'
IDENTIFICATION_JSON_KEY_ALTITUDE = 'altitude'
IDENTIFICATION_JSON_KEY_DESCRIPTION = 'description'

IDENTIFICATION_JSON_KEY_REQUIRED = [
    IDENTIFICATION_JSON_KEY_DATE,
    IDENTIFICATION_JSON_KEY_CITY,
    IDENTIFICATION_JSON_KEY_DEPARTMENT,
    IDENTIFICATION_JSON_KEY_COUNTRY,
    IDENTIFICATION_JSON_KEY_GPS
]

IDENTIFICATION_JSON_KEY_GPS_REQUIRED = [
    IDENTIFICATION_JSON_KEY_LATITUDE,
    IDENTIFICATION_JSON_KEY_LONGITUDE,
    IDENTIFICATION_JSON_KEY_ALTITUDE
]

### IDENTIFICATION class ###

class Identification:
    
    def __init__(self, gui: object, identification_directory_path: str) -> None:
        # Local variables.
        json_decoded = False
        image_found = False
        # Init context.
        self._gui = gui
        self._image_path_list = []
        self._current_image_index = 0
        self._date = ""
        self._city = ""
        self._department = ""
        self._country = ""
        self._gps_latitude = ""
        self._gps_longitude = ""
        self._gps_altitude = ""
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
        gps_mapping = identification_mapping.get(IDENTIFICATION_JSON_KEY_GPS)
        missing_keys = [k for k in IDENTIFICATION_JSON_KEY_GPS_REQUIRED if k not in gps_mapping]
        if missing_keys:
            raise ValueError(f"Missing required identification keys: {', '.join(missing_keys)}")
        # Update context.
        self._date = self._to_text(identification_mapping.get(IDENTIFICATION_JSON_KEY_DATE))
        self._city = self._to_text(identification_mapping.get(IDENTIFICATION_JSON_KEY_CITY))
        self._department = self._to_text(identification_mapping.get(IDENTIFICATION_JSON_KEY_DEPARTMENT))
        self._country = self._to_text(identification_mapping.get(IDENTIFICATION_JSON_KEY_COUNTRY))
        self._gps_latitude = self._to_text(gps_mapping.get(IDENTIFICATION_JSON_KEY_LATITUDE))
        self._gps_longitude = self._to_text(gps_mapping.get(IDENTIFICATION_JSON_KEY_LONGITUDE))
        self._gps_altitude = self._to_text(gps_mapping.get(IDENTIFICATION_JSON_KEY_ALTITUDE))
        self._description = self._to_text(identification_mapping.get(IDENTIFICATION_JSON_KEY_DESCRIPTION))

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
        self._gui.identificationDateLabel.setText(self._date)
        self._gui.identificationCityContentLabel.setText(self._city)
        self._gui.identificationDepartmentContentLabel.setText(self._department)
        self._gui.identificationCountryContentLabel.setText(self._country)
        self._gui.identificationGpsContentLabel.setText(self._gps_latitude + "° " + self._gps_longitude + "° (" + self._gps_altitude + "m)")
        self._gui.identificationDescriptionContentLabel.setText(self._description)
        # Update button callbacks.
        self._gui.identificationPhotosPreviousPushButton.clicked.connect(self._previous_image_callback)
        self._gui.identificationPhotosNextPushButton.clicked.connect(self._next_image_callback)
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
        # Clear image.
        Image.display(gui.identificationPhotosGraphicsView, None)
            