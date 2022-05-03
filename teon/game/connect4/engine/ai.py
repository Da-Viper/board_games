from math import inf

from teon.game.connect4.engine.board import CBoard


def minimax(board: CBoard, depth: int, alpha: int, beta: int, max_player):
    if (depth == 0) or board.is_terminal():
        return board.heuristic()

    open_pos = board.open_pos()

    if max_player:
        value = -inf

        for play in open_pos:
            value = max(value, minimax(play, depth - 1, alpha, beta, not max_player))
            if value >= beta:
                break
            alpha = max(alpha, value)
        return value
    else:
        value = inf
        for play in open_pos:
            value = min(value, minimax(play, depth - 1, alpha, beta, max_player))
            if value <= alpha:
                break
            beta = min(beta, value)

        return value
