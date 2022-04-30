# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmenu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GameMainMenu(object):
    def setupUi(self, GameMainMenu):
        if not GameMainMenu.objectName():
            GameMainMenu.setObjectName(u"GameMainMenu")
        GameMainMenu.resize(828, 563)
        self.verticalLayout = QVBoxLayout(GameMainMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(GameMainMenu)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(GameMainMenu)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Fira Sans")
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.GamesLayout = QVBoxLayout()
        self.GamesLayout.setObjectName(u"GamesLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.btn_checkers = QPushButton(GameMainMenu)
        self.btn_checkers.setObjectName(u"btn_checkers")
        font2 = QFont()
        font2.setFamily(u"Fira Sans")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.btn_checkers.setFont(font2)

        self.horizontalLayout_7.addWidget(self.btn_checkers)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.GamesLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.btn_ttt = QPushButton(GameMainMenu)
        self.btn_ttt.setObjectName(u"btn_ttt")
        self.btn_ttt.setFont(font2)

        self.horizontalLayout_6.addWidget(self.btn_ttt)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.GamesLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_15_puzzle = QPushButton(GameMainMenu)
        self.btn_15_puzzle.setObjectName(u"btn_15_puzzle")
        self.btn_15_puzzle.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_15_puzzle)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.GamesLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.btn_nqueens = QPushButton(GameMainMenu)
        self.btn_nqueens.setObjectName(u"btn_nqueens")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setWeight(50)
        self.btn_nqueens.setFont(font3)

        self.horizontalLayout_2.addWidget(self.btn_nqueens)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.GamesLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.GamesLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(GameMainMenu)

        QMetaObject.connectSlotsByName(GameMainMenu)
    # setupUi

    def retranslateUi(self, GameMainMenu):
        GameMainMenu.setWindowTitle(QCoreApplication.translate("GameMainMenu", u"Form", None))
        self.label.setText(QCoreApplication.translate("GameMainMenu", u"Learn Backtracking", None))
        self.label_2.setText(QCoreApplication.translate("GameMainMenu", u"Play", None))
        self.btn_checkers.setText(QCoreApplication.translate("GameMainMenu", u"Checkers", None))
        self.btn_ttt.setText(QCoreApplication.translate("GameMainMenu", u"Connect 4", None))
        self.btn_15_puzzle.setText(QCoreApplication.translate("GameMainMenu", u"15 Puzzle", None))
        self.btn_nqueens.setText(QCoreApplication.translate("GameMainMenu", u"N-Queens", None))
    # retranslateUi

