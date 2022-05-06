# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nqueenpreference.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NQueenPrefDialog(object):
    def setupUi(self, NQueenPrefDialog):
        if not NQueenPrefDialog.objectName():
            NQueenPrefDialog.setObjectName(u"NQueenPrefDialog")
        NQueenPrefDialog.resize(401, 126)
        self.verticalLayout = QVBoxLayout(NQueenPrefDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(NQueenPrefDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(NQueenPrefDialog)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(NQueenPrefDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(NQueenPrefDialog)
        self.buttonBox.accepted.connect(NQueenPrefDialog.accept)
        self.buttonBox.rejected.connect(NQueenPrefDialog.reject)

        QMetaObject.connectSlotsByName(NQueenPrefDialog)
    # setupUi

    def retranslateUi(self, NQueenPrefDialog):
        NQueenPrefDialog.setWindowTitle(QCoreApplication.translate("NQueenPrefDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("NQueenPrefDialog", u"Queen Size:", None))
    # retranslateUi

