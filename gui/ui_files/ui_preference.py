# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preference.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_rad_easy = QRadioButton(self.groupBox)
        self.btn_rad_easy.setObjectName(u"btn_rad_easy")
        self.btn_rad_easy.setChecked(True)

        self.verticalLayout_3.addWidget(self.btn_rad_easy)

        self.btn_rad_med = QRadioButton(self.groupBox)
        self.btn_rad_med.setObjectName(u"btn_rad_med")

        self.verticalLayout_3.addWidget(self.btn_rad_med)

        self.btn_rad_hard = QRadioButton(self.groupBox)
        self.btn_rad_hard.setObjectName(u"btn_rad_hard")

        self.verticalLayout_3.addWidget(self.btn_rad_hard)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_rad_player = QRadioButton(self.groupBox_2)
        self.btn_rad_player.setObjectName(u"btn_rad_player")
        self.btn_rad_player.setChecked(True)

        self.horizontalLayout.addWidget(self.btn_rad_player)

        self.btn_rad_ai = QRadioButton(self.groupBox_2)
        self.btn_rad_ai.setObjectName(u"btn_rad_ai")

        self.horizontalLayout.addWidget(self.btn_rad_ai)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Select Difficulty", None))
        self.btn_rad_easy.setText(QCoreApplication.translate("Dialog", u"Easy", None))
        self.btn_rad_med.setText(QCoreApplication.translate("Dialog", u"Meduim", None))
        self.btn_rad_hard.setText(QCoreApplication.translate("Dialog", u"Hard", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"First Player", None))
        self.btn_rad_player.setText(QCoreApplication.translate("Dialog", u"Human", None))
        self.btn_rad_ai.setText(QCoreApplication.translate("Dialog", u"Computer", None))
    # retranslateUi

