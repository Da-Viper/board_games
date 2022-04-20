from typing import Tuple, List

import numpy as np


class PBoard:

    def __init__(self, board: List, size: int):
        self._cells = np.array(board, dtype=np.int8)
        self.goal_hash = hash(tuple(self._cells))
        self._view = self._cells.view().reshape(size, size)
        self._blank_val = 0
        self.blank_idx = divmod(size * size - 1, size)
        self.size = size

    def swap_pos(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        if pos in self.get_blank_neighbours():
            new_row, new_col = self.blank_idx
            pos_row, pos_col = pos

            self.swap_with_blank(pos_row, pos_col)

            return new_row, new_col

        return -1, -1

    def swap_with_blank(self, pos_row: int, pos_col: int):
        view = self._view
        new_row, new_col = self.blank_idx

        pos_val = view[pos_row][pos_col]
        view[new_row][new_col] = pos_val
        view[pos_row][pos_col] = self._blank_val
        self.blank_idx = (pos_row, pos_col)

    def get_blank_neighbours(self):
        size = self.size
        row, col = self.blank_idx
        moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
        return filter(lambda rc: 0 <= rc[0] < size and 0 <= rc[1] < size, moves)
    