import sys

from PySide2.QtWidgets import QApplication
from typing import List

from game.boardstate import BoardState
from game.game import Game

from gui.gamemenu import GameMenu


# from gui.preference import Ui_Dialog as PreferenceMenu

class GUI:

    def __init__(self):
        self.game: Game = Game()
        possible_moves: List[BoardState] = []

    def run(self):
        app = QApplication(sys.argv)
        gmenu = GameMenu()
        gmenu.show()

        sys.exit(app.exec_())
