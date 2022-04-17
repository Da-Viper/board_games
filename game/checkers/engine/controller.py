from collections import deque
from typing import List

from game.checkers.engine.snode import SNode
from game.checkers.engine import AI
from game.settings import Settings
from game.checkers.engine.player import Player
from game.gameresponse import GameResponse


class Controller:

    def __init__(self):
        self.prev_states: deque[SNode] = deque()
        self.prev_states.append(SNode.initialize_board())
        self._undo_size = Settings.UNDO_MEM
        self._human_won = False

    def player_move(self, new_state: SNode):
        if not self.is_over() and (self._last_state().get_turn() is Player.HUMAN):
            self._update_state(new_state)

    def move_feedback_click(self) -> GameResponse:
        jump_successors: List[SNode] = self._last_state().get_possible_state(True)
        if len(jump_successors) > 0:
            return GameResponse.FORCED_JUMP
        else:
            return GameResponse.PIECE_BLOCKED

    def get_valid_moves(self, pos: int):
        return self._last_state().get_states_from_position(pos)

    def ai_move(self):
        if not self.is_over() and self.get_turn() == Player.AI:
            new_state: SNode = AI.move(self._last_state(), Player.AI)
            self._update_state(new_state)

    def get_state(self) -> SNode:
        return self._last_state()

    def get_turn(self) -> Player:
        return self._last_state().get_turn()

    def is_over(self) -> bool:
        is_over: bool = self.get_state().is_game_over()
        if is_over:
            self._human_won = self.get_state().piece_count.get(Player.AI) == 0
        return is_over

    def get_game_over_message(self):
        result: str = "Game over. "
        if self._human_won:
            result += "YOU WIN"
        else:
            result += "YOU LOSE"

        return result

    def undo(self):
        if len(self.prev_states) > 2:
            self.prev_states.pop()
            while self.get_state().get_turn() == Player.AI:
                self.prev_states.pop()

    def _last_state(self):
        return self.prev_states[-1]

    def _update_state(self, new_state: SNode):
        self.prev_states.append(new_state)
        if len(self.prev_states) > self._undo_size:
            self.prev_states.remove(self.prev_states[0])
