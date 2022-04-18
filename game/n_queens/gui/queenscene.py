from typing import List, Tuple

import numpy as np
from PySide2.QtCore import QRect, Signal, Slot
from PySide2.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent
from numpy import ndarray

from game.n_queens.engine.board import Pos, Piece
from game.n_queens.gui.tile import Tile


class NQueenScene(QGraphicsScene):
    tile_clicked = Signal(Tile)

    def __init__(self, rect: QRect, parent=None):
        super(NQueenScene, self).__init__(rect, parent)
        self.tiles: ndarray = None
        self.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.enable_mouse_press = True
        # self._tiles = np.zeros()k

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
        return board_b

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if not self.enable_mouse_press:
            return
        super().mousePressEvent(event)

    def draw_board_solution(self, sol_board: ndarray):
        tiles = self.tiles
        for row, r_val in enumerate(sol_board):
            for col, col_val in enumerate(r_val):
                current_tile: Tile = tiles[row][col]
                if col_val == Piece.Q_VALUE:
                    current_tile.p_pos.has_queen = True
                else:
                    current_tile.p_pos.has_queen = False
                current_tile.p_pos.conflicts = 0
        self.update()
