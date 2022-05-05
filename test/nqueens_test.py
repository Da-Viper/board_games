from typing import Callable, Any, Dict

import numpy as np
import pytest

from teon.game.n_queens.engine.algorithm import get_sol
from teon.game.n_queens.engine.board import NQueen


@pytest.fixture
def gen_board(**kwargs) -> Callable[[Dict[str, Any]], NQueen]:
    def _gen_board_helper(**kwargs) -> NQueen:
        size = kwargs.pop("size", 8)

        b_state = np.empty((size, size), dtype=np.int8)
        n_queen = NQueen(b_state, size)
        return n_queen

    return _gen_board_helper


def test_generate_solution(gen_board: Callable) -> None:
    board_8: NQueen = gen_board(size=8)
    result_8 = get_sol(board_8)
    assert len(result_8) == 92

    board_4: NQueen = gen_board(size=4)
    result_4 = get_sol(board_4)
    assert len(result_4) == 2


def test_fixed_pieces_(queen_4: NQueen) -> None:
    print(queen_4)
    pass


def test_removing_queen(gen_board: Callable) -> None:
    pass


def test_conflict_position(gen_board: Callable) -> None:
    pass


def test_one_solution(gen_board: Callable) -> None:
    pass
