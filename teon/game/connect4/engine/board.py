from enum import IntEnum, Enum
from typing import Tuple, List

import numpy as np


class Player(IntEnum):
    ONE = -2
    TWO = 2
    EMPTY = 0

    def __repr__(self):
        return str(int(self))


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
        self._k = 4
        self.available = [b_row - 1] * b_col
        self.last_pos = (-1, -1)

    def place_piece(self, col: int, turn: Player) -> Tuple[bool, int]:
        """
        Places the piece of the given player on a column
        Args:
            col: the column to place the piece
            turn: the turn of the current player

        Returns:

        """
        view = self._view
        is_placed, p_row = False, -1

        if self.is_available(col):
            pos_row = self.available[col]
            self.available[col] -= 1
            view[pos_row][col] = turn
            self.last_pos = (pos_row, col)
            is_placed, p_row = True, pos_row

        print(view)
        return is_placed, p_row

    def open_pos(self) -> List[int]:
        """
        Show the list of columns that you can place a piece on
        Returns: the open columns

        """
        _, col = self._size
        return [i for i in range(col) if self.available[i] > -1]

    def is_available(self, col: int) -> bool:
        """Checks if you can place a piece on the column"""
        return self.available[col] != 0

    def has_won(self, pos: Tuple[int, int]) -> bool:
        """checks if there is a win after placement in that position"""
        k = 4 - 1
        prow, pcol = pos
        board = self._view
        row_len, col_len = self._size
        piece = board[prow][pcol]

        beg, end = max(0, pcol - k), min(col_len, pcol + 1 + k) - k
        for c in range(beg, end):
            if board[prow][c] == piece and board[prow][c + 1] == piece and board[prow][c + 2] == piece and board[prow][ \
                    c + 3] == piece:
                return True

        beg, end = max(0, prow - k), min(row_len, prow + 1 + k) - k
        for r in range(beg, end):
            if board[r][pcol] == piece and board[r + 1][pcol] == piece and board[r + 2][pcol] == piece and board[r + 3][ \
                    pcol] == piece:
                return True

        for c in range(col_len - 3):
            for r in range(row_len - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        for c in range(col_len - 3):
            for r in range(3, row_len):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True
        return False

    def is_terminal(self):
        """
        Checks if there is a win  or loose
        """
        is_term = False
        if self.last_pos != (-1, -1):
            is_term = self.has_won(self.last_pos)

        is_term or all(elem == -1 for elem in self.open_pos())

    def heuristic(self) -> int:
        return -1

    def undo(self):
        if self.last_pos == (-1, -1):
            return
        row, col = self.last_pos
        self._view[row][col] = Player.EMPTY
        self.available[col] += 1

    def is_tie(self):
        return len(self.open_pos()) == 0

    def __repr__(self) -> str:
        return str(self._view)
