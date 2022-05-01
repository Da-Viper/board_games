import copy
import time
from typing import List, Tuple

import numpy as np
from numba import njit, vectorize

from teon.game.n_queens.engine.board import NQueen, Piece


def get_sol(board: NQueen, all_sol: bool = True):
    if all_sol:
        return _all_solution(board, 0, [])
    pass


# def _is_safe(pos: Tuple[int, int], v_row: List, v_col: List, v_ldiag: List, v_rdiag: List):
#     row, col = pos
#     ldiag, rdiag = col - row, col + row
#     if v_row[row] or v_col[col] or v_ldiag[ldiag] or v_rdiag[rdiag]:
#         return False
#
#     return True

def _is_safe(row: int, col: int, v_row: int, v_col: int, v_ldiag: int, v_rdiag: int, offset: int) -> int:
    # row, col = pos
    # ldiag, rdiag = offset + col - row, col + row
    ldiag: int = offset + col - row
    rdiag: int = col + row
    # print(f" index , {row, col, ldiag, rdiag}")
    # print(f"values , {bin(v_row), bin(v_col), bin(v_ldiag), bin(v_rdiag)}")
    if ((v_row >> row) & 1) or ((v_col >> col) & 1) or ((v_ldiag >> ldiag) & 1) or ((v_rdiag >> rdiag) & 1):
        return 0
    return 1


def _all_solution(nqueen: NQueen, row: int, solutions: List) -> List:
    """
    This program uses backtracking to get all the solutions for the fixed queens on the board
    :param row : the starting row
    :param solutions: the list to put the correct boards in
    :return: the list of correct boards
    """
    board = nqueen.queens_pos
    dimension = nqueen.dimension
    offset = dimension - 1
    visited_row = nqueen.visited_row
    visited_col = nqueen.visited_col
    left_diag = nqueen.left_diag
    right_diag = nqueen.right_diag

    # print(f"ldiag, {left_diag}")
    # if at the end add the solution
    if row >= dimension:
        solutions.append(copy.deepcopy(board))
        return solutions

    # if the row contains a fixed queen skip the row
    if nqueen.fixed_row[row]:
        _all_solution(nqueen, row + 1, solutions)

    for col in range(dimension):

        # check if there is a queen in the row, column, left diagonal and right diagonal
        # if nqueen._is_safe((row, col)):
        # print(f"inner : {row, col, left_diag, right_diag}")
        if _is_safe(row, col, visited_row, visited_col, left_diag, right_diag, offset):
            # board[row][col] = Piece.Q_VALUE
            pos = row * dimension + col
            nqueen.queens_pos |= 1 << pos
            ldiag, rdiag = offset + col - row, col + row

            # set the row, col, left diagonal, right diagonal  as having a queen
            nqueen.visited_row |= 1 << row
            nqueen.visited_col |= 1 << col
            nqueen.left_diag |= 1 << ldiag
            nqueen.right_diag |= 1 << rdiag
            # visited_row[row], visited_col[col] = 1, 1
            # left_diag[ldiag], right_diag[rdiag] = 1, 1

            # go to the next row
            _all_solution(nqueen, row + 1, solutions)

            # we backtrack here
            # board[row][col] = Piece.EMPTY

            # set it back to the default
            nqueen.queens_pos &= ~(1 << pos)
            nqueen.visited_row &= ~(1 << row)
            nqueen.visited_col &= ~(1 << col)
            nqueen.left_diag &= ~(1 << ldiag)
            nqueen.right_diag &= ~(1 << rdiag)

    return solutions


if __name__ == '__main__':
    board_size = 8
    nqueen_pos = np.empty((board_size, board_size), dtype=np.int8)
    # nqueen_pos = []
    print(nqueen_pos)
    nqueen = NQueen(nqueen_pos, board_size)
    start = time.perf_counter_ns()
    res = get_sol(nqueen)
    end = time.perf_counter_ns()
    print(len(res))
    print(f"Total time take is {(end - start) / 1000000} millis ")

# With bool
# 8 -> 9
# 9 -> 45
# 10 -> 239
# 11 -> 919
# 12 -> 4848
# 13 ->  27946
# 14 -> 173408

# bits
# 8 -> 12
# 9 -> 51
# 10 -> 724
# 11 -> 2680
# 12 -> 4848
# 13 -> 35418
