"""
* gui.py
*
*  Created on: 21 dec. 2025
*      Author: Ludo
"""

import subprocess
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from .workspace import WorkspaceView
from .main_window_ui import Ui_MainWindow

### GUI class definition ###

"""
* BotanyGuideGui
* Main GUI class.
"""
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
        try:
            # Read last tag.
            tag = subprocess.check_output(["git", "describe", "--tags", "--match", "sw*", "--abbrev=0"], stderr=subprocess.DEVNULL, text=True).strip()
            # Read number of commits since last tag.
            commits_since_tag = subprocess.check_output(["git", "rev-list", "--count", f"{tag}..HEAD"], stderr=subprocess.DEVNULL, text=True).strip()
            # Read commit hash.
            commit_hash = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], stderr=subprocess.DEVNULL, text=True).strip()
            # Check dirty state.
            result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
            is_dirty = bool(result.stdout.strip())
            # Build version
            version = f"{tag}.{commits_since_tag}"
            if is_dirty:
                version += ".dev"
            version += f" - {commit_hash}"
            return version
        except subprocess.CalledProcessError:
            return "Unknown version"
            
### GUI main function ###

if __name__ == "__main__":
    # Create application.
    app = QApplication(sys.argv)
    # Instantiate and show window.
    botany_guide_gui = BotanyGuideGui()
    botany_guide_gui.showMaximized()
    # Start application.
    sys.exit(app.exec())
    