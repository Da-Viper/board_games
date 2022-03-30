from game.player import Player


class Settings:
    FORCE_CAPTURE: bool = False
    FIRST_MOVE: Player = Player.HUMAN
    AI_DEPTH: int = 7
    UNDO_MEM: int = 20
    HEURISTIC: int = 1
