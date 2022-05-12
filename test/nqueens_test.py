from typing import Callable, Any, Dict

import numpy as np
import pytest

from teon.game.n_queens.engine.algorithm import get_sol
from teon.game.n_queens.engine.board import NQueen, Pos
from teon.game.n_queens.gui.tile import Tile


@pytest.fixture
def gen_board(**kwargs) -> Callable[[Dict[str, Any]], NQueen]:
    """ This is a fixture used for testing the nqueens
        you can create a random board in the right way """
    def _gen_board_helper(**kwargs) -> NQueen:
        size = kwargs.pop("size", 8)

        tiles = np.empty((size, size), dtype=Tile)
        for i in range(size * size):
            row, col = divmod(i, size)
            nqueen_pos = Pos(False, False, np.int8(0))
            tiles[row][col] = nqueen_pos

        n_queen = NQueen(tiles, size)
        return n_queen

    return _gen_board_helper


def test_generate_solution(gen_board: Callable) -> None:
    board_8: NQueen = gen_board(size=8)
    result_8 = get_sol(board_8)
    assert len(result_8) == 92

    board_4: NQueen = gen_board(size=4)
    result_4 = get_sol(board_4)
    assert len(result_4) == 2


def test_removing_queen(gen_board: Callable) -> None:
    board_8: NQueen = gen_board(size=8)
    row, col = (1, 2)
    board_8.place_queen((row, col))
    piece: Pos = board_8.pos_states[row][col]

    assert piece.conflicts == 4
    board_8.remove_queen((row, col))
    piece: Pos = board_8.pos_states[row][col]
    assert piece.conflicts == 0
    assert piece.is_fixed is False
    assert piece.has_queen is False


def test_conflict_position(gen_board: Callable) -> None:
    board_8: NQueen = gen_board(size=8)
    row, col = (1, 2)
    board_8.place_queen((row, col))
    piece: Pos = board_8.pos_states[row][col]

    assert piece.conflicts == 4

