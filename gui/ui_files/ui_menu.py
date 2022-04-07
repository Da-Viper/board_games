# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, verticalWidget):
        if not verticalWidget.objectName():
            verticalWidget.setObjectName(u"verticalWidget")
        verticalWidget.resize(401, 301)
        self.verticalLayout = QVBoxLayout(verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_start = QPushButton(verticalWidget)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_3.addWidget(self.btn_start)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_rules = QPushButton(verticalWidget)
        self.btn_rules.setObjectName(u"btn_rules")

        self.horizontalLayout.addWidget(self.btn_rules)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.btn_exit = QPushButton(verticalWidget)
        self.btn_exit.setObjectName(u"btn_exit")

        self.horizontalLayout_2.addWidget(self.btn_exit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(verticalWidget)

        QMetaObject.connectSlotsByName(verticalWidget)
    # setupUi

    def retranslateUi(self, verticalWidget):
        self.btn_start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.btn_rules.setText(QCoreApplication.translate("Form", u"Rules", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        pass
    # retranslateUi

