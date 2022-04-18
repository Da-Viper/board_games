from typing import Tuple

import numpy as np
from PySide2.QtCore import Slot, Signal, QObject

from game.n_queens.engine.board import NQueen, Piece
from game.n_queens.gui.queenscene import NQueenScene
from game.n_queens.gui.tile import Tile


class QueenController(QObject):
    update_gui = Signal(tuple)

    def __init__(self, scene: NQueenScene, size: int, parent=None):
        super(QueenController, self).__init__(parent)
        self.scene = scene
        self.board = NQueen(size)
        self.scene.init_grid(size)
        self._init_connection()

    @Slot(Tile)
    def update_cell(self, clicked_tile: Tile):
        pos = clicked_tile.pos
        tile_piece = clicked_tile.piece_type
        if tile_piece == Piece.Q_VALUE:
            self.board.remove_queen(pos)
        elif tile_piece == Piece.CONFLICT:
            return
        else:
            self.board.place_queen(pos)
        clicked_tile.piece_type = Piece.Q_VALUE
        self.update_gui.emit(pos)

    @Slot(tuple)
    def slot_update_gui(self):
        board = self.board.conflicts
        tiles = self.scene.tiles
        for i in range(len(board)):
            for j in range(len(board[i])):
                b_piece = board[i][j]
                tiles[i][j].piece_type = b_piece

        print(f"conflicts {board}")
        print(f"board {self.board.board}")
        self.scene.update()

    def _init_connection(self):
        self.scene.tile_clicked[Tile].connect(self.update_cell)
        self.update_gui.connect(self.slot_update_gui)
