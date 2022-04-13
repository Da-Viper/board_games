from enum import IntEnum

import numpy as np


class Player(IntEnum):
    ONE = -2
    TWO = 2
    EMPTY = 0


class TBoard:

    def __init__(self, size: int = 3):
        self._cells = np.zeros([size * size], dtype=np.int8)
        self._cell_count = len(self._cells)

    def place_piece(self, player: Player, pos: int) -> bool:
        if self.can_place_piece(pos):
            self._cells[pos] = player
            return True
        return False

    def can_place_piece(self, pos: int) -> bool:
        print(f"cells {self._cells}")
        return self._is_valid_pos(pos) and self._cells[pos] == Player.EMPTY

    def _is_valid_pos(self, pos: int) -> bool:
        return 0 <= pos < self._cell_count

    def eval_board(self, last_move: int):
        pass
