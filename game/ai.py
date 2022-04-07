import random
from itertools import repeat
from multiprocessing import Pool

from typing import List

from game.boardstate import BoardState
from game.player import Player
from game.settings import Settings


class AI:

    def __init__(self, depth: int = Settings.AI_DEPTH, player: Player = Player.AI):
        self.depth = depth
        self.player = player

    def move(self, state: BoardState, player: Player):
        if state.turn is player:
            successors = state.get_successors()
            rv = self.__minimax_move(successors)
            print(f"minimax {rv}")
            return rv

    def __minimax_move(self, successors: List[BoardState]) -> BoardState:
        if len(successors) == 1:
            return successors[0]

        best_score = Settings.MIN_VALUE
        equal_bests = []
        depth_ = self.depth

        # use multiprocessing
        with Pool() as pl:
            result = pl.starmap(self.minimax_, zip(repeat(depth_), successors))

            for i, val in enumerate(result):
                if val > best_score:
                    best_score = val
                    equal_bests.clear()

                if val == best_score:
                    equal_bests.append(successors[i])

        if len(equal_bests) > 1:
            print(f"{self.player} choosing random best move")

        return self.__random_move(equal_bests)

    @staticmethod
    def __random_move(successors: List[BoardState]) -> BoardState:
        successors_len = len(successors)
        if successors_len < 1:
            raise RuntimeError("empty sucessors cant choose a random board")

        rand_num = random.randint(0, successors_len - 1)
        return successors[rand_num]

    def minimax_(self, depth: int, node: BoardState, alpha: int = None, beta: int = None) -> int:
        if (depth == 0) or node.is_game_over():
            return node.compute_heuristic(self.player)

        if alpha is None:
            alpha = Settings.MIN_VALUE  # max
        if beta is None:
            beta = Settings.MAX_VALUE  # min

        # Max player
        if node.turn is self.player:
            v = Settings.MIN_VALUE
            for child in node.get_successors():
                v = max(v, self.minimax_(depth - 1, child, alpha, beta))
                alpha = max(alpha, v)
                if alpha >= beta:
                    break
            return v

        # Min player
        else:
            v = Settings.MAX_VALUE
            for child in node.get_successors():
                v = min(v, self.minimax_(depth - 1, child, alpha, beta))
                beta = min(beta, v)
                if alpha >= beta:
                    break
            return v
