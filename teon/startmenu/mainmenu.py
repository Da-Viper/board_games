from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget

from teon.game.checkers.gui.gamemenu import GameMenu
from teon.game.n_queens.gui.queendialog import NQueensMenu
from teon.game.sliding_puzzle.gui.puzzlemenu import SlidingMenu
from teon.game.connect4.gui.connect4menu import Connect4Menu
from teon.startmenu.ui_files.ui_mainmenu import Ui_GameMainMenu


class MainMenu(QWidget):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.ui = Ui_GameMainMenu()
        self.ui.setupUi(self)

        self.ui.btn_checkers.clicked.connect(self.show_checkers)
        self.ui.btn_ttt.clicked.connect(self.show_tic_tac_toe)
        self.ui.btn_15_puzzle.clicked.connect(self.show_15_puzzle)
        self.ui.btn_nqueens.clicked.connect(self.show_n_queens)

    @Slot()
    def show_checkers(self):
        checker_menu = GameMenu(self)
        checker_menu.show()

    @Slot()
    def show_tic_tac_toe(self):
        ttt_menu = Connect4Menu(self)
        ttt_menu.show()

    @Slot()
    def show_15_puzzle(self):
        puzzle_15 = SlidingMenu()
        puzzle_15.exec_()

    @Slot()
    def show_n_queens(self):
        dialog = NQueensMenu(self)
        dialog.show()
