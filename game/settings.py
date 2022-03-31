from game.player import Player


class Settings:
    FORCE_CAPTURE: bool = False
    FIRST_MOVE: Player = Player.HUMAN
    AI_DEPTH: int = 7
    UNDO_MEM: int = 20
    HEURISTIC: int = 1
    T_WIDTH = 8
    T_HEIGHT = 8
    T_DIMEN = T_WIDTH
    SQUARE_NO = T_WIDTH * T_HEIGHT

    G_WIDTH: int = T_WIDTH * 10
    G_HEIGHT: int = T_HEIGHT * 10
    G_DIMEN = T_DIMEN * 10
