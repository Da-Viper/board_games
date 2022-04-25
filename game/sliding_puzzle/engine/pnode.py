from typing import Sequence, Tuple

from game.sliding_puzzle.engine.pboard import PBoard, Move, Direction


class PNode:

    def __init__(self, board: PBoard, depth: int = 0,
                 heuristic: int = 0, action: Tuple[Move, Direction] = ()):
        self.heuristic = heuristic
        self.depth = depth
        self._board = board
        self.history = action

    @property
    def f_value(self):
        return self.depth + self.heuristic

    @property
    def puzzle(self):
        return self._board.puzzle

    @property
    def size(self):
        return self._board.size

    def play_move(self, move: Move):
        self._board.move_piece(move)

    def generate_moves(self):
        board = self._board
        dimen = board.size
        row, col = board.blank_idx
        moves = ((Move(row + 1, col), Direction.DOWN),
                 (Move(row - 1, col), Direction.UP),
                 (Move(row, col - 1), Direction.LEFT),
                 (Move(row, col + 1), Direction.RIGHT))
        return ((m, direction) for m, direction in moves if 0 <= m.row < dimen and 0 <= m.col < dimen)

    def is_goal(self, goal: Sequence):
        return self._board.is_goal(goal)

    def __hash__(self):
        return hash(tuple(self._board.puzzle))

    def __lt__(self, other) -> bool:
        if self.f_value != other.f_value:
            return self.f_value < other.f_value

        return self.heuristic < other.heuristic

    def __le__(self, other) -> bool:
        return self.f_value <= other.f_value

    def __str__(self):
        return str(self.puzzle)
