"""
* gui.py
*
*  Created on: 21 dec. 2025
*      Author: Ludo
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from gui.workspace import WorkspaceView
from gui.main_window_ui import Ui_MainWindow
from gui.version import get_git_version
from gui import _build_version

### GUI classes ###

class BotanyGuideGui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        # Init parent.
        super().__init__()
        # Setup window.
        self.setupUi(self)
        self.setWindowTitle("Botany Guide GUI (" + self._get_git_version() + ")")
        # Setup tree view.
        self._workspace = WorkspaceView(self)

    def _get_git_version(self) -> str:
        # Read from version file.
        git_version = self._get_git_version_from_file()
        if git_version:
            return git_version
        try:
            return get_git_version().format()
        except Exception:
            return "Unknown version"

    def _get_git_version_from_file(self) -> str | None:
        try:
            git_version = getattr(_build_version, "VERSION", None)
            if git_version and git_version != "dev":
                return str(git_version)
            return None
        except Exception:
            return None
            
### GUI main function ###

if __name__ == "__main__":
    # Create application.
    app = QApplication(sys.argv)
    # Instantiate and show window.
    botany_guide_gui = BotanyGuideGui()
    botany_guide_gui.showMaximized()
    # Start application.
    sys.exit(app.exec())
    