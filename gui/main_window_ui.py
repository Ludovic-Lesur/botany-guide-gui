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
        MainWindow.resize(1580, 638)
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
        self.classificationGroupBox.setMinimumSize(QSize(1000, 0))
        self.classificationGroupBox.setMaximumSize(QSize(1000, 16777215))
        self.classificationGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_17 = QGridLayout(self.classificationGroupBox)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.classificationAddSpeciesPushButton = QPushButton(self.classificationGroupBox)
        self.classificationAddSpeciesPushButton.setObjectName(u"classificationAddSpeciesPushButton")

        self.gridLayout_17.addWidget(self.classificationAddSpeciesPushButton, 1, 0, 1, 1)

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


        self.horizontalLayout.addWidget(self.classificationGroupBox)

        self.speciesGroupBox = QGroupBox(self.centralwidget)
        self.speciesGroupBox.setObjectName(u"speciesGroupBox")
        self.speciesGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_16 = QGridLayout(self.speciesGroupBox)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.speciesNameGroupBox = QGroupBox(self.speciesGroupBox)
        self.speciesNameGroupBox.setObjectName(u"speciesNameGroupBox")
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

        self.speciesPhotoGraphicsViews = QGraphicsView(self.speciesGroupBox)
        self.speciesPhotoGraphicsViews.setObjectName(u"speciesPhotoGraphicsViews")

        self.gridLayout_15.addWidget(self.speciesPhotoGraphicsViews, 1, 0, 1, 1)

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
        self.speciesGuide700PlantesContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesGuide700PlantesContentLabel.setObjectName(u"speciesGuide700PlantesContentLabel")
        self.speciesGuide700PlantesContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesGuide700PlantesContentLabel, 1, 1, 1, 1)

        self.speciesFlorePyreneesLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesFlorePyreneesLabel.setObjectName(u"speciesFlorePyreneesLabel")

        self.gridLayout_9.addWidget(self.speciesFlorePyreneesLabel, 2, 0, 1, 1)

        self.speciesFlorePyreneesContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesFlorePyreneesContentLabel.setObjectName(u"speciesFlorePyreneesContentLabel")
        self.speciesFlorePyreneesContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesFlorePyreneesContentLabel, 2, 1, 1, 1)

        self.speciesDelachauxTreesContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesDelachauxTreesContentLabel.setObjectName(u"speciesDelachauxTreesContentLabel")
        self.speciesDelachauxTreesContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesDelachauxTreesContentLabel, 3, 1, 1, 1)

        self.speciesDelachauxFlowersLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesDelachauxFlowersLabel.setObjectName(u"speciesDelachauxFlowersLabel")

        self.gridLayout_9.addWidget(self.speciesDelachauxFlowersLabel, 0, 0, 1, 1)

        self.speciesDelachauxTreesLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesDelachauxTreesLabel.setObjectName(u"speciesDelachauxTreesLabel")

        self.gridLayout_9.addWidget(self.speciesDelachauxTreesLabel, 3, 0, 1, 1)

        self.speciesChampignonsLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesChampignonsLabel.setObjectName(u"speciesChampignonsLabel")

        self.gridLayout_9.addWidget(self.speciesChampignonsLabel, 4, 0, 1, 1)

        self.speciesDelachauxFlowersContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesDelachauxFlowersContentLabel.setObjectName(u"speciesDelachauxFlowersContentLabel")
        self.speciesDelachauxFlowersContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesDelachauxFlowersContentLabel, 0, 1, 1, 1)

        self.speciesChampignonsContentLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesChampignonsContentLabel.setObjectName(u"speciesChampignonsContentLabel")
        self.speciesChampignonsContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.speciesChampignonsContentLabel, 4, 1, 1, 1)

        self.speciesGuide700PlantesLabel = QLabel(self.speciesReferencesGroupBox)
        self.speciesGuide700PlantesLabel.setObjectName(u"speciesGuide700PlantesLabel")

        self.gridLayout_9.addWidget(self.speciesGuide700PlantesLabel, 1, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.speciesReferencesGroupBox, 3, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.speciesEditPushButton = QPushButton(self.speciesGroupBox)
        self.speciesEditPushButton.setObjectName(u"speciesEditPushButton")

        self.gridLayout_16.addWidget(self.speciesEditPushButton, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.speciesGroupBox)

        self.observationsGroupBox = QGroupBox(self.centralwidget)
        self.observationsGroupBox.setObjectName(u"observationsGroupBox")
        self.observationsGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.observationsGroupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.observationsAddPushButton = QPushButton(self.observationsGroupBox)
        self.observationsAddPushButton.setObjectName(u"observationsAddPushButton")

        self.gridLayout_7.addWidget(self.observationsAddPushButton, 0, 0, 1, 1)

        self.observationsListGroupeBox = QGroupBox(self.observationsGroupBox)
        self.observationsListGroupeBox.setObjectName(u"observationsListGroupeBox")
        self.gridLayout_6 = QGridLayout(self.observationsListGroupeBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.observationsListPreviousPushButton = QPushButton(self.observationsListGroupeBox)
        self.observationsListPreviousPushButton.setObjectName(u"observationsListPreviousPushButton")
        self.observationsListPreviousPushButton.setMinimumSize(QSize(50, 0))
        self.observationsListPreviousPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_5.addWidget(self.observationsListPreviousPushButton, 0, 0, 1, 1)

        self.observationsDateLabel = QLabel(self.observationsListGroupeBox)
        self.observationsDateLabel.setObjectName(u"observationsDateLabel")
        self.observationsDateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.observationsDateLabel, 0, 1, 1, 1)

        self.observationsListNextPushButton = QPushButton(self.observationsListGroupeBox)
        self.observationsListNextPushButton.setObjectName(u"observationsListNextPushButton")
        self.observationsListNextPushButton.setMinimumSize(QSize(50, 0))
        self.observationsListNextPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_5.addWidget(self.observationsListNextPushButton, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.observationsListGroupeBox, 1, 0, 1, 1)

        self.observationsPhotosGroupBox = QGroupBox(self.observationsGroupBox)
        self.observationsPhotosGroupBox.setObjectName(u"observationsPhotosGroupBox")
        self.gridLayout_4 = QGridLayout(self.observationsPhotosGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.observationsPhotosPreviousPushButton = QPushButton(self.observationsPhotosGroupBox)
        self.observationsPhotosPreviousPushButton.setObjectName(u"observationsPhotosPreviousPushButton")
        self.observationsPhotosPreviousPushButton.setMinimumSize(QSize(50, 0))
        self.observationsPhotosPreviousPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.observationsPhotosPreviousPushButton, 0, 0, 1, 1)

        self.observationsPhotosGraphicView = QGraphicsView(self.observationsPhotosGroupBox)
        self.observationsPhotosGraphicView.setObjectName(u"observationsPhotosGraphicView")

        self.gridLayout_3.addWidget(self.observationsPhotosGraphicView, 0, 1, 1, 1)

        self.observationsPhotosNextPushButton = QPushButton(self.observationsPhotosGroupBox)
        self.observationsPhotosNextPushButton.setObjectName(u"observationsPhotosNextPushButton")
        self.observationsPhotosNextPushButton.setMinimumSize(QSize(50, 0))
        self.observationsPhotosNextPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.observationsPhotosNextPushButton, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.observationsPhotosGroupBox, 2, 0, 1, 1)

        self.observationsInfosGroupBox = QGroupBox(self.observationsGroupBox)
        self.observationsInfosGroupBox.setObjectName(u"observationsInfosGroupBox")
        self.gridLayout_2 = QGridLayout(self.observationsInfosGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.observationsFieldContentLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsFieldContentLabel.setObjectName(u"observationsFieldContentLabel")
        self.observationsFieldContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationsFieldContentLabel, 4, 1, 1, 1)

        self.observationsFieldLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsFieldLabel.setObjectName(u"observationsFieldLabel")

        self.gridLayout.addWidget(self.observationsFieldLabel, 4, 0, 1, 1)

        self.observationsDepartmentContentLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsDepartmentContentLabel.setObjectName(u"observationsDepartmentContentLabel")
        self.observationsDepartmentContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationsDepartmentContentLabel, 1, 1, 1, 1)

        self.observationsCityContentLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsCityContentLabel.setObjectName(u"observationsCityContentLabel")
        self.observationsCityContentLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.observationsCityContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationsCityContentLabel, 0, 1, 1, 1)

        self.observationsGpsContentLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsGpsContentLabel.setObjectName(u"observationsGpsContentLabel")
        self.observationsGpsContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationsGpsContentLabel, 3, 1, 1, 1)

        self.observationsCountryContentLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsCountryContentLabel.setObjectName(u"observationsCountryContentLabel")
        self.observationsCountryContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationsCountryContentLabel, 2, 1, 1, 1)

        self.observationsCountryLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsCountryLabel.setObjectName(u"observationsCountryLabel")

        self.gridLayout.addWidget(self.observationsCountryLabel, 2, 0, 1, 1)

        self.observationsDepartmentLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsDepartmentLabel.setObjectName(u"observationsDepartmentLabel")

        self.gridLayout.addWidget(self.observationsDepartmentLabel, 1, 0, 1, 1)

        self.observationsGpsLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsGpsLabel.setObjectName(u"observationsGpsLabel")

        self.gridLayout.addWidget(self.observationsGpsLabel, 3, 0, 1, 1)

        self.observationsCityLabel = QLabel(self.observationsInfosGroupBox)
        self.observationsCityLabel.setObjectName(u"observationsCityLabel")

        self.gridLayout.addWidget(self.observationsCityLabel, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.observationsInfosGroupBox, 3, 0, 1, 1)

        self.observationsEditPushButton = QPushButton(self.observationsGroupBox)
        self.observationsEditPushButton.setObjectName(u"observationsEditPushButton")

        self.gridLayout_7.addWidget(self.observationsEditPushButton, 4, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.observationsGroupBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_20.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Recherche", None))
        self.searchTitlelabel.setText(QCoreApplication.translate("MainWindow", u"Nom d'esp\u00e8ce", None))
        self.classificationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.classificationAddSpeciesPushButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter une esp\u00e8ce", None))
        ___qtreewidgetitem = self.classificationTreeWidget.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Esp\u00e8ce", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Famille", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Ordre", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Classe", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Division", None));
        self.speciesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Esp\u00e8ce", None))
        self.speciesNameGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Nomenclature", None))
        self.speciesLatinNameLabel.setText(QCoreApplication.translate("MainWindow", u"Nom Latin", None))
        self.speciesLatinNameContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.speciesCommonNameLabel.setText(QCoreApplication.translate("MainWindow", u"Nom Commun", None))
        self.speciesCommonNameContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.speciesInfosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Infos", None))
        self.speciedEdibilityLabel.setText(QCoreApplication.translate("MainWindow", u"Comestibilit\u00e9", None))
        self.speciesEdibilityContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.speciesReferencesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"R\u00e9f\u00e9rences", None))
        self.speciesGuide700PlantesContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.speciesFlorePyreneesLabel.setText(QCoreApplication.translate("MainWindow", u"Guide Flore des Pyr\u00e9n\u00e9es", None))
        self.speciesFlorePyreneesContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.speciesDelachauxTreesContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.speciesDelachauxFlowersLabel.setText(QCoreApplication.translate("MainWindow", u"Guide Delachaux des Fleurs", None))
        self.speciesDelachauxTreesLabel.setText(QCoreApplication.translate("MainWindow", u"Guide Delachaux des Arbres", None))
        self.speciesChampignonsLabel.setText(QCoreApplication.translate("MainWindow", u"Guide des Champignons", None))
        self.speciesDelachauxFlowersContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.speciesChampignonsContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.speciesGuide700PlantesLabel.setText(QCoreApplication.translate("MainWindow", u"Guide 700 Plantes", None))
        self.speciesEditPushButton.setText(QCoreApplication.translate("MainWindow", u"Editer", None))
        self.observationsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Observations", None))
        self.observationsAddPushButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.observationsListGroupeBox.setTitle(QCoreApplication.translate("MainWindow", u"Liste", None))
        self.observationsListPreviousPushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.observationsDateLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.observationsListNextPushButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.observationsPhotosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Photos", None))
        self.observationsPhotosPreviousPushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.observationsPhotosNextPushButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.observationsInfosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Infos", None))
        self.observationsFieldContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.observationsFieldLabel.setText(QCoreApplication.translate("MainWindow", u"Description terrain", None))
        self.observationsDepartmentContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.observationsCityContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.observationsGpsContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.observationsCountryContentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.observationsCountryLabel.setText(QCoreApplication.translate("MainWindow", u"Pays", None))
        self.observationsDepartmentLabel.setText(QCoreApplication.translate("MainWindow", u"D\u00e9partement", None))
        self.observationsGpsLabel.setText(QCoreApplication.translate("MainWindow", u"Coordonn\u00e9es GPS", None))
        self.observationsCityLabel.setText(QCoreApplication.translate("MainWindow", u"Commune", None))
        self.observationsEditPushButton.setText(QCoreApplication.translate("MainWindow", u"Editer", None))
    # retranslateUi

