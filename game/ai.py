import random

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
        for b_state in successors:
            val = self.__minimax(b_state, self.depth)
            if val > best_score:
                best_score = val
                equal_bests.clear()

            if val == best_score:
                equal_bests.append(b_state)

        if len(equal_bests) > 1:
            print(f"{self.player} choosing random best move")

        return self.__random_move(equal_bests)

    def __random_move(self, successors: List[BoardState]) -> BoardState:
        successors_len = len(successors)
        if successors_len < 1:
            raise RuntimeError("empty sucessors cant choose a random board")

        rand_num = random.randint(0, successors_len - 1)
        return successors[rand_num]

    def __minimax(self, node: BoardState, depth: int, alpha: int = None, beta: int = None) -> int:
        if alpha is None:
            alpha = Settings.MIN_VALUE  # max
        if beta is None:
            beta = Settings.MAX_VALUE  # min

        if (depth == 0) or node.is_game_over():
            return node.compute_heuristic(self.player)

        # Max player
        if node.turn is self.player:
            v = Settings.MIN_VALUE
            for child in node.get_successors():
                v = max(v, self.__minimax(child, depth - 1, alpha, beta))
                alpha = max(alpha, v)
                if alpha >= beta:
                    break
            return v

        # Min player
        else:
            v = Settings.MAX_VALUE
            for child in node.get_successors():
                v = min(v, self.__minimax(child, depth - 1, alpha, beta))
                beta = min(beta, v)
                if alpha >= beta:
                    break
            return v
