from collections import deque

from typing import List

from game.boardstate import BoardState
from game.ai import AI
from game.settings import Settings
from game.player import Player
from game.movefeedback import MoveFeedBack


class Game:

    def __init__(self):
        self.__memory = Settings.UNDO_MEM
        self.__state: deque[BoardState] = deque()
        self.__state.append(BoardState())
        self.__ai = AI(Settings.AI_DEPTH)
        self.__human_won = False

    def player_move(self, new_state: BoardState):
        if not self.is_over() and (self.state_peek().get_turn() is Player.HUMAN):
            self.__update_state(new_state)

    def playerMove(self, from_pos: int, dx: int, dy: int) -> MoveFeedBack:
        to_pos: int = from_pos + dx + BoardState.SIDE_LENGTH * dy
        if to_pos > len(self.get_state().state):
            return MoveFeedBack.NOT_ON_BOARD

        jump_successors: list[BoardState] = self.state_peek().get_successors_jump(True)
        can_jump: bool = len(jump_successors) > 0
        if can_jump:
            for succ in jump_successors:
                if succ.get_from_pos() == from_pos and succ.get_to_pos == to_pos:
                    self.__update_state(succ)
                    return MoveFeedBack.SUCCESS

            return MoveFeedBack.FORCED_JUMP

        if abs(dx) != abs(dy):
            return MoveFeedBack.NOT_DIAGONAL

        if self.get_state().state[to_pos] is not None:
            return MoveFeedBack.NO_FREE_SPACE

        non_jump_successors: List[BoardState] = self.state_peek().get_successors_pos_jump(from_pos, False)

        for succ in non_jump_successors:
            if succ.get_from_pos() == from_pos and succ.get_to_pos() == to_pos:
                self.__update_state(succ)
                return MoveFeedBack.SUCCESS

        if dy > 1:
            return MoveFeedBack.NO_BACKWARD_MOVES_FOR_SINGLES

        if abs(dx) == 2:
            return MoveFeedBack.ONLY_SINGLE_DIAGONALS

        return MoveFeedBack.UNKNOWN_INVALID

    def move_feedback_click(self) -> MoveFeedBack:
        jump_successors: List[BoardState] = self.state_peek().get_successors_jump(True)
        if len(jump_successors) > 0:
            return MoveFeedBack.FORCED_JUMP
        else:
            return MoveFeedBack.PIECE_BLOCKED

    def get_valid_moves(self, pos: int):
        return self.state_peek().get_successors_pos(pos)

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
