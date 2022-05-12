from teon.game.sliding_puzzle.engine.algorithms import ai_play, Search, Heuristic
from teon.game.sliding_puzzle.engine.pboard import PBoard


def test_shortest_moves():
    s_puzzle = [1, 2, 3, 4, 0, 5, 7, 8, 6]
    cboard = PBoard(s_puzzle, 3)
    result = ai_play(cboard, Search.ASTAR, Heuristic.MANHATTAN)
    assert len(result) == 2


def test_right_moves_taken():
    d_puzzle = [1, 0, 3, 4, 2, 5, 7, 8, 6]
    cboard = PBoard(d_puzzle, 3)
    result = ai_play(cboard, Search.ASTAR, Heuristic.MANHATTAN)

    assert len(result) == 2
