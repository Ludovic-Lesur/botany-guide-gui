# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'identification_edit_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QLabel,
    QSizePolicy, QTextEdit, QWidget)

class Ui_IdentificationEditDialog(object):
    def setupUi(self, IdentificationEditDialog):
        if not IdentificationEditDialog.objectName():
            IdentificationEditDialog.setObjectName(u"IdentificationEditDialog")
        IdentificationEditDialog.resize(500, 500)
        self.gridLayout = QGridLayout(IdentificationEditDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.dateLabel = QLabel(IdentificationEditDialog)
        self.dateLabel.setObjectName(u"dateLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.dateLabel)

        self.dateEdit = QDateEdit(IdentificationEditDialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(300, 30))
        self.dateEdit.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dateEdit)

        self.cityLabel = QLabel(IdentificationEditDialog)
        self.cityLabel.setObjectName(u"cityLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.cityLabel)

        self.cityTextEdit = QTextEdit(IdentificationEditDialog)
        self.cityTextEdit.setObjectName(u"cityTextEdit")
        self.cityTextEdit.setMinimumSize(QSize(300, 30))
        self.cityTextEdit.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cityTextEdit)

        self.departmentLabel = QLabel(IdentificationEditDialog)
        self.departmentLabel.setObjectName(u"departmentLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.departmentLabel)

        self.departmentTextEdit = QTextEdit(IdentificationEditDialog)
        self.departmentTextEdit.setObjectName(u"departmentTextEdit")
        self.departmentTextEdit.setMinimumSize(QSize(300, 30))
        self.departmentTextEdit.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.departmentTextEdit)

        self.countryLabel = QLabel(IdentificationEditDialog)
        self.countryLabel.setObjectName(u"countryLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.countryLabel)

        self.countryTextEdit = QTextEdit(IdentificationEditDialog)
        self.countryTextEdit.setObjectName(u"countryTextEdit")
        self.countryTextEdit.setMinimumSize(QSize(300, 30))
        self.countryTextEdit.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.countryTextEdit)

        self.latitudeLabel = QLabel(IdentificationEditDialog)
        self.latitudeLabel.setObjectName(u"latitudeLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.latitudeLabel)

        self.latitudeTextEdit = QTextEdit(IdentificationEditDialog)
        self.latitudeTextEdit.setObjectName(u"latitudeTextEdit")
        self.latitudeTextEdit.setMinimumSize(QSize(300, 30))
        self.latitudeTextEdit.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.latitudeTextEdit)

        self.longitudeLabel = QLabel(IdentificationEditDialog)
        self.longitudeLabel.setObjectName(u"longitudeLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.longitudeLabel)

        self.longitudeTextEdit = QTextEdit(IdentificationEditDialog)
        self.longitudeTextEdit.setObjectName(u"longitudeTextEdit")
        self.longitudeTextEdit.setMinimumSize(QSize(300, 30))
        self.longitudeTextEdit.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.longitudeTextEdit)

        self.altitudeLabel = QLabel(IdentificationEditDialog)
        self.altitudeLabel.setObjectName(u"altitudeLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.altitudeLabel)

        self.altitudeTextEdit = QTextEdit(IdentificationEditDialog)
        self.altitudeTextEdit.setObjectName(u"altitudeTextEdit")
        self.altitudeTextEdit.setMinimumSize(QSize(300, 30))
        self.altitudeTextEdit.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.altitudeTextEdit)

        self.descriptionLabel = QLabel(IdentificationEditDialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.descriptionLabel)

        self.descriptionTextEdit = QTextEdit(IdentificationEditDialog)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setMinimumSize(QSize(300, 150))
        self.descriptionTextEdit.setMaximumSize(QSize(16777215, 150))

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.descriptionTextEdit)

        self.buttonBox = QDialogButtonBox(IdentificationEditDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.SpanningRole, self.buttonBox)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.retranslateUi(IdentificationEditDialog)
        self.buttonBox.accepted.connect(IdentificationEditDialog.accept)
        self.buttonBox.rejected.connect(IdentificationEditDialog.reject)

        QMetaObject.connectSlotsByName(IdentificationEditDialog)
    # setupUi

    def retranslateUi(self, IdentificationEditDialog):
        IdentificationEditDialog.setWindowTitle(QCoreApplication.translate("IdentificationEditDialog", u"Identification", None))
        self.dateLabel.setText(QCoreApplication.translate("IdentificationEditDialog", u"Date", None))
        self.cityLabel.setText(QCoreApplication.translate("IdentificationEditDialog", u"Commune", None))
        self.departmentLabel.setText(QCoreApplication.translate("IdentificationEditDialog", u"D\u00e9partement", None))
        self.countryLabel.setText(QCoreApplication.translate("IdentificationEditDialog", u"Pays", None))
        self.latitudeLabel.setText(QCoreApplication.translate("IdentificationEditDialog", u"Latitude (\u00b0)", None))
        self.longitudeLabel.setText(QCoreApplication.translate("IdentificationEditDialog", u"Longitude (\u00b0)", None))
        self.altitudeLabel.setText(QCoreApplication.translate("IdentificationEditDialog", u"Altitude (m)", None))
        self.descriptionLabel.setText(QCoreApplication.translate("IdentificationEditDialog", u"Description terrain", None))
    # retranslateUi

