# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'species_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QLabel, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_SpeciesEditWindow(object):
    def setupUi(self, SpeciesEditWindow):
        if not SpeciesEditWindow.objectName():
            SpeciesEditWindow.setObjectName(u"SpeciesEditWindow")
        SpeciesEditWindow.resize(518, 472)
        self.gridLayout = QGridLayout(SpeciesEditWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.speciesFormLayout = QFormLayout()
        self.speciesFormLayout.setObjectName(u"speciesFormLayout")
        self.latinNameLabel = QLabel(SpeciesEditWindow)
        self.latinNameLabel.setObjectName(u"latinNameLabel")

        self.speciesFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.latinNameLabel)

        self.latinNameTextEdit = QTextEdit(SpeciesEditWindow)
        self.latinNameTextEdit.setObjectName(u"latinNameTextEdit")
        self.latinNameTextEdit.setMinimumSize(QSize(300, 0))
        self.latinNameTextEdit.setMaximumSize(QSize(16777215, 30))

        self.speciesFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.latinNameTextEdit)

        self.commonNameLabel = QLabel(SpeciesEditWindow)
        self.commonNameLabel.setObjectName(u"commonNameLabel")

        self.speciesFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.commonNameLabel)

        self.commonNameTextEdit = QTextEdit(SpeciesEditWindow)
        self.commonNameTextEdit.setObjectName(u"commonNameTextEdit")
        self.commonNameTextEdit.setMinimumSize(QSize(300, 0))
        self.commonNameTextEdit.setMaximumSize(QSize(16777215, 30))

        self.speciesFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.commonNameTextEdit)

        self.edibilityLabel = QLabel(SpeciesEditWindow)
        self.edibilityLabel.setObjectName(u"edibilityLabel")

        self.speciesFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.edibilityLabel)

        self.edibilityTextEdit = QTextEdit(SpeciesEditWindow)
        self.edibilityTextEdit.setObjectName(u"edibilityTextEdit")
        self.edibilityTextEdit.setMinimumSize(QSize(300, 0))
        self.edibilityTextEdit.setMaximumSize(QSize(16777215, 30))

        self.speciesFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.edibilityTextEdit)

        self.refDelachauxFleursLabel = QLabel(SpeciesEditWindow)
        self.refDelachauxFleursLabel.setObjectName(u"refDelachauxFleursLabel")

        self.speciesFormLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.refDelachauxFleursLabel)

        self.refDelachauxFleursTextEdit = QTextEdit(SpeciesEditWindow)
        self.refDelachauxFleursTextEdit.setObjectName(u"refDelachauxFleursTextEdit")
        self.refDelachauxFleursTextEdit.setMinimumSize(QSize(300, 0))
        self.refDelachauxFleursTextEdit.setMaximumSize(QSize(16777215, 30))

        self.speciesFormLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.refDelachauxFleursTextEdit)

        self.ref700PlantesLabel = QLabel(SpeciesEditWindow)
        self.ref700PlantesLabel.setObjectName(u"ref700PlantesLabel")

        self.speciesFormLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ref700PlantesLabel)

        self.ref700PlantesTextEdit = QTextEdit(SpeciesEditWindow)
        self.ref700PlantesTextEdit.setObjectName(u"ref700PlantesTextEdit")
        self.ref700PlantesTextEdit.setMinimumSize(QSize(300, 0))
        self.ref700PlantesTextEdit.setMaximumSize(QSize(16777215, 30))

        self.speciesFormLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.ref700PlantesTextEdit)

        self.refFlorePyreneesLabel = QLabel(SpeciesEditWindow)
        self.refFlorePyreneesLabel.setObjectName(u"refFlorePyreneesLabel")

        self.speciesFormLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.refFlorePyreneesLabel)

        self.refFlorePyreneesTextEdit = QTextEdit(SpeciesEditWindow)
        self.refFlorePyreneesTextEdit.setObjectName(u"refFlorePyreneesTextEdit")
        self.refFlorePyreneesTextEdit.setMinimumSize(QSize(300, 0))
        self.refFlorePyreneesTextEdit.setMaximumSize(QSize(16777215, 30))

        self.speciesFormLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.refFlorePyreneesTextEdit)

        self.refDelachauxArbresLabel = QLabel(SpeciesEditWindow)
        self.refDelachauxArbresLabel.setObjectName(u"refDelachauxArbresLabel")

        self.speciesFormLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.refDelachauxArbresLabel)

        self.refDelachauxArbresTextEdit = QTextEdit(SpeciesEditWindow)
        self.refDelachauxArbresTextEdit.setObjectName(u"refDelachauxArbresTextEdit")
        self.refDelachauxArbresTextEdit.setMinimumSize(QSize(300, 0))
        self.refDelachauxArbresTextEdit.setMaximumSize(QSize(16777215, 30))

        self.speciesFormLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.refDelachauxArbresTextEdit)

        self.refChampignonsLabel = QLabel(SpeciesEditWindow)
        self.refChampignonsLabel.setObjectName(u"refChampignonsLabel")

        self.speciesFormLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.refChampignonsLabel)

        self.refChampignonsTextEdit = QTextEdit(SpeciesEditWindow)
        self.refChampignonsTextEdit.setObjectName(u"refChampignonsTextEdit")
        self.refChampignonsTextEdit.setMinimumSize(QSize(300, 0))
        self.refChampignonsTextEdit.setMaximumSize(QSize(16777215, 30))

        self.speciesFormLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.refChampignonsTextEdit)


        self.verticalLayout.addLayout(self.speciesFormLayout)

        self.buttonBox = QDialogButtonBox(SpeciesEditWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SpeciesEditWindow)
        self.buttonBox.accepted.connect(SpeciesEditWindow.accept)
        self.buttonBox.rejected.connect(SpeciesEditWindow.reject)

        QMetaObject.connectSlotsByName(SpeciesEditWindow)
    # setupUi

    def retranslateUi(self, SpeciesEditWindow):
        SpeciesEditWindow.setWindowTitle(QCoreApplication.translate("SpeciesEditWindow", u"Esp\u00e8ce", None))
        self.latinNameLabel.setText(QCoreApplication.translate("SpeciesEditWindow", u"Nom latin", None))
        self.commonNameLabel.setText(QCoreApplication.translate("SpeciesEditWindow", u"Nom commun", None))
        self.edibilityLabel.setText(QCoreApplication.translate("SpeciesEditWindow", u"Comestibilit\u00e9", None))
        self.refDelachauxFleursLabel.setText(QCoreApplication.translate("SpeciesEditWindow", u"Guide Delachaux des Fleurs", None))
        self.refDelachauxFleursTextEdit.setDocumentTitle("")
        self.ref700PlantesLabel.setText(QCoreApplication.translate("SpeciesEditWindow", u"Guide 700 Plantes", None))
        self.ref700PlantesTextEdit.setDocumentTitle("")
        self.refFlorePyreneesLabel.setText(QCoreApplication.translate("SpeciesEditWindow", u"Guide Flore des Pyr\u00e9n\u00e9es", None))
        self.refFlorePyreneesTextEdit.setDocumentTitle("")
        self.refDelachauxArbresLabel.setText(QCoreApplication.translate("SpeciesEditWindow", u"Guide Delachaux des Arbres", None))
        self.refDelachauxArbresTextEdit.setDocumentTitle("")
        self.refChampignonsLabel.setText(QCoreApplication.translate("SpeciesEditWindow", u"Guide des Champignons", None))
        self.refChampignonsTextEdit.setDocumentTitle("")
    # retranslateUi

