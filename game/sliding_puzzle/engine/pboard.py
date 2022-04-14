from typing import Tuple, List

import numpy as np


class PBoard:

    def __init__(self, board: List, size: int):
        self._cells = np.array(board, dtype=np.int8)
        self._view = self._cells.view().reshape(size, size)
        self._blank = 0
        self._size = size

    def click_tile(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        old_row, old_col = pos
        view = self._view

        for row, col in self._valid_moves(old_row, old_col):
            curr_val = view[row][col]
            if curr_val == self._blank:
                view[row][col] = view[old_row][old_col]
                view[old_row][old_col] = curr_val
                return row, col
        return -1, -1

    def _valid_moves(self, row: int, col: int):
        size = self._size
        moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
        return filter(lambda rc: 0 <= rc[0] < size and 0 <= rc[1] < size, moves)
