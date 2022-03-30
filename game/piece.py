from game.player import Player

class Piece:

    def __init__(self, player_type: Player, is_king: bool):
        self.player = player_type
        self.is_king = is_king

    def get_type(self):
        return self.player

    def get_y_movements(self) -> list[int]:
        if self.is_king:
            return [-1, 1]
        else:
            if self.player.AI:
                return [1]
            else:
                return [-1]

    def get_x_movements(self) -> list[int]:
        return [-1, 1]
