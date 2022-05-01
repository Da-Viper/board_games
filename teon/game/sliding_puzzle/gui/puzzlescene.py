from typing import List

from PySide2.QtCore import QRect, Signal
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsScene

from teon.game.sliding_puzzle.gui.tile import Tile


class PuzzleScene(QGraphicsScene):
    tile_clicked = Signal(Tile)

    def __init__(self, geometry: QRect, parent=None):
        super(PuzzleScene, self).__init__(geometry, parent)
        self.board_size = -1
        self.setBackgroundBrush(QColor("#b58863"))
        self.tiles: List[Tile] = []

    def draw_board(self, size):
        self.board_size = size
        item_width = int(self.width() // size)
        item_height = int(self.height() // size)

        board = []
        for i in range(size * size - 1):
            row, col = divmod(i, size)
            item_pos = QRect(col, row, item_width, item_height)
            curr_tile = Tile(i, item_pos)
            self.tiles.append(curr_tile)
            board.append(i + 1)
            self.addItem(curr_tile)
        board.append(0)
        self.tiles.append(None)
        return board
