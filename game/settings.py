from game.player import Player


class Settings:
    FORCE_CAPTURE: bool = True
    FIRST_MOVE: Player = Player.HUMAN
    AI_DEPTH: int = 8
    UNDO_MEM: int = 20
    HEURISTIC: int = 2
    T_WIDTH = 8
    T_HEIGHT = 8
    BOARD_DIMEN = T_WIDTH
    SQUARE_NO = T_WIDTH * T_HEIGHT

    G_WIDTH: int = T_WIDTH * 10
    G_HEIGHT: int = T_HEIGHT * 10
    G_BOARD_DIMEN = BOARD_DIMEN * G_WIDTH
    G_SQUARE_NO = G_WIDTH * G_HEIGHT

    MAX_VALUE = 2147483647
    MIN_VALUE = -2147483648
