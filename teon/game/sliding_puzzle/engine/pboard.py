from enum import IntEnum
from typing import Tuple, List, Sequence, NamedTuple

import numpy as np

Move = NamedTuple("Move", [("row", int), ("col", int)])


class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class PBoard:

    def __init__(self, board: List, size: int):
        # self.puzzle = np.array(board, dtype=np.int8)
        self.puzzle = board
        self.goal_hash = hash(tuple(self.puzzle))
        # self._view = self.puzzle.view().reshape(size, size)
        self._blank_val = 0
        self.blank_idx = divmod(board.index(0), size)
        self.size = size

    def move_piece(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """
        Check if the blank piece can slide to the current position
        if yes return the new position else return -1,-1
        Args:
            pos:

        Returns:

        """
        if pos in self.get_blank_neighbours():
            new_row, new_col = self.blank_idx
            pos_row, pos_col = pos

            self.swap_with_blank(pos_row, pos_col)

            return new_row, new_col

        return -1, -1

    def undo_move(self):
        pass

    def swap_with_blank(self, pos_row: int, pos_col: int):
        """swap the position of the blank with the new give position"""
        puzzle = self.puzzle
        new_row, new_col = self.blank_idx
        blank_pos = new_row * self.size + new_col
        piece_pos = pos_row * self.size + pos_col

        puzzle[blank_pos], puzzle[piece_pos] = puzzle[piece_pos], puzzle[blank_pos]

        self.blank_idx = (pos_row, pos_col)

    def get_blank_neighbours(self):
        """Get the tile around the blank tile """
        size = self.size
        row, col = self.blank_idx
        moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
        return filter(lambda rc: 0 <= rc[0] < size and 0 <= rc[1] < size, moves)

    def is_goal(self, goal: Sequence):
        """check if the board respresentation is the same as the goal """
        return self.puzzle == goal

    def __str__(self) -> str:
        return str(np.reshape(self.puzzle, (-1, self.size)))
