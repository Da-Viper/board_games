import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget

from gui.preferencemenu import PreferenceMenu
from gui.ui_files.ui_menu import Ui_Form as UIGameMenu


class GameMenu(QWidget):
    def __init__(self, parent=None):
        super(GameMenu, self).__init__(parent)

        self.ui = UIGameMenu()
        self.ui.setupUi(self)

        # connecting signal and slots
        self.ui.btn_start.clicked.connect(self.show_preference)
        self.ui.btn_exit.clicked.connect(self.exit_game)

    @Slot()
    def show_preference(self):
        pref_dialog = PreferenceMenu()
        pref_dialog.exec_()
        pref_dialog.show()

    @Slot()
    def show_rules(self):
        pass

    @Slot()
    def exit_game(self):
        sys.exit()
