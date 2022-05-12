import copy
import time
from typing import List, Tuple

import numpy as np

from teon.game.n_queens.engine.board import NQueen, Piece, Pos
from teon.utils import utils


def bit_extracted(number: int, size: int, pos: int):
    return ((1 << size) - 1) & (number >> pos)


def bit_value(number: int, index: int):
    return (number >> index) & 1


def get_sol(board: NQueen, all_sol: bool = True):
    if all_sol:
        return _all_solution(board, 0, [])
        # return new_one(board.queens_pos, board.dimension, 0, board.left_diag,
        #                board.right_diag, board.visited_col, [])

    one_sol = _one_solution(board, 0)
    if one_sol:
        print("One solution ", board.queens_pos)
        return board.queens_pos

        # return another(board.queens_pos, board.dimension, 0, board.visited_row, board.visited_col, board.left_diag,
        #                board.right_diag, board.fixed_row, [])
    # pass


def new_one(board, dimen: int, col, ld, rd, cl, sols: List[int]):
    if col >= dimen:
        sols.append(board.copy())
        # return True

    for i in range(dimen):

        if not ((ld[i - col + dimen - 1] or rd[i + col]) or cl[i]):
            board[i][col] = True
            ld[i - col + dimen - 1] = rd[i + col] = cl[i] = True

            new_one(board, dimen, col + 1, ld, rd, cl, sols)
            # return True

            board[i][col] = False  # BACKTRACK
            ld[i - col + dimen - 1] = rd[i + col] = cl[i] = False

    return sols


# def _is_safe(row: int, col: int, v_row: int, v_col: int, v_ldiag: int, v_rdiag: int, offset: int) -> int:
#     if ((v_row >> row) & 1) or ((v_col >> col) & 1) or ((v_ldiag >> (offset + col - row)) & 1) or (
#             (v_rdiag >> (col + row)) & 1):
#         return 0
#     return 1
# v_row | v_col | v_ldiag | rdiag |


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
    v_row = nqueen.visited_row
    v_col = nqueen.visited_col
    l_diag = nqueen.left_diag
    r_diag = nqueen.right_diag

    # if at the end add the solution
    if row >= dimension:
        solutions.append(copy.deepcopy(board))
        return solutions

    # if the row contains a fixed queen skip the row
    if nqueen.fixed_row[row]:
        _all_solution(nqueen, row + 1, solutions)

    for col in range(dimension):

        ldiag_i, rdiag_i = col - row, col + row
        # check if there is a queen in the row, column, left diagonal and right diagonal
        if not (v_row[row] or v_col[col] or l_diag[ldiag_i] or r_diag[rdiag_i]):
            # set the row, col, left diagonal, right diagonal  as having a queen
            board[row][col] = Piece.Q_VALUE
            v_row[row], v_col[col] = True, True
            l_diag[ldiag_i], r_diag[rdiag_i] = True, True

            # go to the next row
            _all_solution(nqueen, row + 1, solutions)

            # we backtrack here
            board[row][col] = Piece.EMPTY

            # set it back to the default
            v_row[row], v_col[col] = False, False
            l_diag[ldiag_i], r_diag[rdiag_i] = False, False

    return solutions


def _one_solution(nqueen: NQueen, row: int) -> bool:
    board = nqueen.queens_pos
    dimension = nqueen.dimension
    visited_row = nqueen.visited_row
    visited_col = nqueen.visited_col
    left_diag = nqueen.left_diag
    right_diag = nqueen.right_diag

    # if at the end add the solution
    if row >= dimension:
        return True

    # if the row contains a fixed queen skip the row
    if nqueen.fixed_row[row]:
        return _one_solution(nqueen, row + 1)

    for col in range(dimension):

        if _is_safe((row, col), visited_row, visited_col, left_diag, right_diag):
            board[row][col] = Piece.Q_VALUE
            # nqueen.pos_states[row][col].has_queen = False
            nqueen.place_queen((row, col))
            # print("board state", nqueen.queens_pos)

            ldiag, rdiag = col - row, col + row
            # set the row, col, left diagonal, right diagonal  as having a queen
            visited_row[row], visited_col[col] = True, True
            left_diag[ldiag], right_diag[rdiag] = True, True
            utils.qt_sleep(400)

            # go to the next row
            has_sol = _one_solution(nqueen, row + 1)
            if has_sol:
                return has_sol

            # we backtrack here
            nqueen.remove_queen((row, col))
            # set it back to the default
            visited_row[row], visited_col[col] = False, False
            left_diag[ldiag], right_diag[rdiag] = False, False
            utils.qt_sleep(400)

    return False


def another(board, dimen: int, col: int, v_row: int, v_col: int, v_ldiag: int, v_rdiag: int, f_row: List[int],
            solutions):
    offset = dimen - 1
    if col >= dimen:
        solutions.append(copy.deepcopy(board))
        return solutions
    if f_row[col]:
        another(board, dimen, col + 1, v_row, v_col, v_ldiag, v_rdiag, f_row, solutions)

    # while current_open & mask:
    for row in range(dimen):
        if _is_safe(col, row, v_row, v_col, v_ldiag, v_rdiag, offset):
            ldiag, rdiag = offset + row - col, row + col

            board[col][row] = Piece.Q_VALUE
            another(board, dimen, col + 1, v_row | (1 << col), v_col | (1 << row), v_ldiag | (1 << ldiag),
                    v_rdiag | (1 << rdiag), f_row, solutions)
            board[col][row] = Piece.EMPTY

    return solutions


if __name__ == '__main__':
    board_size = 14
    nqueen_pos = np.empty((board_size, board_size), dtype=np.int8)
    # nqueen_pos = [[0] * board_size for _ in range(board_size)]
    # print(nqueen_pos)

    nqueen_b = NQueen(nqueen_pos, board_size)
    start = time.perf_counter_ns()
    res = get_sol(nqueen_b)
    end = time.perf_counter_ns()

    print(len(res))
    # print(res)
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


# classic Array
# 8 -> 5.1
# 9 -> 24
# 10 -> 96
# 11 -> 484
# 12 -> 2438
# 13 -> 14344
# 14 -> 91687