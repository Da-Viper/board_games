from PySide2.QtCore import Slot, QObject
from PySide2.QtWidgets import QPushButton

from game.tictactoe.engine.board import TBoard, Player
from game.tictactoe.gui.tile import Tile


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

        self.current_player *= -1

    def update(self, tile: QPushButton):
        print(f"clicked button {self.view.ui.board_grid.indexOf(tile)}")

    @staticmethod
    def is_valid_pos(pos: int, bound: int):
        return 0 <= pos < bound
