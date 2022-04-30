from enum import IntEnum, Enum
from typing import Tuple

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


class CBoard:

    def __init__(self, b_row: int, b_col: int):
        self._cells = np.full(b_row * b_col, Player.EMPTY, dtype=Player)
        self._view = self._cells.view().reshape((b_row, b_col))
        self._size = (b_row, b_col)

    def place_piece(self, col: int, turn: Player) -> Tuple[bool, int]:
        view = self._view
        cur_col = view[:, col]
        col_len = len(cur_col)
        is_placed, p_row = False, -1

        for row in range(col_len - 1, -1, -1):
            if view[row][col] == Player.EMPTY:
                view[row][col] = turn
                is_placed, p_row = True, row
                break

        return is_placed, p_row

    def has_won(self, pos:Tuple[int, int]) -> bool:
        pass
    # def get_game_state(self, last_move: int) -> GameState:
    #     player = self._cells[last_move]
    #     size = self._size
    #     if self._cell_count <= 0:
    #         return GameState.TIE
    #
    #     cell_view = self._view
    #     row, col = divmod(last_move, size)
    #
    #     row_check = all(x == player for x in cell_view[row])
    #     if row_check:
    #         return GameState(player)
    #
    #     col_check = all(x == player for x in cell_view[:, col])
    #     if col_check:
    #         return GameState(player)
    #
    #     if row != col and (size - 1) - row != col:  # if the pos is on the diagonal
    #         return GameState.NO_WINS
    #     diag_check = all(x == player for x in np.diag(cell_view))
    #     if diag_check:
    #         return GameState(player)
    #
    #     inv_diag = all(x == player for x in np.fliplr(cell_view).diagonal())
    #     if inv_diag:
    #         return GameState(player)
    #
    #     return GameState.NO_WINS
