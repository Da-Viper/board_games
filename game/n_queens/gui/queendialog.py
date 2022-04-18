from PySide2.QtWidgets import QDialog

from game.n_queens.engine.queencontroller import QueenController
from game.n_queens.gui.queenscene import NQueenScene
from game.tictactoe.gui.ui_files.ui_tictactoemenu import Ui_TictactoeMenu


class NQueensMenu(QDialog):

    def __init__(self, parent=None):
        super(NQueensMenu, self).__init__(parent)
        self.ui = Ui_TictactoeMenu()
        self.ui.setupUi(self)
        self.view = self.ui.g_view
        self.view.setGeometry(0, 0, 600, 600)
        print(f"view rect {self.view.sceneRect(), self.view.geometry()}")
        self.scene = NQueenScene(self.view.geometry(), self)
        self._controller = QueenController(self.scene, 8)
        self.view.setScene(self.scene)
        self.setMinimumSize(600, 600)
        self.adjustSize()
