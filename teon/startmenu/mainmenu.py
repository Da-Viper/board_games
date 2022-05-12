from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget

from teon.game.checkers.gui.gamemenu import GameMenu
from teon.game.connect4.gui.connect4menu import Connect4Menu
from teon.game.n_queens.gui.queendialog import NQueensPrefDialog
from teon.game.sliding_puzzle.gui.puzzlemenu import SlidingMenu
from teon.startmenu.ui_files.ui_mainmenu import Ui_GameMainMenu


class MainMenu(QWidget):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.ui = Ui_GameMainMenu()
        self.ui.setupUi(self)

        self.ui.btn_checkers.clicked.connect(self.show_checkers)
        self.ui.btn_ttt.clicked.connect(self.show_connect_4)
        self.ui.btn_15_puzzle.clicked.connect(self.show_15_puzzle)
        self.ui.btn_nqueens.clicked.connect(self.show_n_queens)

    @Slot()
    def show_checkers(self):
        """
        Launch the checkers menu
        Returns:

        """
        checker_menu = GameMenu(self)
        checker_menu.exec_()

    @Slot()
    def show_connect_4(self):
        """
        Launch the connect4 menu
        Returns:

        """
        ttt_menu = Connect4Menu(self)
        ttt_menu.exec_()

    @Slot()
    def show_15_puzzle(self):
        """
        Launches the 15 puzzle menu
        Returns:

        """
        puzzle_15 = SlidingMenu(self)
        puzzle_15.exec_()

    @Slot()
    def show_n_queens(self):
        """
        Launches the NQueens Menu
        Returns:

        """
        dialog = NQueensPrefDialog(self)
        dialog.exec_()
