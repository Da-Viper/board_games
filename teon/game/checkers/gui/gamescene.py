from typing import List

from PySide2.QtCore import Slot
from PySide2.QtGui import QTransform
from PySide2.QtWidgets import QGraphicsScene, QGraphicsItem, QGraphicsSceneMouseEvent, QMessageBox

from teon.game.checkers.engine.snode import SNode
from teon.game.checkers.engine.controller import Controller
from teon.game.checkers.engine.gameresponse import GameResponse
from teon.game.checkers.engine.player import Player
from teon.game.checkers.engine.settings import Settings
from teon.game.checkers.gui.models import BTile, GPiece
from teon.utils import utils


class GameScene(QGraphicsScene):

    def __init__(self, parent=None):
        super(GameScene, self).__init__(parent)
        self.forced_moves: List[int] = None
        self.game = Controller()
        self.possible_moves: List[SNode] = []
        self.tiles: List[BTile] = [None] * Settings.SQUARE_NO
        self.pieces: [QGraphicsItem] = []
        self._setup_game_preferences()
        self.feedback = None

    def _update_checker_board(self):
        self.clear()
        self.add_tiles()
        self.add_pieces()
        self.highlight_new_pos()
        utils.qt_sleep(300)
        self.update()

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        game = self.game
        if game.get_turn() is Player.AI:
            return
        clicked_piece = self.itemAt(event.scenePos(), QTransform())

        if clicked_piece is None:
            return

        if isinstance(clicked_piece, BTile):
            if clicked_piece.is_highlighted:
                if not game.is_over() and game.get_turn() == Player.HUMAN:
                    self.forced_moves = []
                    clicked_piece.toggle_highlight()  # turn off highlight
                    self.possible_moves = []
                    game.player_move(clicked_piece.get_state())
                    self._update_checker_board()
                    print("updating board")
                    self.move_ai()
                    if game.is_over():
                        self._show_game_over_dialog()
                    # TODO add __self.gameover()

        elif isinstance(clicked_piece, GPiece):
            pos = clicked_piece.board_pos
            self.possible_moves = game.get_valid_moves(pos)
            if clicked_piece.piece.player is Player.HUMAN:
                if len(self.possible_moves) == 0:
                    feedback = game.move_feedback_click()
                    if feedback is GameResponse.FORCED_JUMP:
                        allstate: List[SNode] = game.get_state().get_possible_state(True)
                        self.forced_moves = list(map(lambda x: x.from_pos, allstate))
                        self.possible_moves = game.get_valid_moves(pos)
                        self._update_checker_board()

            self._update_checker_board()
        super().mouseMoveEvent(event)

    def move_ai(self):
        game = self.game
        game.ai_move()
        self._update_checker_board()
        if not game.is_over() and (game.get_turn() is Player.AI):
            self.move_ai()

    def highlight_new_pos(self):
        pos_moves = self.possible_moves
        if not pos_moves:
            return
        gui_width = Settings.G_WIDTH
        offset = gui_width / 2

        for state in pos_moves:
            h_pos = state.to_pos
            col = (h_pos % Settings.BOARD_DIMEN) * gui_width
            row = (h_pos // Settings.BOARD_DIMEN) * gui_width

            current_tile = self.itemAt(col + offset, row + offset, QTransform())
            if not isinstance(current_tile, BTile):
                continue
            current_tile.toggle_highlight()
            current_tile.set_state(state)

    def _setup_game_preferences(self):
        self._update_checker_board()
        if Settings.FIRST_MOVE is Player.AI:
            self.move_ai()

    def _show_game_over_dialog(self):
        msg_box = QMessageBox()
        msg_box.setText(self.game.get_game_over_message())
        msg_box.setInformativeText("Do you want to play again ?")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)

        res = msg_box.exec_()
        if res == QMessageBox.Ok:
            self.clear()
            self.reset_game()
        else:
            pass

    def add_tiles(self):
        tiles = self.tiles
        force_moves = self.forced_moves
        for i in range(Settings.SQUARE_NO):
            grid_y, grid_x = divmod(i, Settings.BOARD_DIMEN)
            curr_tile = BTile(grid_x, grid_y)
            self.addItem(curr_tile)
            tiles[i] = curr_tile

            if force_moves is not None:
                if i in force_moves:
                    tiles[i].toggle_highlight()

    def add_pieces(self):
        pieces = self.pieces
        curr_state = self.game.get_state()
        for i in range(Settings.SQUARE_NO):
            grid_y, grid_x = divmod(i, Settings.BOARD_DIMEN)
            curr_piece = curr_state.state[i]
            if curr_piece is not None:
                curr_gpiece = GPiece(grid_x, grid_y, curr_piece, i)
                self.addItem(curr_gpiece)
                pieces.append(curr_gpiece)

    def reset_game(self):
        self.game = Controller()
        self.possible_moves: List[SNode] = []
        self.tiles: List[BTile] = [None] * Settings.SQUARE_NO
        self.pieces: [QGraphicsItem] = []
        self.forced_moves = None
        self._setup_game_preferences()

    @Slot()
    def slot_undo_clicked(self):
        self.game.undo()
        self._update_checker_board()
