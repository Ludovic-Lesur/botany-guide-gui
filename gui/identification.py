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
    
    def __init__(self, identification_directory_path: str) -> None:
        # Local variables.
        json_decoded = False
        image_found = False
        # Reset context.
        self._date = ""
        self._image_path_list = []
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

    def _update_gui(self, gui: object, clear_flag: bool) -> None:
        # Set GUI labels text.
        gui.identificationDateLabel.setText(self._date if clear_flag == False else "")
        gui.identificationCityContentLabel.setText(self._city if clear_flag == False else "")
        gui.identificationDepartmentContentLabel.setText(self._department if clear_flag == False else "")
        gui.identificationCountryContentLabel.setText(self._country if clear_flag == False else "")
        gui.identificationGpsContentLabel.setText((self._gps_latitude + "° " + self._gps_longitude + "° (" + self._gps_altitude + "m)") if clear_flag == False else "")
        gui.identificationDescriptionContentLabel.setText(self._description if clear_flag == False else "")
        # Print image.
        if (len(self._image_path_list) > 0):
            Image.display(gui.identificationPhotosGraphicsView, self._image_path_list[0])
        else:
            Image.display(gui.identificationPhotosGraphicsView, None)
    
    def display(self, gui: object) -> None:
        # Print GUI labels text.
        self._update_gui(gui, False)
    
    def clear(self, gui: object) -> None:
        # Clear GUI labels text.
        self._update_gui(gui, True)
            