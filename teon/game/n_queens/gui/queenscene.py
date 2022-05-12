import numpy as np
from PySide2.QtCore import QRect, Signal
from PySide2.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent
from numpy import ndarray

from teon.game.n_queens.engine.board import Pos, Piece
from teon.game.n_queens.gui.tile import Tile


class NQueenScene(QGraphicsScene):
    tile_clicked = Signal(Tile)

    def __init__(self, rect: QRect, parent=None):
        super(NQueenScene, self).__init__(rect, parent)
        self.tiles: ndarray = None
        self.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.enable_mouse_press = True

    def init_grid(self, size: int):
        self.tiles = np.empty((size, size), dtype=Tile)
        board_b = np.empty((size, size), dtype=Pos)
        item_width = int(self.width() // size)
        item_height = int(self.height() // size)

        for i in range(size * size):
            row, col = divmod(i, size)
            item_pos = QRect(col * item_width, row * item_height, item_width, item_height)
            nqueen_pos = Pos(False, False, np.int8(0))
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
        """Draw the board solution to the scene gotten from the controller"""
        tiles = self.tiles
        for row, r_val in enumerate(sol_board):
            for col, col_val in enumerate(r_val):
                current_tile_pos: Pos = tiles[row][col].p_pos
                if col_val == Piece.FIXED_QUEEN:
                    current_tile_pos.is_fixed = True
                    current_tile_pos.has_queen = True
                elif col_val == Piece.Q_VALUE:
                    current_tile_pos.has_queen = True
                else:
                    current_tile_pos.has_queen = False
                    current_tile_pos.conflicts = 1
        self.update()
