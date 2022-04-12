import numpy as np


class TBoard:

    def __init__(self, size: int = 3):
        self.cells = np.empty([size * size], dtype=np.int8)
