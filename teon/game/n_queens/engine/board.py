from dataclasses import dataclass
from enum import IntEnum
from typing import Tuple

import numpy as np
from numpy import ndarray


class Piece(IntEnum):
    Q_VALUE = 1
    EMPTY = 0
    CONFLICT = -1
    FIXED_QUEEN = 2


@dataclass
class Pos:
    has_queen: bool
    is_fixed: bool
    conflicts: np.int8

    def __repr__(self):
        return str(self.conflicts)


class NQueen:

    def __init__(self, board_state: ndarray, _dimension: int) -> None:
        self.dimension = _dimension
        self.pos_states = board_state
        # self.queens_pos = np.zeros((_dimension, _dimension), dtype=np.int8)
        self.queens_pos = 0

        # self.visited_row = np.zeros(_dimension, dtype=np.int8)
        # self.visited_col = np.zeros(_dimension, dtype=np.int8)
        self.fixed_row = np.zeros(_dimension, dtype=bool)
        #
        # dimen_len = 2 * _dimension - 1
        # self.left_diag = np.zeros(dimen_len, dtype=np.int8)
        # self.right_diag = np.zeros(dimen_len, dtype=np.int8)
        self.visited_row = 0
        self.visited_col = 0
        self.left_diag = 0
        self.right_diag = 0
        print(f"created board : {self.pos_states}")

    def place_queen(self, pos: Tuple[int, int]):
        row, col = pos

        self.pos_states[row][col].has_queen = True
        self.queens_pos[row][col] = Piece.Q_VALUE

        for val in self.pos_states[row]:
            val.conflicts += 1
        for val in self.pos_states[:, col]:
            val.conflicts += 1
        for val in np.diag(self.pos_states, k=col - row):
            val.conflicts += 1
        n_row = len(self.pos_states) - 1 - row
        for val in np.diag(np.flipud(self.pos_states), k=col - n_row):
            val.conflicts += 1

    def is_solved(self) -> bool:
        for row in self.queens_pos:
            if np.count_nonzero(row == Piece.Q_VALUE) != 1:
                return False
        return True

    def remove_queen(self, pos: Tuple[int, int]):
        row, col = pos

        self.pos_states[row][col].has_queen = False
        self.queens_pos[row][col] = Piece.EMPTY
        for val in self.pos_states[row]:
            val.conflicts -= 1
        for val in self.pos_states[:, col]:
            val.conflicts -= 1
        for val in np.diag(self.pos_states, k=col - row):
            val.conflicts -= 1
        n_row = len(self.pos_states) - 1 - row
        for val in np.diag(np.flipud(self.pos_states), k=col - n_row):
            val.conflicts -= 1

    def reset(self):
        dimension = self.dimension
        state_flatten = self.pos_states.flatten()
        for pos in state_flatten:
            pos.conflicts = 0
            pos.has_queen = False
            pos.is_fixed = False

        self.queens_pos = np.zeros((dimension, dimension), dtype=np.int8)
        self.reset_fixed_places()

    def reset_fixed_places(self):
        """
        Reset the positions of all the fixed queens on the board
        """
        dimension = self.dimension
        self.visited_row = 1 << dimension
        self.visited_col = 1 << dimension
        self.fixed_row = np.zeros(dimension, dtype=bool)

        dimen_len = 2 * dimension - 1
        self.left_diag = 1 << dimen_len
        self.right_diag = 1 << dimen_len

    def set_default_queens(self):
        """
        Set the position of the fixed queens on the board
        :return:
        """
        self.reset_fixed_places()
        board = self.queens_pos
        fixed_row = self.fixed_row
        dimension = self.dimension
        offset = dimension - 1

        for row, r_val in enumerate(board):
            for col, c_val in enumerate(r_val):
                if c_val == Piece.Q_VALUE:
                    pos = row * dimension + 1
                    # board[row][col] = Piece.FIXED_QUEEN
                    board |= 1 << pos

                    self.visited_col |= 1 << col
                    self.visited_row |= 1 << row
                    fixed_row[row] = 1
                    self.left_diag |= 1 << (offset + col - row)
                    self.right_diag |= 1 << (col + row)
