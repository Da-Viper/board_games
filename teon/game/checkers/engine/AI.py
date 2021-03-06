import random
from functools import lru_cache
from itertools import repeat
from multiprocessing import Pool

from typing import List
from math import inf

from teon.game.checkers.engine.snode import SNode
from teon.game.checkers.engine.player import Player
from teon.game.checkers.engine.settings import Settings


def move(state: SNode, player: Player):
    if state.turn is player:
        generated_states = state.get_all_states()
        return _minimax_move(generated_states, player)


def _minimax_move(successors: List[SNode], max_player: Player) -> SNode:
    """Perform alphabeta with multiprocessing """
    if len(successors) == 1:
        return successors[0]

    best_score = -inf
    equal_bests = []
    depth_ = Settings.AI_DEPTH
    res = "AI" if max_player == 0 else "HUMAN"

    # use multiprocessing
    with Pool() as pl:
        result = pl.starmap(_alpha_beta, zip(repeat(depth_), successors, repeat(-inf), repeat(inf)))

        for i, val in enumerate(result):
            if val > best_score:
                best_score = val
                equal_bests.clear()

            if val == best_score:
                equal_bests.append(successors[i])
    return random.choice(successors)


@lru_cache(maxsize=None)
def _alpha_beta(depth: int, node: SNode, alpha: int = -inf, beta: int = inf) -> int:
    """Perform alpha beta depending on whose turn it is"""

    if (depth == 0) or node.is_game_over():
        return node.compute_heuristic(Player.AI)

    node_states = node.get_all_states()
    node_states.sort(key=lambda x: x.compute_heuristic(node.turn))

    # Max player
    if node.turn is Player.AI:
        val = -inf
        for child in node_states:
            val = max(val, _alpha_beta(depth - 1, child, alpha, beta))
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return val

    # Min player
    else:
        val = inf
        for child in node_states:
            val = min(val, _alpha_beta(depth - 1, child, alpha, beta))
            beta = min(beta, val)
            if alpha >= beta:
                break
        return val
