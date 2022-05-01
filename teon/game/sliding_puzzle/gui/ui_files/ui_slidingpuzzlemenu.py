# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slidingpuzzlemenu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SlidingPuzzleMenu(object):
    def setupUi(self, SlidingPuzzleMenu):
        if not SlidingPuzzleMenu.objectName():
            SlidingPuzzleMenu.setObjectName(u"SlidingPuzzleMenu")
        SlidingPuzzleMenu.resize(447, 423)
        self.verticalLayout_2 = QVBoxLayout(SlidingPuzzleMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.g_view = QGraphicsView(SlidingPuzzleMenu)
        self.g_view.setObjectName(u"g_view")

        self.horizontalLayout_2.addWidget(self.g_view)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(SlidingPuzzleMenu)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.groupBox = QGroupBox(SlidingPuzzleMenu)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_3.addWidget(self.radioButton)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(SlidingPuzzleMenu)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_4.addWidget(self.radioButton_5)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_4.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_4.addWidget(self.radioButton_4)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_undo = QPushButton(SlidingPuzzleMenu)
        self.btn_undo.setObjectName(u"btn_undo")

        self.horizontalLayout.addWidget(self.btn_undo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_solve = QPushButton(SlidingPuzzleMenu)
        self.btn_solve.setObjectName(u"btn_solve")

        self.horizontalLayout.addWidget(self.btn_solve)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_show_solution = QPushButton(SlidingPuzzleMenu)
        self.btn_show_solution.setObjectName(u"btn_show_solution")

        self.horizontalLayout.addWidget(self.btn_show_solution)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(SlidingPuzzleMenu)

        QMetaObject.connectSlotsByName(SlidingPuzzleMenu)
    # setupUi

    def retranslateUi(self, SlidingPuzzleMenu):
        SlidingPuzzleMenu.setWindowTitle(QCoreApplication.translate("SlidingPuzzleMenu", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("SlidingPuzzleMenu", u"Heuristic", None))
        self.radioButton_2.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Man Hattan", None))
        self.radioButton.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Misplaced Tiles", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SlidingPuzzleMenu", u"Search Type", None))
        self.radioButton_5.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Depth First Search", None))
        self.radioButton_3.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"A Star", None))
        self.radioButton_4.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"IDA Star", None))
        self.btn_undo.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Undo", None))
        self.btn_solve.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Solve", None))
        self.btn_show_solution.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Show Solution", None))
    # retranslateUi

