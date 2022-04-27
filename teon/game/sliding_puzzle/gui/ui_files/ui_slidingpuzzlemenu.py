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

        self.listWidget = QListWidget(SlidingPuzzleMenu)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_2.addWidget(self.listWidget)


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

        self.btn_new_game = QPushButton(SlidingPuzzleMenu)
        self.btn_new_game.setObjectName(u"btn_new_game")

        self.horizontalLayout.addWidget(self.btn_new_game)

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
        self.btn_undo.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Undo", None))
        self.btn_new_game.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"New Game", None))
        self.btn_show_solution.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Show Solution", None))
    # retranslateUi

