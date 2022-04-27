from PySide2.QtCore import Slot, QObject
from PySide2.QtWidgets import QMessageBox

from teon.game.tictactoe.engine.board import TBoard, Player, GameState
from teon.game.tictactoe.gui.tile import Tile


class TTTController(QObject):

    def __init__(self, board_size: int, parent=None):
        super(TTTController, self).__init__(parent)
        self._cell_count = board_size * board_size
        self._board = TBoard(board_size)
        self.current_player = Player.ONE

    def run(self):
        pass

    def _init_connections(self):
        pass

    @Slot(Tile)
    def update_cell(self, tile: Tile):
        tile.toggled = True
        tile_pos = tile.pos
        if not self._board.place_piece(self.current_player, tile_pos):
            return
        tile.player = self.current_player
        tile.update()
        print(f"from controller current pos : {tile.pos}")
        print(f"Next player {self.current_player}")

        game_state: GameState = self._board.get_game_state(tile_pos)
        self.has_won(game_state)

        self.current_player *= -1

    @staticmethod
    def has_won(state: GameState):
        if state != GameState.NO_WINS:
            msg_box = QMessageBox(QMessageBox.Information, "Game Over", f"Game Over Player {state} wins !!")
            msg_box.exec_()

    def evaluateBoard(self, board: TBoard, last_pos: int) -> int:
        player_at_pos: Player = board.get_piece(last_pos)
        pass

    @staticmethod
    def is_valid_pos(pos: int, bound: int):
        return 0 <= pos < bound
