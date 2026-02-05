# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QTextBrowser, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1580, 725)
        font = QFont()
        font.setFamilies([u"LM Sans 12"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_20 = QGridLayout(self.centralwidget)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchGroupBox = QGroupBox(self.centralwidget)
        self.searchGroupBox.setObjectName(u"searchGroupBox")
        self.searchGroupBox.setMinimumSize(QSize(80, 0))
        self.searchGroupBox.setMaximumSize(QSize(16777215, 80))
        self.searchGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_19 = QGridLayout(self.searchGroupBox)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.searchTitlelabel = QLabel(self.searchGroupBox)
        self.searchTitlelabel.setObjectName(u"searchTitlelabel")
        font1 = QFont()
        font1.setFamilies([u"LM Sans 12"])
        font1.setBold(True)
        self.searchTitlelabel.setFont(font1)

        self.gridLayout_18.addWidget(self.searchTitlelabel, 0, 0, 1, 1)

        self.searchTextBrowser = QTextBrowser(self.searchGroupBox)
        self.searchTextBrowser.setObjectName(u"searchTextBrowser")

        self.gridLayout_18.addWidget(self.searchTextBrowser, 0, 1, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.searchGroupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.classificationGroupBox = QGroupBox(self.centralwidget)
        self.classificationGroupBox.setObjectName(u"classificationGroupBox")
        self.classificationGroupBox.setMinimumSize(QSize(0, 0))
        self.classificationGroupBox.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"LM Sans 12"])
        font2.setBold(False)
        self.classificationGroupBox.setFont(font2)
        self.classificationGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_17 = QGridLayout(self.classificationGroupBox)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.classificationTreeWidget = QTreeWidget(self.classificationGroupBox)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"R\u00e8gne");
        self.classificationTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.classificationTreeWidget.setObjectName(u"classificationTreeWidget")
        self.classificationTreeWidget.setAutoFillBackground(False)
        self.classificationTreeWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.classificationTreeWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.classificationTreeWidget.setLineWidth(1)
        self.classificationTreeWidget.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.classificationTreeWidget.setIndentation(0)
        self.classificationTreeWidget.setSortingEnabled(False)
        self.classificationTreeWidget.setWordWrap(True)
        self.classificationTreeWidget.setColumnCount(7)
        self.classificationTreeWidget.setSupportedDragActions(Qt.DropAction.IgnoreAction)
        self.classificationTreeWidget.header().setCascadingSectionResizes(False)
        self.classificationTreeWidget.header().setMinimumSectionSize(100)
        self.classificationTreeWidget.header().setProperty(u"showSortIndicator", False)
        self.classificationTreeWidget.header().setStretchLastSection(True)

        self.gridLayout_17.addWidget(self.classificationTreeWidget, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.classificationAddSpeciesPushButton = QPushButton(self.classificationGroupBox)
        self.classificationAddSpeciesPushButton.setObjectName(u"classificationAddSpeciesPushButton")

        self.horizontalLayout_3.addWidget(self.classificationAddSpeciesPushButton)

        self.classificationRefreshPushButton = QPushButton(self.classificationGroupBox)
        self.classificationRefreshPushButton.setObjectName(u"classificationRefreshPushButton")

        self.horizontalLayout_3.addWidget(self.classificationRefreshPushButton)


        self.gridLayout_17.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.classificationGroupBox)

        self.speciesGroupBox = QGroupBox(self.centralwidget)
        self.speciesGroupBox.setObjectName(u"speciesGroupBox")
        self.speciesGroupBox.setMinimumSize(QSize(400, 0))
        self.speciesGroupBox.setMaximumSize(QSize(400, 16777215))
        font3 = QFont()
        font3.setFamilies([u"LM Sans 12"])
        font3.setItalic(False)
        self.speciesGroupBox.setFont(font3)
        self.speciesGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_16 = QGridLayout(self.speciesGroupBox)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.speciesNameGroupBox = QGroupBox(self.speciesGroupBox)
        self.speciesNameGroupBox.setObjectName(u"speciesNameGroupBox")
        font4 = QFont()
        font4.setFamilies([u"LM Sans 12"])
        font4.setBold(False)
        font4.setItalic(False)
        self.speciesNameGroupBox.setFont(font4)
        self.gridLayout_14 = QGridLayout(self.speciesNameGroupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.speciesLatinNameLabel = QLabel(self.speciesNameGroupBox)
        self.speciesLatinNameLabel.setObjectName(u"speciesLatinNameLabel")

        self.gridLayout_13.addWidget(self.speciesLatinNameLabel, 0, 0, 1, 1)

        self.speciesLatinNameContentLabel = QLabel(self.speciesNameGroupBox)
        self.speciesLatinNameContentLabel.setObjectName(u"speciesLatinNameContentLabel")
        self.speciesLatinNameContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_13.addWidget(self.speciesLatinNameContentLabel, 0, 1, 1, 1)

        self.speciesCommonNameLabel = QLabel(self.speciesNameGroupBox)
        self.speciesCommonNameLabel.setObjectName(u"speciesCommonNameLabel")

        self.gridLayout_13.addWidget(self.speciesCommonNameLabel, 1, 0, 1, 1)

        self.speciesCommonNameContentLabel = QLabel(self.speciesNameGroupBox)
        self.speciesCommonNameContentLabel.setObjectName(u"speciesCommonNameContentLabel")
        self.speciesCommonNameContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_13.addWidget(self.speciesCommonNameContentLabel, 1, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.speciesNameGroupBox, 0, 0, 1, 1)

        self.speciesPhotoGraphicsView = QGraphicsView(self.speciesGroupBox)
        self.speciesPhotoGraphicsView.setObjectName(u"speciesPhotoGraphicsView")
        self.speciesPhotoGraphicsView.setFrameShape(QFrame.Shape.Panel)
        self.speciesPhotoGraphicsView.setInteractive(False)
        self.speciesPhotoGraphicsView.setRenderHints(QPainter.RenderHint.LosslessImageRendering|QPainter.RenderHint.SmoothPixmapTransform|QPainter.RenderHint.TextAntialiasing)
        self.speciesPhotoGraphicsView.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)

        self.gridLayout_15.addWidget(self.speciesPhotoGraphicsView, 1, 0, 1, 1)

        self.speciesInfosGroupBox = QGroupBox(self.speciesGroupBox)
        self.speciesInfosGroupBox.setObjectName(u"speciesInfosGroupBox")
        self.gridLayout_11 = QGridLayout(self.speciesInfosGroupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.speciedEdibilityLabel = QLabel(self.speciesInfosGroupBox)
        self.speciedEdibilityLabel.setObjectName(u"speciedEdibilityLabel")

        self.gridLayout_10.addWidget(self.speciedEdibilityLabel, 0, 0, 1, 1)

        self.speciesEdibilityContentLabel = QLabel(self.speciesInfosGroupBox)
        self.speciesEdibilityContentLabel.setObjectName(u"speciesEdibilityContentLabel")
        self.speciesEdibilityContentLabel.setMinimumSize(QSize(0, 50))
        self.speciesEdibilityContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_10.addWidget(self.speciesEdibilityContentLabel, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.speciesInfosGroupBox, 2, 0, 1, 1)

        self.speciesReferencesGroupBox = QGroupBox(self.speciesGroupBox)
        self.speciesReferencesGroupBox.setObjectName(u"speciesReferencesGroupBox")
        self.gridLayout_12 = QGridLayout(self.speciesReferencesGroupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.speciesRefGuide700PlantesContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefGuide700PlantesContentLabel.setObjectName(u"speciesRefGuide700PlantesContentLabel")
        self.speciesRefGuide700PlantesContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesRefGuide700PlantesContentLabel, 1, 1, 1, 1)

        self.speciesRefFlorePyreneesLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefFlorePyreneesLabel.setObjectName(u"speciesRefFlorePyreneesLabel")

        self.gridLayout_9.addWidget(self.speciesRefFlorePyreneesLabel, 2, 0, 1, 1)

        self.speciesRefFlorePyreneesContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefFlorePyreneesContentLabel.setObjectName(u"speciesRefFlorePyreneesContentLabel")
        self.speciesRefFlorePyreneesContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesRefFlorePyreneesContentLabel, 2, 1, 1, 1)

        self.speciesRefDelachauxArbresContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefDelachauxArbresContentLabel.setObjectName(u"speciesRefDelachauxArbresContentLabel")
        self.speciesRefDelachauxArbresContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesRefDelachauxArbresContentLabel, 3, 1, 1, 1)

        self.speciesRefDelachauxFleursLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefDelachauxFleursLabel.setObjectName(u"speciesRefDelachauxFleursLabel")

        self.gridLayout_9.addWidget(self.speciesRefDelachauxFleursLabel, 0, 0, 1, 1)

        self.speciesRefDelachauxArbresLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefDelachauxArbresLabel.setObjectName(u"speciesRefDelachauxArbresLabel")

        self.gridLayout_9.addWidget(self.speciesRefDelachauxArbresLabel, 3, 0, 1, 1)

        self.speciesRefChampignonsLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefChampignonsLabel.setObjectName(u"speciesRefChampignonsLabel")

        self.gridLayout_9.addWidget(self.speciesRefChampignonsLabel, 4, 0, 1, 1)

        self.speciesRefDelachauxFleursContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefDelachauxFleursContentLabel.setObjectName(u"speciesRefDelachauxFleursContentLabel")
        self.speciesRefDelachauxFleursContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesRefDelachauxFleursContentLabel, 0, 1, 1, 1)

        self.speciesRefChampignonsContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefChampignonsContentLabel.setObjectName(u"speciesRefChampignonsContentLabel")
        self.speciesRefChampignonsContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesRefChampignonsContentLabel, 4, 1, 1, 1)

        self.speciesRefGuide700PlantesLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesRefGuide700PlantesLabel.setObjectName(u"speciesRefGuide700PlantesLabel")

        self.gridLayout_9.addWidget(self.speciesRefGuide700PlantesLabel, 1, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.speciesReferencesGroupBox, 3, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.speciesOpenDirectoryPushButton = QPushButton(self.speciesGroupBox)
        self.speciesOpenDirectoryPushButton.setObjectName(u"speciesOpenDirectoryPushButton")

        self.horizontalLayout_2.addWidget(self.speciesOpenDirectoryPushButton)

        self.speciesEditPushButton = QPushButton(self.speciesGroupBox)
        self.speciesEditPushButton.setObjectName(u"speciesEditPushButton")

        self.horizontalLayout_2.addWidget(self.speciesEditPushButton)


        self.gridLayout_16.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.speciesGroupBox)

        self.identificationGroupBox = QGroupBox(self.centralwidget)
        self.identificationGroupBox.setObjectName(u"identificationGroupBox")
        self.identificationGroupBox.setMinimumSize(QSize(400, 0))
        self.identificationGroupBox.setMaximumSize(QSize(400, 16777215))
        self.identificationGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.identificationGroupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.identificationAddPushButton = QPushButton(self.identificationGroupBox)
        self.identificationAddPushButton.setObjectName(u"identificationAddPushButton")

        self.gridLayout_7.addWidget(self.identificationAddPushButton, 0, 0, 1, 1)

        self.identificationInfosGroupBox = QGroupBox(self.identificationGroupBox)
        self.identificationInfosGroupBox.setObjectName(u"identificationInfosGroupBox")
        self.identificationInfosGroupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.identificationInfosGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.identificationGpsLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationGpsLabel.setObjectName(u"identificationGpsLabel")

        self.gridLayout.addWidget(self.identificationGpsLabel, 3, 0, 1, 1)

        self.identificationCityLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationCityLabel.setObjectName(u"identificationCityLabel")

        self.gridLayout.addWidget(self.identificationCityLabel, 0, 0, 1, 1)

        self.identificationDepartmentContentLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationDepartmentContentLabel.setObjectName(u"identificationDepartmentContentLabel")
        self.identificationDepartmentContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.identificationDepartmentContentLabel, 1, 1, 1, 1)

        self.identificationCountryLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationCountryLabel.setObjectName(u"identificationCountryLabel")

        self.gridLayout.addWidget(self.identificationCountryLabel, 2, 0, 1, 1)

        self.identificationCountryContentLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationCountryContentLabel.setObjectName(u"identificationCountryContentLabel")
        self.identificationCountryContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.identificationCountryContentLabel, 2, 1, 1, 1)

        self.identificationGpsContentLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationGpsContentLabel.setObjectName(u"identificationGpsContentLabel")
        self.identificationGpsContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.identificationGpsContentLabel, 3, 1, 1, 1)

        self.identificationDepartmentLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationDepartmentLabel.setObjectName(u"identificationDepartmentLabel")

        self.gridLayout.addWidget(self.identificationDepartmentLabel, 1, 0, 1, 1)

        self.identificationCityContentLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationCityContentLabel.setObjectName(u"identificationCityContentLabel")
        self.identificationCityContentLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.identificationCityContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.identificationCityContentLabel, 0, 1, 1, 1)

        self.identificationDescriptionLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationDescriptionLabel.setObjectName(u"identificationDescriptionLabel")

        self.gridLayout.addWidget(self.identificationDescriptionLabel, 4, 0, 1, 1)

        self.identificationDescriptionContentLabel = QLabel(self.identificationInfosGroupBox)
        self.identificationDescriptionContentLabel.setObjectName(u"identificationDescriptionContentLabel")
        self.identificationDescriptionContentLabel.setMinimumSize(QSize(0, 117))
        self.identificationDescriptionContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.identificationDescriptionContentLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.identificationDescriptionContentLabel, 4, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.identificationInfosGroupBox, 3, 0, 1, 1)

        self.identificationEditPushButton = QPushButton(self.identificationGroupBox)
        self.identificationEditPushButton.setObjectName(u"identificationEditPushButton")

        self.gridLayout_7.addWidget(self.identificationEditPushButton, 4, 0, 1, 1)

        self.identificationListGroupBox = QGroupBox(self.identificationGroupBox)
        self.identificationListGroupBox.setObjectName(u"identificationListGroupBox")
        self.identificationListGroupBox.setFont(font)
        self.gridLayout_6 = QGridLayout(self.identificationListGroupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.identificationListPreviousPushButton = QPushButton(self.identificationListGroupBox)
        self.identificationListPreviousPushButton.setObjectName(u"identificationListPreviousPushButton")
        self.identificationListPreviousPushButton.setMinimumSize(QSize(50, 0))
        self.identificationListPreviousPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_5.addWidget(self.identificationListPreviousPushButton, 0, 0, 1, 1)

        self.identificationDateLabel = QLabel(self.identificationListGroupBox)
        self.identificationDateLabel.setObjectName(u"identificationDateLabel")
        self.identificationDateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.identificationDateLabel, 0, 1, 1, 1)

        self.identificationListNextPushButton = QPushButton(self.identificationListGroupBox)
        self.identificationListNextPushButton.setObjectName(u"identificationListNextPushButton")
        self.identificationListNextPushButton.setMinimumSize(QSize(50, 0))
        self.identificationListNextPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_5.addWidget(self.identificationListNextPushButton, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.identificationListGroupBox, 1, 0, 1, 1)

        self.identificationPhotosGroupBox = QGroupBox(self.identificationGroupBox)
        self.identificationPhotosGroupBox.setObjectName(u"identificationPhotosGroupBox")
        self.identificationPhotosGroupBox.setFont(font)
        self.gridLayout_4 = QGridLayout(self.identificationPhotosGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.identificationPhotosPreviousPushButton = QPushButton(self.identificationPhotosGroupBox)
        self.identificationPhotosPreviousPushButton.setObjectName(u"identificationPhotosPreviousPushButton")
        self.identificationPhotosPreviousPushButton.setMinimumSize(QSize(50, 0))
        self.identificationPhotosPreviousPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.identificationPhotosPreviousPushButton, 0, 0, 1, 1)

        self.identificationPhotosGraphicsView = QGraphicsView(self.identificationPhotosGroupBox)
        self.identificationPhotosGraphicsView.setObjectName(u"identificationPhotosGraphicsView")

        self.gridLayout_3.addWidget(self.identificationPhotosGraphicsView, 0, 1, 1, 1)

        self.identificationPhotosNextPushButton = QPushButton(self.identificationPhotosGroupBox)
        self.identificationPhotosNextPushButton.setObjectName(u"identificationPhotosNextPushButton")
        self.identificationPhotosNextPushButton.setMinimumSize(QSize(50, 0))
        self.identificationPhotosNextPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.identificationPhotosNextPushButton, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.identificationPhotosGroupBox, 2, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.identificationGroupBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_20.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"RECHERCHE", None))
        self.searchTitlelabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#c01c28;\">Nom d'esp\u00e8ce</span></p></body></html>", None))
        self.classificationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"CLASSIFICATION", None))
        ___qtreewidgetitem = self.classificationTreeWidget.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Esp\u00e8ce", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Famille", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Ordre", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Classe", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Division", None));
        self.classificationAddSpeciesPushButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter une esp\u00e8ce", None))
        self.classificationRefreshPushButton.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.speciesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"ESP\u00c8CE", None))
        self.speciesNameGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Nomenclature", None))
        self.speciesLatinNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#26a269;\">Nom latin</span></p></body></html>", None))
        self.speciesLatinNameContentLabel.setText("")
        self.speciesCommonNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#26a269;\">Nom commun</span></p></body></html>", None))
        self.speciesCommonNameContentLabel.setText("")
        self.speciesInfosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Infos", None))
        self.speciedEdibilityLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#e5a50a;\">Comestibilit\u00e9</span></p></body></html>", None))
        self.speciesEdibilityContentLabel.setText("")
        self.speciesReferencesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"R\u00e9f\u00e9rences", None))
        self.speciesRefGuide700PlantesContentLabel.setText("")
        self.speciesRefFlorePyreneesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#3584e4;\">Guide Flore des Pyr\u00e9n\u00e9es</span></p></body></html>", None))
        self.speciesRefFlorePyreneesContentLabel.setText("")
        self.speciesRefDelachauxArbresContentLabel.setText("")
        self.speciesRefDelachauxFleursLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#3584e4;\">Guide Delachaux des Fleurs</span></p></body></html>", None))
        self.speciesRefDelachauxArbresLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#3584e4;\">Guide Delachaux des Arbres</span></p></body></html>", None))
        self.speciesRefChampignonsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#3584e4;\">Guide des Champignons</span></p></body></html>", None))
        self.speciesRefDelachauxFleursContentLabel.setText("")
        self.speciesRefChampignonsContentLabel.setText("")
        self.speciesRefGuide700PlantesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#3584e4;\">Guide 700 Plantes</span></p></body></html>", None))
        self.speciesOpenDirectoryPushButton.setText(QCoreApplication.translate("MainWindow", u"Ouvrir dossier", None))
        self.speciesEditPushButton.setText(QCoreApplication.translate("MainWindow", u"Editer", None))
        self.identificationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"IDENTIFICATIONS", None))
        self.identificationAddPushButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.identificationInfosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Infos", None))
        self.identificationGpsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#9141ac;\">Coordonn\u00e9es GPS</span></p></body></html>", None))
        self.identificationCityLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#9141ac;\">Commune</span></p></body></html>", None))
        self.identificationDepartmentContentLabel.setText("")
        self.identificationCountryLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#9141ac;\">Pays</span></p></body></html>", None))
        self.identificationCountryContentLabel.setText("")
        self.identificationGpsContentLabel.setText("")
        self.identificationDepartmentLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#9141ac;\">D\u00e9partement</span></p></body></html>", None))
        self.identificationCityContentLabel.setText("")
        self.identificationDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#9141ac;\">Description terrain</span></p></body></html>", None))
        self.identificationDescriptionContentLabel.setText("")
        self.identificationEditPushButton.setText(QCoreApplication.translate("MainWindow", u"Editer", None))
        self.identificationListGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Liste", None))
        self.identificationListPreviousPushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.identificationDateLabel.setText("")
        self.identificationListNextPushButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.identificationPhotosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Photos", None))
        self.identificationPhotosPreviousPushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.identificationPhotosNextPushButton.setText(QCoreApplication.translate("MainWindow", u">", None))
    # retranslateUi

