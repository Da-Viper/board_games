from typing import List

from PySide2.QtGui import QTransform
from PySide2.QtWidgets import QGraphicsScene, QGraphicsItem, QGraphicsSceneMouseEvent, QMessageBox

from game.boardstate import BoardState
from game.game import Game
from game.gameresponse import GameResponse
from game.player import Player
from game.settings import Settings
from gui.gameblock import BTile, GPiece


class GameScene(QGraphicsScene):

    def __init__(self, parent=None):
        super(GameScene, self).__init__(parent)
        self.game = Game()
        self.possible_moves: List[BoardState] = []
        self.tiles: List[QGraphicsItem] = [None] * Settings.SQUARE_NO
        self.pieces: [QGraphicsItem] = []
        self._setup_game_preferences()

    def _update_checker_board(self):
        self.clear()
        self.add_tiles()
        self.add_pieces()
        self.highlight_new_pos()
        self.update()

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
                    print("updating board")
                    self.ai_move()
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
                        self.possible_moves = game.get_valid_moves(pos)
                        self._update_checker_board()

            self._update_checker_board()
        super().mouseMoveEvent(event)

    def ai_move(self):
        game = self.game
        game.ai_move()
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
        gui_width = Settings.G_WIDTH
        offset = gui_width / 2

        for state in pos_moves:
            h_pos = state.get_to_pos()
            print(f"the possible GPiece pos: {h_pos % Settings.T_HEIGHT, h_pos // Settings.T_WIDTH}")
            x = (h_pos % Settings.BOARD_DIMEN) * gui_width
            y = (h_pos // Settings.BOARD_DIMEN) * gui_width
            current_tile = self.itemAt(x + offset, y + offset, QTransform())
            if not isinstance(current_tile, BTile):
                return
            current_tile.toggle_highlight()
            print(
                f"BTile highlight pos:{current_tile.pos()}\n")
            current_tile.set_state(state)
            # current_tile.update()

    def _setup_game_preferences(self):
        self._update_checker_board()
        if Settings.FIRST_MOVE is Player.AI:
            self.ai_move()

    def _show_game_over_dialog(self):
        msg_box = QMessageBox()
        msg_box.setText(self.game.get_game_over_message())
        msg_box.setInformativeText("Do you want to play again ?")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)

        res = msg_box.exec_()
        if res == QMessageBox.Ok:
            self.clear()
            self.__init__()
        else:
            pass
            # a: QGraphicsView = self.views()[0]
            # a.parent().close()
