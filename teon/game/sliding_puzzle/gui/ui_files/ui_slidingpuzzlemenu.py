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

        self.grpbox_heuristic = QGroupBox(SlidingPuzzleMenu)
        self.grpbox_heuristic.setObjectName(u"grpbox_heuristic")
        self.verticalLayout_3 = QVBoxLayout(self.grpbox_heuristic)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_manhattan = QRadioButton(self.grpbox_heuristic)
        self.btn_manhattan.setObjectName(u"btn_manhattan")
        self.btn_manhattan.setChecked(True)

        self.verticalLayout_3.addWidget(self.btn_manhattan)

        self.btn_misplaced = QRadioButton(self.grpbox_heuristic)
        self.btn_misplaced.setObjectName(u"btn_misplaced")

        self.verticalLayout_3.addWidget(self.btn_misplaced)


        self.verticalLayout.addWidget(self.grpbox_heuristic)

        self.grpbox_search = QGroupBox(SlidingPuzzleMenu)
        self.grpbox_search.setObjectName(u"grpbox_search")
        self.verticalLayout_4 = QVBoxLayout(self.grpbox_search)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_dfs = QRadioButton(self.grpbox_search)
        self.btn_dfs.setObjectName(u"btn_dfs")

        self.verticalLayout_4.addWidget(self.btn_dfs)

        self.btn_astar = QRadioButton(self.grpbox_search)
        self.btn_astar.setObjectName(u"btn_astar")
        self.btn_astar.setChecked(True)

        self.verticalLayout_4.addWidget(self.btn_astar)

        self.btn_idastar = QRadioButton(self.grpbox_search)
        self.btn_idastar.setObjectName(u"btn_idastar")
        self.btn_idastar.setChecked(False)

        self.verticalLayout_4.addWidget(self.btn_idastar)


        self.verticalLayout.addWidget(self.grpbox_search)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_show_svg = QPushButton(SlidingPuzzleMenu)
        self.btn_show_svg.setObjectName(u"btn_show_svg")

        self.horizontalLayout.addWidget(self.btn_show_svg)

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

        self.btn_shuffle = QPushButton(SlidingPuzzleMenu)
        self.btn_shuffle.setObjectName(u"btn_shuffle")

        self.horizontalLayout.addWidget(self.btn_shuffle)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(SlidingPuzzleMenu)

        QMetaObject.connectSlotsByName(SlidingPuzzleMenu)
    # setupUi

    def retranslateUi(self, SlidingPuzzleMenu):
        SlidingPuzzleMenu.setWindowTitle(QCoreApplication.translate("SlidingPuzzleMenu", u"Dialog", None))
        self.grpbox_heuristic.setTitle(QCoreApplication.translate("SlidingPuzzleMenu", u"Heuristic", None))
        self.btn_manhattan.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Man Hattan", None))
        self.btn_misplaced.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Misplaced Tiles", None))
        self.grpbox_search.setTitle(QCoreApplication.translate("SlidingPuzzleMenu", u"Search Type", None))
        self.btn_dfs.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Depth First Search", None))
        self.btn_astar.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"A Star", None))
        self.btn_idastar.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"IDA Star", None))
        self.btn_show_svg.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Search Tree", None))
        self.btn_solve.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Solve", None))
        self.btn_show_solution.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Show Solution", None))
        self.btn_shuffle.setText(QCoreApplication.translate("SlidingPuzzleMenu", u"Shuffle", None))
    # retranslateUi

