from enum import IntEnum

from PySide2.QtCore import Slot, QObject
from PySide2.QtWidgets import QPushButton

from game.tictactoe.engine.board import TBoard, Player
from game.tictactoe.gui.tile import Tile


class TTTController(QObject):

    def __init__(self, board_size: int, parent=None):
        super(TTTController, self).__init__(parent)
        self._cell_count = board_size * board_size
        self._board = TBoard(board_size)
        self.turn = Player.ONE

    def run(self):
        pass

    def _init_connections(self):
        pass

    @Slot(Tile)
    def update_cell(self, tile: Tile):
        tile.toggled = True
        tile_pos = tile.pos
        if not TTTController.is_valid_pos(tile_pos, self._cell_count):
            return
        self._board.cells[tile.pos] = self.turn
        tile.player = self.turn
        self.turn *= -1
        print(f"from controller current pos : {tile.pos}")
        tile.update()

    def update(self, tile: QPushButton):
        print(f"clicked button {self.view.ui.board_grid.indexOf(tile)}")

    @staticmethod
    def is_valid_pos(pos: int, bound: int):
        return 0 <= pos < bound
