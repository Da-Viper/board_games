from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QWidget

from game.checkers.gui.gamemenu import GameMenu
from gui.ui_files.ui_mainmenu import Ui_GameMainMenu


class MainMenu(QWidget):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.ui = Ui_GameMainMenu()
        self.ui.setupUi(self)
        self.setMinimumSize(600, 480)

        self.ui.btn_checkers.clicked.connect(self.show_checkers)

    @Slot()
    def show_checkers(self):
        print("i go here")
        checker_menu = GameMenu(self)
        checker_menu.show()

    @Slot()
    def show_tic_tac_toe(self):
        pass

    @Slot()
    def show_15_puzzle(self):
        pass
