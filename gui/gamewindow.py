from typing import List

from PySide2.QtGui import QTransform
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItemGroup, \
    QGraphicsItem, QMainWindow, QGraphicsSceneMouseEvent

from game.boardstate import BoardState
from game.game import Game
from game.movefeedback import MoveFeedBack
from game.player import Player
from game.settings import Settings
from gui.GameBlock import BTile, GPiece


class GDialog(QGraphicsScene):

    def __init__(self, parent=None):
        super(GDialog, self).__init__(parent)
        self.game = Game()
        self.possible_moves: List[BoardState] = []  # ✅
        self.tiles: List[QGraphicsItem] = [None] * Settings.SQUARE_NO
        self.pieces: [QGraphicsItem] = []
        self.add_tiles()
        self.add_pieces()

    def _update_checker_board(self):
        self.clear()
        self.add_tiles()
        self.add_pieces()
        self.highlight_new_pos()

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        game = self.game
        if game.get_turn() is Player.AI:
            return
        clicked_piece = self.itemAt(event.scenePos(), QTransform())

        if clicked_piece is None:
            return
        if not isinstance(clicked_piece, GPiece):
            return

        pos = clicked_piece.board_pos
        self.possible_moves = game.get_valid_moves(pos)
        self._update_checker_board()

        # TODO update checker board here for ghost buttons
        if len(self.possible_moves) == 0:
            feedback = game.move_feedback_click()
            if feedback is MoveFeedBack.FORCED_JUMP:
                self.on_help_movable_click()
        else:
            print("")
        super().mouseMoveEvent(event)

    def on_help_movable_click(self):
        pass

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

    def highlight_new_pos(self):
        pos_moves = self.possible_moves
        if not pos_moves:
            return

        for state in pos_moves:
            h_pos = state.get_to_pos()
            print(f"the hpos: {h_pos}")
            x = (h_pos % Settings.BOARD_DIMEN) * Settings.G_WIDTH
            y = (h_pos // Settings.BOARD_DIMEN) * Settings.G_WIDTH
            current_tile = self.itemAt(x, y, QTransform())
            if not isinstance(current_tile, BTile):
                return
            current_tile.toggle_highlight()
