from typing import List

from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItemGroup, \
    QGraphicsItem, QMainWindow

import gui.GameBlock
from game.boardstate import BoardState
from game.game import Game
from game.settings import Settings
from gui.GameBlock import BTile, GPiece


class GDialog(QGraphicsScene):

    def __init__(self, parent=None):
        super(GDialog, self).__init__(parent)
        self.game = Game()
        gui.GameBlock.GAME_WINDOW = self
        self.possible_moves: List[BoardState] = [] # ✅
        self.tiles: List[QGraphicsItem] = [None] * Settings.SQUARE_NO
        self.pieces: [QGraphicsItem] = []
        self.add_tiles()
        self.add_pieces()

    def add_tiles(self):
        # scene = self.scene
        tiles = self.tiles
        for i in range(Settings.SQUARE_NO):
            grid_x = i % Settings.BOARD_DIMEN
            grid_y = i // Settings.BOARD_DIMEN
            curr_tile = BTile(grid_x, grid_y)
            self.addItem(curr_tile)
            tiles[i] = curr_tile

    def add_pieces(self):
        # scene = self.scene
        pieces = self.pieces
        for i in range(Settings.SQUARE_NO):

            grid_x = i % Settings.BOARD_DIMEN
            grid_y = i // Settings.BOARD_DIMEN
            curr_piece = self.game.get_state().get_piece(i)
            if curr_piece is not None:
                curr_gpiece = GPiece(grid_x, grid_y, curr_piece, i)
                self.addItem(curr_gpiece)
                pieces.append(curr_gpiece)

