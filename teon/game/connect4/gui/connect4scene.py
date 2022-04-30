from typing import Tuple

import numpy as np
from PySide2.QtCore import Signal, QRect, Slot
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsScene
from numpy import ndarray

from teon.game.connect4.engine.board import Player
from teon.game.connect4.gui.connectpiece import ConnectPiece


class TScene(QGraphicsScene):
    BG_COLOR = QColor("#f0d9b5")
    tile_clicked = Signal(ConnectPiece)

    def __init__(self, width: int, height: int, rect: QRect, parent=None):
        super(TScene, self).__init__(rect, parent)
        self._tiles: ndarray = None
        self.b_rows = width
        self.b_cols = height
        self.setBackgroundBrush(TScene.BG_COLOR)
        self.setItemIndexMethod(QGraphicsScene.NoIndex)

    def init_grid(self, b_row: int, b_col: int) -> ndarray:
        self._tiles = np.empty((b_row, b_col), dtype=ConnectPiece)
        item_width = int(self.width() // b_col)
        item_height = int(self.height() // b_row)

        for i in range(b_row * b_col):
            row, col = divmod(i, b_col)
            item_pos = QRect(col * item_height, row * item_width, item_height, item_width)
            curr_tile = ConnectPiece(item_pos)
            self.addItem(curr_tile)
            self._tiles[row][col] = curr_tile

        return self._tiles

    # @Slot(tuple)
    def slot_update_pos(self, pos: Tuple[int, int], player: Player):
        t_row, t_col = pos
        cur_tile: ConnectPiece = self._tiles[t_row][t_col]
        cur_tile.player = player
        cur_tile.update()

    def init_connections(self):
        self.tile_clicked[ConnectPiece].connect(self._controller.update_cell)
