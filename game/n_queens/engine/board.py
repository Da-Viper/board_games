import copy
from enum import IntEnum
from typing import Tuple

import numpy as np
from dataclasses import dataclass

from numpy import ndarray


class Piece(IntEnum):
    Q_VALUE = 1
    EMPTY = 0
    CONFLICT = -1
    FIXED_QUEEN = 2


@dataclass
class Pos:
    has_queen: bool
    conflicts: np.int8

    def __repr__(self):
        return str(self.conflicts)


class NQueen:

    def __init__(self, board_state: ndarray, _dimension: int) -> None:
        self.dimension = _dimension
        self.pos_states = board_state
        self.queens_pos = np.zeros((_dimension, _dimension), dtype=np.int8)

        self.visited_row = np.zeros(_dimension, dtype=bool)
        self.visited_col = np.zeros(_dimension, dtype=bool)
        self.fixed_row = np.zeros(_dimension, dtype=bool)

        dimen_len = 2 * _dimension - 1
        self.left_diag = np.zeros(dimen_len, dtype=bool)
        self.right_diag = np.zeros(dimen_len, dtype=bool)
        print(f"created board : {self.pos_states}")

    def generate_all_solutions(self) -> list:
        self._set_default_queens()
        return self._all_solution_helper(0, [])

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

    def _all_solution_helper(self, row: int, solutions: list) -> list:
        """
        This program uses backtracking to get all the solutions for the fixed queens on the board
        :param row : the starting row
        :param solutions: the list to put the correct boards in
        :return: the list of correct boards
        """
        board = self.queens_pos
        dimension = self.dimension

        # if at the end add the solution
        if row >= dimension:
            solutions.append(copy.deepcopy(board))
            return solutions

        # if the row contains a fixed queen skip the row
        if self.fixed_row[row]:
            self._all_solution_helper(row + 1, solutions)

        for col in range(dimension):

            # check if there is a queen in the row, column, left diagonal and right diagonal
            if self._is_safe((row, col)):
                board[row][col] = Piece.Q_VALUE
                ldiag, rdiag = col - row, col + row

                # set the row, col, left diagonal, right diagonal  as having a queen
                self.visited_row[row], self.visited_col[col] = True, True
                self.left_diag[ldiag], self.right_diag[rdiag] = True, True

                # go to the next row
                self._all_solution_helper(row + 1, solutions)

                # we backtrack here
                board[row][col] = Piece.EMPTY

                # set it back to the default
                self.visited_row[row], self.visited_col[col] = False, False
                self.left_diag[ldiag], self.right_diag[rdiag] = False, False

        return solutions

    def _is_safe(self, pos: Tuple[int, int]) -> bool:
        row, col = pos
        # row and column check
        if self.visited_row[row] or self.visited_col[col]:
            return False

        ldiag, rdiag = col - row, col + row
        # left and right diagonal
        if self.left_diag[ldiag] or self.right_diag[rdiag]:
            return False

        return True

    def reset(self):
        dimension = self.dimension
        state_flatten = self.pos_states.flatten()
        for pos in state_flatten:
            pos.conflicts = 0
            pos.has_queen = False

        self.queens_pos = np.zeros((dimension, dimension), dtype=bool)
        self.reset_fixed_places()

    def reset_fixed_places(self):
        dimension = self.dimension
        self.visited_row = np.zeros(dimension, dtype=bool)
        self.visited_col = np.zeros(dimension, dtype=bool)
        self.fixed_row = np.zeros(dimension, dtype=bool)

        dimen_len = 2 * dimension - 1
        self.left_diag = np.zeros(dimen_len, dtype=bool)
        self.right_diag = np.zeros(dimen_len, dtype=bool)

    def _set_default_queens(self):
        """
        Set the position of the fixed queens on the board
        :param q_list: list of tuples of the fixed queens position
        :return:
        """
        self.reset_fixed_places()
        board = self.queens_pos
        fixed_row = self.fixed_row
        left_diag = self.left_diag
        right_diag = self.right_diag

        for row, r_val in enumerate(board):
            for col, c_val in enumerate(r_val):
                if c_val == Piece.Q_VALUE:
                    self.visited_col[col] = True
                    self.visited_row[row] = True
                    fixed_row[row] = True
                    left_diag[col - row] = True
                    right_diag[col + row] = True
