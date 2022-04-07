from typing import List

from game.player import Player


class Piece:

    def __init__(self, player_type: Player, is_king: bool):
        self.player = player_type
        self.is_king = is_king

    def get_type(self):
        return self.player

    def y_moves(self) -> List[int]:
        if self.is_king:
            return [-1, 1]
        else:
            return [1] if self.player is Player.AI else [-1]

    @staticmethod
    def x_moves() -> List[int]:
        return [-1, 1]
