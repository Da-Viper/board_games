from typing import List

from PySide2.QtCore import Slot

from game.sliding_puzzle.engine.pboard import PBoard
from game.sliding_puzzle.gui.tile import Tile


class PController:

    def __init__(self, board: List, board_size: int):
        self._board = PBoard(board, board_size)

    @Slot(Tile)
    def tile_clicked(self, tile: Tile):
        print(f"\tTile clicked from pos: {tile.idx_pos}")
        new_pos = self._board.get_blank_pos(tile.idx_pos)
        print(f"\tView : \n{self._board._view}")
        tile.new_pos = new_pos
        if new_pos != (-1, -1):
            tile.set_new_pos(new_pos)
