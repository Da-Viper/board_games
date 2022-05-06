# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect4.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UI_NQueensMenu(object):
    def setupUi(self, TictactoeMenu):
        if not TictactoeMenu.objectName():
            TictactoeMenu.setObjectName(u"TictactoeMenu")
        TictactoeMenu.resize(447, 423)
        self.verticalLayout_2 = QVBoxLayout(TictactoeMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.g_view = QGraphicsView(TictactoeMenu)
        self.g_view.setObjectName(u"g_view")

        self.verticalLayout_2.addWidget(self.g_view)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_undo = QPushButton(TictactoeMenu)
        self.btn_undo.setObjectName(u"btn_undo")

        self.horizontalLayout.addWidget(self.btn_undo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_new_game = QPushButton(TictactoeMenu)
        self.btn_new_game.setObjectName(u"btn_new_game")

        self.horizontalLayout.addWidget(self.btn_new_game)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(TictactoeMenu)

        QMetaObject.connectSlotsByName(TictactoeMenu)
    # setupUi

    def retranslateUi(self, TictactoeMenu):
        TictactoeMenu.setWindowTitle(QCoreApplication.translate("TictactoeMenu", u"Dialog", None))
        self.btn_undo.setText(QCoreApplication.translate("TictactoeMenu", u"Undo", None))
        self.btn_new_game.setText(QCoreApplication.translate("TictactoeMenu", u"New Game", None))
    # retranslateUi

