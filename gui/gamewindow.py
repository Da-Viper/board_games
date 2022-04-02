from typing import List

from PyQt5.QtCore import QRect, QRectF
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QDialog, QGraphicsItemGroup, \
    QGraphicsItem, QVBoxLayout, QHBoxLayout, QMainWindow

from game.boardstate import BoardState
from game.game import Game
from game.settings import Settings
from gui.GameBlock import BTile, GPiece


class GDialog(QMainWindow):

    def __init__(self, parent=None):
        super(GDialog, self).__init__(parent)
        ##
        self.game = Game()
        self.possible_moves: List[BoardState] = []

        # UI
        # self.setMinimumSize(Settings.T_WIDTH * Settings.G_WIDTH + 20, Settings.T_HEIGHT * Settings.G_HEIGHT + 20)
        self.t_group: QGraphicsItemGroup = QGraphicsItemGroup()
        self.p_group: QGraphicsItemGroup = QGraphicsItemGroup()
        self.scene: QGraphicsScene = QGraphicsScene(self)
        self.view: QGraphicsView = QGraphicsView(self.scene, self)
        self.tiles: List[QGraphicsItem] = [None] * Settings.SQUARE_NO
        self.pieces: [QGraphicsItem] = []
        self._setup_ui()
        self.add_tiles()
        self.add_pieces()
        self.scene.addItem(self.p_group)

    def add_tiles(self):
        for i in range(Settings.SQUARE_NO):
            grid_x = i % Settings.BOARD_DIMEN
            grid_y = i // Settings.BOARD_DIMEN
            curr_tile = BTile(grid_x, grid_y)
            self.tiles[i] = curr_tile
            self.t_group.addToGroup(curr_tile)

    def add_pieces(self):
        scene = self.scene
        pieces = self.pieces
        for i in range(Settings.SQUARE_NO):
            grid_x = i % Settings.BOARD_DIMEN
            grid_y = i // Settings.BOARD_DIMEN
            curr_piece = self.game.get_state().get_piece(i)
            if curr_piece is not None:
                curr_gpiece = GPiece(grid_x, grid_y, i, curr_piece)
                scene.addItem(curr_gpiece)
                pieces.append(curr_gpiece)

    def _setup_ui(self):
        scene = self.scene
        view = self.view
        view.setGeometry(0, 0, Settings.T_WIDTH * Settings.G_WIDTH, Settings.T_HEIGHT * Settings.G_HEIGHT)
        scene.setSceneRect(view.geometry())
        self.setCentralWidget(view)
        scene.setSceneRect(view.geometry())
        scene.addItem(self.t_group)
