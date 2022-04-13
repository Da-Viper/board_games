from enum import IntEnum

import numpy as np


class Player(IntEnum):
    ONE = -2
    TWO = 2
    EMPTY = 0


class TBoard:

    def __init__(self, size: int = 3):
        self.cells = np.empty([size * size], dtype=np.int8)

    def eval_board(self, last_move: int):
        pass
