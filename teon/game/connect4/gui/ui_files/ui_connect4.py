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


class Ui_Connect4Menu(object):
    def setupUi(self, Connect4Menu):
        if not Connect4Menu.objectName():
            Connect4Menu.setObjectName(u"Connect4Menu")
        Connect4Menu.resize(689, 614)
        self.verticalLayout_2 = QVBoxLayout(Connect4Menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.g_view = QGraphicsView(Connect4Menu)
        self.g_view.setObjectName(u"g_view")

        self.verticalLayout.addWidget(self.g_view)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btn_0 = QPushButton(Connect4Menu)
        self.btn_0.setObjectName(u"btn_0")

        self.horizontalLayout_2.addWidget(self.btn_0)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.btn_1 = QPushButton(Connect4Menu)
        self.btn_1.setObjectName(u"btn_1")

        self.horizontalLayout_2.addWidget(self.btn_1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.btn_2 = QPushButton(Connect4Menu)
        self.btn_2.setObjectName(u"btn_2")

        self.horizontalLayout_2.addWidget(self.btn_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.btn_3 = QPushButton(Connect4Menu)
        self.btn_3.setObjectName(u"btn_3")

        self.horizontalLayout_2.addWidget(self.btn_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.btn_4 = QPushButton(Connect4Menu)
        self.btn_4.setObjectName(u"btn_4")

        self.horizontalLayout_2.addWidget(self.btn_4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.btn_5 = QPushButton(Connect4Menu)
        self.btn_5.setObjectName(u"btn_5")

        self.horizontalLayout_2.addWidget(self.btn_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.btn_6 = QPushButton(Connect4Menu)
        self.btn_6.setObjectName(u"btn_6")

        self.horizontalLayout_2.addWidget(self.btn_6)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_undo = QPushButton(Connect4Menu)
        self.btn_undo.setObjectName(u"btn_undo")

        self.horizontalLayout.addWidget(self.btn_undo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_new_game = QPushButton(Connect4Menu)
        self.btn_new_game.setObjectName(u"btn_new_game")

        self.horizontalLayout.addWidget(self.btn_new_game)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Connect4Menu)

        QMetaObject.connectSlotsByName(Connect4Menu)
    # setupUi

    def retranslateUi(self, Connect4Menu):
        Connect4Menu.setWindowTitle(QCoreApplication.translate("Connect4Menu", u"Dialog", None))
        self.btn_0.setText(QCoreApplication.translate("Connect4Menu", u"Add", None))
        self.btn_1.setText(QCoreApplication.translate("Connect4Menu", u"Add", None))
        self.btn_2.setText(QCoreApplication.translate("Connect4Menu", u"Add", None))
        self.btn_3.setText(QCoreApplication.translate("Connect4Menu", u"Add", None))
        self.btn_4.setText(QCoreApplication.translate("Connect4Menu", u"Add", None))
        self.btn_5.setText(QCoreApplication.translate("Connect4Menu", u"Add", None))
        self.btn_6.setText(QCoreApplication.translate("Connect4Menu", u"Add", None))
        self.btn_undo.setText(QCoreApplication.translate("Connect4Menu", u"Undo", None))
        self.btn_new_game.setText(QCoreApplication.translate("Connect4Menu", u"New Game", None))
    # retranslateUi

