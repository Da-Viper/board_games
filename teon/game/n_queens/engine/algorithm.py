import copy
import time
from typing import List, Tuple

import numpy as np

from teon.game.n_queens.engine.board import NQueen, Piece


def get_sol(board: NQueen, all_sol: bool = True):
    if all_sol:
        return _all_solution(board, 0, [])
    pass


def _is_safe(pos: Tuple[int, int], v_row: List, v_col: List, v_ldiag: List, v_rdiag: List):
    row, col = pos
    ldiag, rdiag = col - row, col + row
    if v_row[row] or v_col[col] or v_ldiag[ldiag] or v_rdiag[rdiag]:
        return False

    return True


def _all_solution(nqueen: NQueen, row: int, solutions: List) -> List:
    """
    This program uses backtracking to get all the solutions for the fixed queens on the board
    :param row : the starting row
    :param solutions: the list to put the correct boards in
    :return: the list of correct boards
    """
    board = nqueen.queens_pos
    dimension = nqueen.dimension
    visited_row = nqueen.visited_row
    visited_col = nqueen.visited_col
    left_diag = nqueen.left_diag
    right_diag = nqueen.right_diag

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
        if _is_safe((row, col), visited_row, visited_col, left_diag, right_diag):
            board[row][col] = Piece.Q_VALUE
            ldiag, rdiag = col - row, col + row

            # set the row, col, left diagonal, right diagonal  as having a queen
            visited_row[row], visited_col[col] = True, True
            left_diag[ldiag], right_diag[rdiag] = True, True

            # go to the next row
            _all_solution(nqueen, row + 1, solutions)

            # we backtrack here
            board[row][col] = Piece.EMPTY

            # set it back to the default
            visited_row[row], visited_col[col] = False, False
            left_diag[ldiag], right_diag[rdiag] = False, False

    return solutions


if __name__ == '__main__':
    board_size = 12
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
