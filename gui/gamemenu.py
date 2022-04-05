import sys

from PySide2 import QtCore
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QMainWindow, QGraphicsView, QDialog

from game.settings import Settings
from gui.gamewindow import GDialog
from gui.preferencemenu import PreferenceMenu
from gui.ui_files.ui_menu import Ui_Form as UIGameMenu


class GameMenu(QWidget):

    def __init__(self, parent=None):
        super(GameMenu, self).__init__(parent)

        self.ui = UIGameMenu()
        self.ui.setupUi(self)

        # connecting signal and slots
        # TODO set back to the preference page
        self.ui.btn_start.clicked.connect(self.start_checkers)
        self.ui.btn_exit.clicked.connect(self.exit_game)

    @Slot()
    def show_preference(self):
        pref_dialog = PreferenceMenu(self)
        pref_dialog.exec_()
        self.start_checkers()

    @Slot()
    def show_rules(self):
        pass

    @Slot()
    def exit_game(self):
        sys.exit()

    @Slot()
    def start_checkers(self):
        mainwindow = QMainWindow(self)
        mainwindow.setMinimumSize(Settings.G_BOARD_DIMEN, Settings.G_BOARD_DIMEN)
        scene = GDialog(self)
        view = QGraphicsView(scene, mainwindow)
        view.setGeometry(0, 0, Settings.G_BOARD_DIMEN, Settings.G_BOARD_DIMEN)
        mainwindow.setCentralWidget(view)
        scene.setSceneRect(view.geometry())
        mainwindow.setWindowTitle("Checkers")
        mainwindow.show()
