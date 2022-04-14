from PySide2.QtCore import Slot, QTimer, QObject
from PySide2.QtWidgets import QWidget

from game.checkers.gui.gamemenu import GameMenu
from game.sliding_puzzle.gui.puzzlescene import SlidingMenu
from game.tictactoe.gui.tttmenu import TTTMenu
from gui.ui_files.ui_mainmenu import Ui_GameMainMenu


class MainMenu(QWidget):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.ui = Ui_GameMainMenu()
        self.ui.setupUi(self)

        self.ui.btn_checkers.clicked.connect(self.show_checkers)
        self.ui.btn_ttt.clicked.connect(self.show_tic_tac_toe)
        self.ui.btn_15_puzzle.clicked.connect(self.show_15_puzzle)

    @Slot()
    def show_checkers(self):
        checker_menu = GameMenu(self)
        checker_menu.show()

    @Slot()
    def show_tic_tac_toe(self):
        ttt_menu = TTTMenu(self)
        ttt_menu.show()

    @Slot()
    def show_15_puzzle(self):
        puzzle_15 = SlidingMenu()
        puzzle_15.exec_()
