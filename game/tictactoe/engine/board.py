from enum import IntEnum, Enum

import numpy as np


class Player(IntEnum):
    ONE = -2
    TWO = 2
    EMPTY = 0


class GameState(IntEnum):
    ONE_WINS = -2
    TWO_WINS = 2
    NO_WINS = 0
    TIE = -1


class TBoard:

    def __init__(self, size: int = 3):
        self._cells = np.zeros([size * size], dtype=np.int8)
        self._view = self._cells.view().reshape(size, size)
        self._size = size
        self._cell_count = len(self._cells)

    def place_piece(self, player: Player, pos: int) -> bool:
        if self.can_place_piece(pos):
            self._cells[pos] = player
            self._cell_count += 1
            return True
        return False

    def get_piece(self, pos: int) -> Player:
        return self._cells[pos]

    def can_place_piece(self, pos: int) -> bool:
        print(f"cells {self._cells}")
        return self._is_valid_pos(pos) and self._cells[pos] == Player.EMPTY

    def _is_valid_pos(self, pos: int) -> bool:
        return 0 <= pos < self._size * self._size

    def get_game_state(self, last_move: int) -> GameState:
        player = self._cells[last_move]
        size = self._size
        if self._cell_count <= 0:
            return GameState.TIE

        cell_view = self._view
        row, col = divmod(last_move, size)

        row_check = all(x == player for x in cell_view[row])
        if row_check:
            return GameState(player)

        col_check = all(x == player for x in cell_view[:, col])
        if col_check:
            return GameState(player)

        if row != col and (size - 1) - row != col:  # if the pos is on the diagonal
            return GameState.NO_WINS
        diag_check = all(x == player for x in np.diag(cell_view))
        if diag_check:
            return GameState(player)

        inv_diag = all(x == player for x in np.fliplr(cell_view).diagonal())
        if inv_diag:
            return GameState(player)

        return GameState.NO_WINS
