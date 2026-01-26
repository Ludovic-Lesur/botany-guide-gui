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
        self.classificationGroupBox.setMinimumSize(QSize(0, 0))
        self.classificationGroupBox.setMaximumSize(QSize(16777215, 16777215))
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
        self.speciesGroupBox.setMinimumSize(QSize(400, 0))
        self.speciesGroupBox.setMaximumSize(QSize(400, 16777215))
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

        self.speciesEditPushButton = QPushButton(self.speciesGroupBox)
        self.speciesEditPushButton.setObjectName(u"speciesEditPushButton")

        self.gridLayout_16.addWidget(self.speciesEditPushButton, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.speciesGroupBox)

        self.observationGroupBox = QGroupBox(self.centralwidget)
        self.observationGroupBox.setObjectName(u"observationGroupBox")
        self.observationGroupBox.setMinimumSize(QSize(400, 0))
        self.observationGroupBox.setMaximumSize(QSize(400, 16777215))
        self.observationGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.observationGroupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.observationAddPushButton = QPushButton(self.observationGroupBox)
        self.observationAddPushButton.setObjectName(u"observationAddPushButton")

        self.gridLayout_7.addWidget(self.observationAddPushButton, 0, 0, 1, 1)

        self.observationListGroupeBox = QGroupBox(self.observationGroupBox)
        self.observationListGroupeBox.setObjectName(u"observationListGroupeBox")
        self.gridLayout_6 = QGridLayout(self.observationListGroupeBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.observationListPreviousPushButton = QPushButton(self.observationListGroupeBox)
        self.observationListPreviousPushButton.setObjectName(u"observationListPreviousPushButton")
        self.observationListPreviousPushButton.setMinimumSize(QSize(50, 0))
        self.observationListPreviousPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_5.addWidget(self.observationListPreviousPushButton, 0, 0, 1, 1)

        self.observationDateLabel = QLabel(self.observationListGroupeBox)
        self.observationDateLabel.setObjectName(u"observationDateLabel")
        self.observationDateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.observationDateLabel, 0, 1, 1, 1)

        self.observationListNextPushButton = QPushButton(self.observationListGroupeBox)
        self.observationListNextPushButton.setObjectName(u"observationListNextPushButton")
        self.observationListNextPushButton.setMinimumSize(QSize(50, 0))
        self.observationListNextPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_5.addWidget(self.observationListNextPushButton, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.observationListGroupeBox, 1, 0, 1, 1)

        self.observationPhotosGroupBox = QGroupBox(self.observationGroupBox)
        self.observationPhotosGroupBox.setObjectName(u"observationPhotosGroupBox")
        self.gridLayout_4 = QGridLayout(self.observationPhotosGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.observationPhotosPreviousPushButton = QPushButton(self.observationPhotosGroupBox)
        self.observationPhotosPreviousPushButton.setObjectName(u"observationPhotosPreviousPushButton")
        self.observationPhotosPreviousPushButton.setMinimumSize(QSize(50, 0))
        self.observationPhotosPreviousPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.observationPhotosPreviousPushButton, 0, 0, 1, 1)

        self.observationPhotosGraphicView = QGraphicsView(self.observationPhotosGroupBox)
        self.observationPhotosGraphicView.setObjectName(u"observationPhotosGraphicView")

        self.gridLayout_3.addWidget(self.observationPhotosGraphicView, 0, 1, 1, 1)

        self.observationPhotosNextPushButton = QPushButton(self.observationPhotosGroupBox)
        self.observationPhotosNextPushButton.setObjectName(u"observationPhotosNextPushButton")
        self.observationPhotosNextPushButton.setMinimumSize(QSize(50, 0))
        self.observationPhotosNextPushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.observationPhotosNextPushButton, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.observationPhotosGroupBox, 2, 0, 1, 1)

        self.observationInfosGroupBox = QGroupBox(self.observationGroupBox)
        self.observationInfosGroupBox.setObjectName(u"observationInfosGroupBox")
        self.gridLayout_2 = QGridLayout(self.observationInfosGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.observationDescriptionContentLabel = QLabel(self.observationInfosGroupBox)
        self.observationDescriptionContentLabel.setObjectName(u"observationDescriptionContentLabel")
        self.observationDescriptionContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationDescriptionContentLabel, 4, 1, 1, 1)

        self.observationDescriptionLabel = QLabel(self.observationInfosGroupBox)
        self.observationDescriptionLabel.setObjectName(u"observationDescriptionLabel")

        self.gridLayout.addWidget(self.observationDescriptionLabel, 4, 0, 1, 1)

        self.observationDepartmentContentLabel = QLabel(self.observationInfosGroupBox)
        self.observationDepartmentContentLabel.setObjectName(u"observationDepartmentContentLabel")
        self.observationDepartmentContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationDepartmentContentLabel, 1, 1, 1, 1)

        self.observationCityContentLabel = QLabel(self.observationInfosGroupBox)
        self.observationCityContentLabel.setObjectName(u"observationCityContentLabel")
        self.observationCityContentLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.observationCityContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationCityContentLabel, 0, 1, 1, 1)

        self.observationGpsContentLabel = QLabel(self.observationInfosGroupBox)
        self.observationGpsContentLabel.setObjectName(u"observationGpsContentLabel")
        self.observationGpsContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationGpsContentLabel, 3, 1, 1, 1)

        self.observationCountryContentLabel = QLabel(self.observationInfosGroupBox)
        self.observationCountryContentLabel.setObjectName(u"observationCountryContentLabel")
        self.observationCountryContentLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.observationCountryContentLabel, 2, 1, 1, 1)

        self.observationCountryLabel = QLabel(self.observationInfosGroupBox)
        self.observationCountryLabel.setObjectName(u"observationCountryLabel")

        self.gridLayout.addWidget(self.observationCountryLabel, 2, 0, 1, 1)

        self.observationDepartmentLabel = QLabel(self.observationInfosGroupBox)
        self.observationDepartmentLabel.setObjectName(u"observationDepartmentLabel")

        self.gridLayout.addWidget(self.observationDepartmentLabel, 1, 0, 1, 1)

        self.observationGpsLabel = QLabel(self.observationInfosGroupBox)
        self.observationGpsLabel.setObjectName(u"observationGpsLabel")

        self.gridLayout.addWidget(self.observationGpsLabel, 3, 0, 1, 1)

        self.observationCityLabel = QLabel(self.observationInfosGroupBox)
        self.observationCityLabel.setObjectName(u"observationCityLabel")

        self.gridLayout.addWidget(self.observationCityLabel, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.observationInfosGroupBox, 3, 0, 1, 1)

        self.observationEditPushButton = QPushButton(self.observationGroupBox)
        self.observationEditPushButton.setObjectName(u"observationEditPushButton")

        self.gridLayout_7.addWidget(self.observationEditPushButton, 4, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.observationGroupBox)


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
        self.speciesLatinNameContentLabel.setText("")
        self.speciesCommonNameLabel.setText(QCoreApplication.translate("MainWindow", u"Nom Commun", None))
        self.speciesCommonNameContentLabel.setText("")
        self.speciesInfosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Infos", None))
        self.speciedEdibilityLabel.setText(QCoreApplication.translate("MainWindow", u"Comestibilit\u00e9", None))
        self.speciesEdibilityContentLabel.setText("")
        self.speciesReferencesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"R\u00e9f\u00e9rences", None))
        self.speciesRefGuide700PlantesContentLabel.setText("")
        self.speciesRefFlorePyreneesLabel.setText(QCoreApplication.translate("MainWindow", u"Guide Flore des Pyr\u00e9n\u00e9es", None))
        self.speciesRefFlorePyreneesContentLabel.setText("")
        self.speciesRefDelachauxArbresContentLabel.setText("")
        self.speciesRefDelachauxFleursLabel.setText(QCoreApplication.translate("MainWindow", u"Guide Delachaux des Fleurs", None))
        self.speciesRefDelachauxArbresLabel.setText(QCoreApplication.translate("MainWindow", u"Guide Delachaux des Arbres", None))
        self.speciesRefChampignonsLabel.setText(QCoreApplication.translate("MainWindow", u"Guide des Champignons", None))
        self.speciesRefDelachauxFleursContentLabel.setText("")
        self.speciesRefChampignonsContentLabel.setText("")
        self.speciesRefGuide700PlantesLabel.setText(QCoreApplication.translate("MainWindow", u"Guide 700 Plantes", None))
        self.speciesEditPushButton.setText(QCoreApplication.translate("MainWindow", u"Editer", None))
        self.observationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Observations", None))
        self.observationAddPushButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.observationListGroupeBox.setTitle(QCoreApplication.translate("MainWindow", u"Liste", None))
        self.observationListPreviousPushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.observationDateLabel.setText("")
        self.observationListNextPushButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.observationPhotosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Photos", None))
        self.observationPhotosPreviousPushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.observationPhotosNextPushButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.observationInfosGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Infos", None))
        self.observationDescriptionContentLabel.setText("")
        self.observationDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Description terrain", None))
        self.observationDepartmentContentLabel.setText("")
        self.observationCityContentLabel.setText("")
        self.observationGpsContentLabel.setText("")
        self.observationCountryContentLabel.setText("")
        self.observationCountryLabel.setText(QCoreApplication.translate("MainWindow", u"Pays", None))
        self.observationDepartmentLabel.setText(QCoreApplication.translate("MainWindow", u"D\u00e9partement", None))
        self.observationGpsLabel.setText(QCoreApplication.translate("MainWindow", u"Coordonn\u00e9es GPS", None))
        self.observationCityLabel.setText(QCoreApplication.translate("MainWindow", u"Commune", None))
        self.observationEditPushButton.setText(QCoreApplication.translate("MainWindow", u"Editer", None))
    # retranslateUi

