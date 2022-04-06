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
        self.possible_moves: List[BoardState] = []
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

        print(f"the clicked piece: {clicked_piece}")

        if clicked_piece is None:
            return

        if isinstance(clicked_piece, BTile):
            if clicked_piece.is_highlighted:
                if not game.is_over() and game.get_turn() == Player.HUMAN:
                    clicked_piece.toggle_highlight()  # turn off highlight
                    self.possible_moves = []
                    game.player_move(clicked_piece.get_state())
                    self._update_checker_board()
                    self.ai_move()
                    if game.is_over():
                        return
                        # TODO add __self.gameover()

        elif isinstance(clicked_piece, GPiece):
            pos = clicked_piece.board_pos
            self.possible_moves = game.get_valid_moves(pos)
            if clicked_piece.piece.player is Player.HUMAN:
                if len(self.possible_moves) == 0:
                    feedback = game.move_feedback_click()
                    sucg = (game.state_peek().get_successors_jump(True))
                    print(sucg)
                    if feedback is MoveFeedBack.FORCED_JUMP:
                        self.possible_moves = game.get_valid_moves(pos)
                        print(feedback)
                        self._update_checker_board()
                        # self.on_help_movable_click()

            self._update_checker_board()
        super().mouseMoveEvent(event)

    def on_help_movable_click(self):
        print(f"you need to play forced move")

    def ai_move(self):
        game = self.game
        game.ai_move()

        ##  INVOKE AI UPDATE
        self._update_checker_board()
        if not game.is_over() and (game.get_turn() is Player.AI):
            self.ai_move()

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
            current_tile.set_state(state)
