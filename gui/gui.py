"""
* gui.py
*
*  Created on: 21 dec. 2025
*      Author: Ludo
"""

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
        self.setWindowTitle("Botany Guide GUI")
        # Setup tree view.
        self._workspace = WorkspaceView(self)
            
### GUI main function ###

if __name__ == "__main__":
    # Create application.
    app = QApplication(sys.argv)
    # Instantiate and show window.
    botany_guide_gui = BotanyGuideGui()
    botany_guide_gui.showMaximized()
    # Start application.
    sys.exit(app.exec())
    