import random

import numpy as np
import pytest

from teon.game.connect4.engine.board import CBoard, Player


@pytest.fixture
def board() -> CBoard:
    width, height = 6, 7
    board = CBoard(width, height)
    return board


def test_undo_connect4_board(board: CBoard):
    b_width, b_height = 6, 7
    lowest_row = 5
    p_col = 2

    result_board = np.full([b_width, b_height], Player.EMPTY, dtype=Player)
    player = Player.ONE

    board.place_piece(p_col, player)
    result_board[lowest_row][p_col] = player

    assert str(board) == str(result_board)
    board.undo()
    result_board[lowest_row][p_col] = Player.EMPTY

    assert str(board) == str(result_board)


def test_place_piece(board: CBoard) -> None:
    b_width, b_height = 6, 7
    lowest_row = 5
    p_col = 2

    result_board = np.full([b_width, b_height], Player.EMPTY, dtype=Player)
    player = Player.ONE

    board.place_piece(p_col, player)
    result_board[lowest_row][p_col] = player

    assert str(board) == str(result_board)


def test_last_turn(board: CBoard) -> None:
    row_len, col_len = 6, 7
    rand_pos = random.choice(range(col_len))

    board.place_piece(rand_pos, Player.ONE)

    assert board.last_pos[1] == rand_pos


def test_full_column(board: CBoard) -> None:
    col_to_place = 2
    player = Player.ONE
    is_placed, row = False, -1
    for i in range(6):
        board.place_piece(col_to_place, player)

    # try to place one more piece should not work
    result = board.place_piece(col_to_place, player)
    assert result == (is_placed, row)
