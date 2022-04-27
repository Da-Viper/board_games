from enum import Enum


class GameResponse(Enum):
    FORCED_JUMP = "You're forced to take."
    PIECE_BLOCKED = "This piece has no diagonal moves."
