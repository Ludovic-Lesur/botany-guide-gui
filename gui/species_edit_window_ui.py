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
    QFormLayout, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_SpeciesEditDialog(object):
    def setupUi(self, SpeciesEditDialog):
        if not SpeciesEditDialog.objectName():
            SpeciesEditDialog.setObjectName(u"SpeciesEditDialog")
        SpeciesEditDialog.resize(650, 500)
        font = QFont()
        font.setFamilies([u"LM Sans 12"])
        SpeciesEditDialog.setFont(font)
        self.gridLayout = QGridLayout(SpeciesEditDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.directoryLabel = QLabel(SpeciesEditDialog)
        self.directoryLabel.setObjectName(u"directoryLabel")
        self.directoryLabel.setMinimumSize(QSize(200, 0))
        self.directoryLabel.setFont(font)

        self.horizontalLayout.addWidget(self.directoryLabel)

        self.directoryContentLabel = QLabel(SpeciesEditDialog)
        self.directoryContentLabel.setObjectName(u"directoryContentLabel")
        self.directoryContentLabel.setMinimumSize(QSize(300, 90))
        self.directoryContentLabel.setMaximumSize(QSize(16777215, 90))
        self.directoryContentLabel.setFont(font)
        self.directoryContentLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.directoryContentLabel)

        self.explorerPushButton = QPushButton(SpeciesEditDialog)
        self.explorerPushButton.setObjectName(u"explorerPushButton")
        self.explorerPushButton.setFont(font)

        self.horizontalLayout.addWidget(self.explorerPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.latinNameLabel = QLabel(SpeciesEditDialog)
        self.latinNameLabel.setObjectName(u"latinNameLabel")
        self.latinNameLabel.setMinimumSize(QSize(200, 0))
        self.latinNameLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.latinNameLabel)

        self.latinNameTextEdit = QTextEdit(SpeciesEditDialog)
        self.latinNameTextEdit.setObjectName(u"latinNameTextEdit")
        self.latinNameTextEdit.setMinimumSize(QSize(300, 35))
        self.latinNameTextEdit.setMaximumSize(QSize(16777215, 35))
        self.latinNameTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.latinNameTextEdit)

        self.commonNameLabel = QLabel(SpeciesEditDialog)
        self.commonNameLabel.setObjectName(u"commonNameLabel")
        self.commonNameLabel.setMinimumSize(QSize(200, 0))
        self.commonNameLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.commonNameLabel)

        self.commonNameTextEdit = QTextEdit(SpeciesEditDialog)
        self.commonNameTextEdit.setObjectName(u"commonNameTextEdit")
        self.commonNameTextEdit.setMinimumSize(QSize(300, 35))
        self.commonNameTextEdit.setMaximumSize(QSize(16777215, 35))
        self.commonNameTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.commonNameTextEdit)

        self.edibilityLabel = QLabel(SpeciesEditDialog)
        self.edibilityLabel.setObjectName(u"edibilityLabel")
        self.edibilityLabel.setMinimumSize(QSize(200, 0))
        self.edibilityLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.edibilityLabel)

        self.edibilityTextEdit = QTextEdit(SpeciesEditDialog)
        self.edibilityTextEdit.setObjectName(u"edibilityTextEdit")
        self.edibilityTextEdit.setMinimumSize(QSize(300, 35))
        self.edibilityTextEdit.setMaximumSize(QSize(16777215, 35))
        self.edibilityTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.edibilityTextEdit)

        self.refDelachauxFleursLabel = QLabel(SpeciesEditDialog)
        self.refDelachauxFleursLabel.setObjectName(u"refDelachauxFleursLabel")
        self.refDelachauxFleursLabel.setMinimumSize(QSize(200, 0))
        self.refDelachauxFleursLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.refDelachauxFleursLabel)

        self.refDelachauxFleursTextEdit = QTextEdit(SpeciesEditDialog)
        self.refDelachauxFleursTextEdit.setObjectName(u"refDelachauxFleursTextEdit")
        self.refDelachauxFleursTextEdit.setMinimumSize(QSize(300, 35))
        self.refDelachauxFleursTextEdit.setMaximumSize(QSize(16777215, 35))
        self.refDelachauxFleursTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.refDelachauxFleursTextEdit)

        self.ref700PlantesLabel = QLabel(SpeciesEditDialog)
        self.ref700PlantesLabel.setObjectName(u"ref700PlantesLabel")
        self.ref700PlantesLabel.setMinimumSize(QSize(200, 0))
        self.ref700PlantesLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ref700PlantesLabel)

        self.ref700PlantesTextEdit = QTextEdit(SpeciesEditDialog)
        self.ref700PlantesTextEdit.setObjectName(u"ref700PlantesTextEdit")
        self.ref700PlantesTextEdit.setMinimumSize(QSize(300, 35))
        self.ref700PlantesTextEdit.setMaximumSize(QSize(16777215, 35))
        self.ref700PlantesTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.ref700PlantesTextEdit)

        self.refFlorePyreneesLabel = QLabel(SpeciesEditDialog)
        self.refFlorePyreneesLabel.setObjectName(u"refFlorePyreneesLabel")
        self.refFlorePyreneesLabel.setMinimumSize(QSize(200, 0))
        self.refFlorePyreneesLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.refFlorePyreneesLabel)

        self.refFlorePyreneesTextEdit = QTextEdit(SpeciesEditDialog)
        self.refFlorePyreneesTextEdit.setObjectName(u"refFlorePyreneesTextEdit")
        self.refFlorePyreneesTextEdit.setMinimumSize(QSize(300, 35))
        self.refFlorePyreneesTextEdit.setMaximumSize(QSize(16777215, 35))
        self.refFlorePyreneesTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.refFlorePyreneesTextEdit)

        self.refDelachauxArbresLabel = QLabel(SpeciesEditDialog)
        self.refDelachauxArbresLabel.setObjectName(u"refDelachauxArbresLabel")
        self.refDelachauxArbresLabel.setMinimumSize(QSize(200, 0))
        self.refDelachauxArbresLabel.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.refDelachauxArbresLabel)

        self.refDelachauxArbresTextEdit = QTextEdit(SpeciesEditDialog)
        self.refDelachauxArbresTextEdit.setObjectName(u"refDelachauxArbresTextEdit")
        self.refDelachauxArbresTextEdit.setMinimumSize(QSize(300, 35))
        self.refDelachauxArbresTextEdit.setMaximumSize(QSize(16777215, 35))
        self.refDelachauxArbresTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.refDelachauxArbresTextEdit)

        self.refChampignonsLabel = QLabel(SpeciesEditDialog)
        self.refChampignonsLabel.setObjectName(u"refChampignonsLabel")
        self.refChampignonsLabel.setMinimumSize(QSize(200, 0))
        self.refChampignonsLabel.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.refChampignonsLabel)

        self.refChampignonsTextEdit = QTextEdit(SpeciesEditDialog)
        self.refChampignonsTextEdit.setObjectName(u"refChampignonsTextEdit")
        self.refChampignonsTextEdit.setMinimumSize(QSize(300, 35))
        self.refChampignonsTextEdit.setMaximumSize(QSize(16777215, 35))
        self.refChampignonsTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.refChampignonsTextEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(SpeciesEditDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SpeciesEditDialog)
        self.buttonBox.accepted.connect(SpeciesEditDialog.accept)
        self.buttonBox.rejected.connect(SpeciesEditDialog.reject)

        QMetaObject.connectSlotsByName(SpeciesEditDialog)
    # setupUi

    def retranslateUi(self, SpeciesEditDialog):
        SpeciesEditDialog.setWindowTitle(QCoreApplication.translate("SpeciesEditDialog", u"Esp\u00e8ce", None))
        self.directoryLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Dossier", None))
        self.directoryContentLabel.setText("")
        self.explorerPushButton.setText(QCoreApplication.translate("SpeciesEditDialog", u"Parcourir", None))
        self.latinNameLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Nom latin", None))
        self.commonNameLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Nom commun", None))
        self.edibilityLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Comestibilit\u00e9", None))
        self.refDelachauxFleursLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Guide Delachaux des Fleurs", None))
        self.refDelachauxFleursTextEdit.setDocumentTitle("")
        self.ref700PlantesLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Guide 700 Plantes", None))
        self.ref700PlantesTextEdit.setDocumentTitle("")
        self.refFlorePyreneesLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Guide Flore des Pyr\u00e9n\u00e9es", None))
        self.refFlorePyreneesTextEdit.setDocumentTitle("")
        self.refDelachauxArbresLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Guide Delachaux des Arbres", None))
        self.refDelachauxArbresTextEdit.setDocumentTitle("")
        self.refChampignonsLabel.setText(QCoreApplication.translate("SpeciesEditDialog", u"Guide des Champignons", None))
        self.refChampignonsTextEdit.setDocumentTitle("")
    # retranslateUi

