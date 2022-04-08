from enum import IntEnum


class Player(IntEnum):
    AI = 0
    HUMAN = 1


def get_opposite(ptype: Player) -> Player:
    return Player.AI if ptype is Player.HUMAN else Player.HUMAN
