from typing import List, Tuple

import numpy as np
from PySide2.QtCore import QRect, Signal, Slot
from PySide2.QtWidgets import QGraphicsScene
from numpy import ndarray

from game.n_queens.engine.board import Pos
from game.n_queens.gui.tile import Tile


class NQueenScene(QGraphicsScene):
    tile_clicked = Signal(Tile)

    def __init__(self, rect: QRect, parent=None):
        super(NQueenScene, self).__init__(rect, parent)
        self.tiles: ndarray = None
        self.setItemIndexMethod(QGraphicsScene.NoIndex)
        # self._tiles = np.zeros()

    def init_grid(self, size: int):
        self.tiles = np.empty((size, size), dtype=Tile)
        board_b = np.empty((size, size), dtype=Pos)
        item_width = int(self.width() // size)
        item_height = int(self.height() // size)

        for i in range(size * size):
            row, col = divmod(i, size)
            item_pos = QRect(col * item_width, row * item_height, item_width, item_height)
            nqueen_pos = Pos(False, np.int8(0))
            curr_tile = Tile(nqueen_pos, (row, col), item_pos)

            self.addItem(curr_tile)
            board_b[row][col] = nqueen_pos
            self.tiles[row][col] = curr_tile
            # self._tiles.append(curr_tile)
        return board_b
