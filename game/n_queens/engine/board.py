import copy
from enum import IntEnum
from typing import Tuple

import numpy as np
from dataclasses import dataclass

from numpy import ndarray

Q_VALUE = "Q"
EMPTY = "_"
FIXED_QUEEN = "F"


class Piece(IntEnum):
    Q_VALUE = 1
    EMPTY = 0
    CONFLICT = -1


@dataclass
class Pos:
    has_queen: bool
    conflicts: np.int8

    def __repr__(self):
        return str(self.conflicts)


class NQueen:

    def __init__(self, board_state: ndarray, _dimension: int) -> None:
        self.dimension = _dimension
        # self.board = np.full((_dimension, _dimension), Piece.EMPTY, dtype=np.int8)
        self.board = board_state
        self.conflicts = np.zeros((_dimension, _dimension), dtype=np.int8)

        self.visited_row = np.zeros(_dimension, dtype=np.int8)
        self.visited_col = np.zeros(_dimension, dtype=np.int8)

        dimen_len = 2 * _dimension - 1
        self.left_diag = np.zeros(dimen_len, dtype=np.int8)
        self.right_diag = np.zeros(dimen_len, dtype=np.int8)
        print(f"created board : {self.board}")

    def generate_all_solutions(self) -> Tuple[bool, list]:
        solutions = self._all_solution_helper(0, [])
        if solutions:
            return True, solutions
        return False, []

    def place_queen(self, pos: Tuple[int, int]):
        # ldiag, rdiag = col - row, col + row
        row, col = pos

        self.board[row][col].has_queen = True
        self.conflicts[row][col] = Piece.Q_VALUE

        for val in self.board[row]: val.conflicts += 1
        for val in self.board[:, col]:
            val.conflicts += 1
        for val in np.diag(self.board, k=col - row):
            val.conflicts += 1
        n_row = len(self.board) - 1 - row
        for val in np.diag(np.flipud(self.board), k=col - n_row):
            val.conflicts += 1
        # for val in np.flipud(self.board).diagonal( row - col):
        #     val.conflicts += 1
        # # up right diagonal
        # for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        #     if board[i][j] == Q_VALUE:
        #         return False
        #
        # for i, j in zip(range(row, dimension, 1), range(col, dimension, 1)):
        #     if board[i][j] == Q_VALUE:
        #         return False
        #
        # # up left digonal
        # for i, j in zip(range(row, -1, -1), range(col, dimension, 1)):
        #     if board[i][j] == Q_VALUE:
        #         return False
        #
        # for i, j in zip(range(row, dimension, 1), range(col, -1, -1)):
        #     if board[i][j] == Q_VALUE:
        #         return False
        #

    def remove_queen(self, pos: Tuple[int, int]):
        row, col = pos

        self.board[row][col].has_queen = False
        self.conflicts[row][col] = Piece.EMPTY
        for val in self.board[row]:
            val.conflicts -= 1
        for val in self.board[:, col]:
            val.conflicts -= 1
        for val in np.diag(self.board, k=col - row):
            val.conflicts -= 1
        n_row = len(self.board) - 1 - row
        for val in np.diag(np.flipud(self.board), k=col - n_row):
            val.conflicts -= 1

    def _all_solution_helper(self, row: int, solutions: list) -> list:
        """
        This program uses backtracking to get all the solutions for the fixed queens on the board
        :param row : the starting row
        :param solutions: the list to put the correct boards in
        :return: the list of correct boards
        """
        board = self.board
        dimension = self.dimension

        # if at the end add the solution
        if row >= dimension:
            solutions.append(copy.deepcopy(board))
            return solutions

        # if the row contains a fixed queen skip the row
        # if self.fixed_row[row]:
        #     self._all_solution_helper(row + 1, solutions)

        for col in range(dimension):

            # check if there is a queen in the row, column, left diagonal and right diagonal
            if self._is_safe((row, col)):
                board[row][col] = Q_VALUE
                ldiag, rdiag = col - row, col + row

                # set the row, col, left diagonal, right diagonal  as having a queen
                self.visited_row[row], self.visited_col[col] = True, True
                self.left_diag[ldiag], self.right_diag[rdiag] = True, True

                # go to the next row
                self._all_solution_helper(row + 1, solutions)

                # we backtrack here
                board[row][col] = EMPTY

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
