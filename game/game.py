from collections import deque

from typing import List

from game.boardstate import BoardState
from game.ai import AI
from game.settings import Settings
from game.player import Player
from game.gameresponse import GameResponse


class Game:

    def __init__(self):
        self.__memory = Settings.UNDO_MEM
        self.__state: deque[BoardState] = deque()
        self.__state.append(BoardState.initialize_board())
        self.__ai = AI(Settings.AI_DEPTH)
        self.__human_won = False

    def player_move(self, new_state: BoardState):
        if not self.is_over() and (self.state_peek().get_turn() is Player.HUMAN):
            self.__update_state(new_state)

    def move_feedback_click(self) -> GameResponse:
        jump_successors: List[BoardState] = self.state_peek().get_possible_state(True)
        if len(jump_successors) > 0:
            return GameResponse.FORCED_JUMP
        else:
            return GameResponse.PIECE_BLOCKED

    def get_valid_moves(self, pos: int):
        return self.state_peek().get_states_from_position(pos)

    def ai_move(self):
        if not self.is_over() and self.state_peek().get_turn() == Player.AI:
            new_state: BoardState = self.__ai.move(self.state_peek(), Player.AI)
            self.__update_state(new_state)

    def state_peek(self):
        return self.__state[-1]

    def __update_state(self, new_state: BoardState):
        self.__state.append(new_state)
        if len(self.__state) > self.__memory:
            self.__state.remove(self.__state[0])

    def get_state(self) -> BoardState:
        return self.state_peek()

    def get_turn(self) -> Player:
        return self.state_peek().get_turn()

    def is_over(self) -> bool:
        is_over: bool = self.get_state().is_game_over()
        if is_over:
            self.__human_won = self.get_state().piece_count.get(Player.AI) == 0
        return is_over

    def get_game_over_message(self):
        result: str = "Game over. "
        if self.__human_won:
            result += "YOU WIN"
        else:
            result += "YOU LOSE"

        return result

    def undo(self):
        if len(self.__state) > 2:
            self.__state.pop()
            while self.get_state().get_turn() == Player.AI:
                self.__state.pop()
