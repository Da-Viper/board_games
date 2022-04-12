from enum import IntEnum

from PySide2.QtCore import Slot, QObject
from PySide2.QtWidgets import QPushButton

from game.tictactoe.engine.board import TBoard
from game.tictactoe.gui.tile import Tile


class Player(IntEnum):
    ONE = 1
    TWO = 2


class TTTController(QObject):

    def __init__(self, board_size: int, parent=None):
        super(TTTController, self).__init__(parent)

        self._board = TBoard(board_size)
        self.turn = Player.ONE

    def run(self):
        pass

    def _init_connections(self):
        pass

    @Slot(Tile)
    def update_cell(self, tile: Tile):
        tile.toggled = True
        tile.update()
        print(f"from controller current pos : {tile.pos}")

    def update(self, tile: QPushButton):
        print(f"clicked button {self.view.ui.board_grid.indexOf(tile)}")
