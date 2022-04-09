import itertools
from typing import Iterable, Tuple

from game.player import Player


class Piece:

    def __init__(self, player_type: Player, is_king: bool):
        self.player = player_type
        self.is_king = is_king

    def pos_moves(self) -> Iterable[Tuple[int, int]]:
        x_moves = (-1, 1)
        if self.is_king:
            y_moves = (-1, 1)
        else:
            if self.player is Player.AI:
                y_moves = (1,)
            else:
                y_moves = (-1,)
        return itertools.product(x_moves, y_moves)
