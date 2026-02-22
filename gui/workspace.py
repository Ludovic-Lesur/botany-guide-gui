"""
* workspace.py
*
*  Created on: 09 feb. 2026
*      Author: Ludo
"""

import json
import logging
import os

from typing import Any
from PySide6.QtWidgets import QFileDialog

from gui.classification import ClassificationView

### CLASSIFICATION macros ###   

WORKSPACE_FILE = 'workspace.json'
WORKSPACE_JSON_KEY_TOP_LEVEL = 'workspace'
WORKSPACE_JSON_KEY_DIRECTORY_PATH = 'directory_path'

### CLASSIFICATION class definition ###
        
class WorkspaceView:
    
    def __init__(self, gui: object) -> None:
        # Local variables.
        root_directory = os.getcwd()
        # Init context.
        self._gui = gui
        self._directory_path = ""
        # Check if there is a workspace file.
        for f in sorted(os.listdir(root_directory)):
            # Build complete path.
            p = os.path.join(root_directory, f)
            # Check name.
            if (f == WORKSPACE_FILE):
                # Try parsing JSON file.
                try:
                    self._parse_json(p)
                    break
                except Exception as e:
                    logging.error("Invalid JSON file : %s", e)
        # Check workspace.
        if ((self._directory_path is None) or (self._directory_path == "")):
            # Ask workspace.
            self._edit_workspace_callback()
        # Setup workspace view.
        self._gui.workspaceContentLabel.setText(self._directory_path)
        self._gui.workspaceEditPushButton.clicked.connect(self._edit_workspace_callback)
        self._gui.workspaceEditPushButton.setEnabled(True)
        # Display classification.
        self._classification = ClassificationView(self._gui, self._directory_path)
        
    @staticmethod
    def _to_text(value: Any) -> str:
        if value is None:
            return ""
        return str(value)
            
    def _parse_json(self, workspace_json_path: str) -> None:
        # Open JSON file.
        try:
            with open(workspace_json_path, 'r') as json_file:
                data = json.load(json_file)
        except Exception as e:
            raise ValueError(f"Workspace JSON file decoding failed: {e}")
        # Check top level key.
        if WORKSPACE_JSON_KEY_TOP_LEVEL not in data:
            raise ValueError("Workspace JSON file top level key not found")
        # Extract data.
        workspace_mapping = data[WORKSPACE_JSON_KEY_TOP_LEVEL]
        # Check type.
        if not isinstance(workspace_mapping, dict):
            raise ValueError("Invalid workspace content: expected an object")
        # Update context.
        self._directory_path = self._to_text(workspace_mapping.get(WORKSPACE_JSON_KEY_DIRECTORY_PATH, ""))

    def _write_json(self) -> None:
        # Local variables.
        data = dict()
        json_path = os.path.join(os.getcwd(), WORKSPACE_FILE)
        # Open JSON file.
        with open(json_path, 'r+' if (os.path.isfile(json_path)) else 'w+') as json_file:
            # Compute data.
            data[WORKSPACE_JSON_KEY_TOP_LEVEL] = dict()
            data[WORKSPACE_JSON_KEY_TOP_LEVEL][WORKSPACE_JSON_KEY_DIRECTORY_PATH] = self._directory_path
            # Write file.
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
            json_file.close()
            
    def _edit_workspace_callback(self) -> None:
        # Ask new workspace.
        new_directory_path = QFileDialog.getExistingDirectory(None, 'Select a folder', os.getcwd(), QFileDialog.ShowDirsOnly)
        # Check returned value.
        if ((new_directory_path is None) or (new_directory_path == "")):
            return
        self._directory_path = new_directory_path
        self._gui.workspaceContentLabel.setText(self._directory_path)
        # Update metadata file.
        self._write_json()
        # Display new classification.
        self._classification = ClassificationView(self._gui, self._directory_path)
            