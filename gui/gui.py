import sys

from PySide2.QtCore import QCoreApplication, Qt
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
        hint_moves = []

    def run(self):
        # game setup
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        app = QApplication(sys.argv)

        # with open("../style.qss", "r") as f:
        #     _style = f.read()
        #     app.setStyleSheet(_style)
        # app.setStyle("Windows")
        gmenu = GameMenu()
        gmenu.show()
        # end
        self.setup()
        sys.exit(app.exec_())

    def setup(self):
        pass
