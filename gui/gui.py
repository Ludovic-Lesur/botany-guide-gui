"""
* gui.py
*
*  Created on: 21 dec. 2025
*      Author: Ludo
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel
from main_window_ui import Ui_MainWindow

### GUI macros ###

GUI_DATA_PATH = './data'

### GUI class definition ###

class BotanyGuideGui(QMainWindow, Ui_MainWindow):
    # Constructor.
    def __init__(self):
        # Init parent.
        super().__init__()
        # Window properties.
        self.setupUi(self)
        self.setWindowTitle("Botany Guide GUI")
        # Setup tree view.
        model = QFileSystemModel()
        model.setRootPath(GUI_DATA_PATH)
        self.classificationTreeView.setModel(model)
        self.classificationTreeView.setRootIndex(model.index(GUI_DATA_PATH))
        for column_idx in range(1, self.classificationTreeView.model().columnCount()):
            self.classificationTreeView.header().hideSection(column_idx)
            
### GUI main function ###

if __name__ == "__main__":
    # Create application.
    app = QApplication(sys.argv)
    # Instantiate and show window.
    botanyGuideGui = BotanyGuideGui()
    botanyGuideGui.show()
    # Start application.
    sys.exit(app.exec())