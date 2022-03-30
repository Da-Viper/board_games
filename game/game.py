from collections import deque
from game.boardstate import BoardState
from game.ai import AI
from game.settings import Settings
from game.player import Player
from game.movefeedback import MoveFeedBack


class Game:
    __state: deque[BoardState] = deque()
    __memory: int = Settings.UNDO_MEM
    __ai: AI = AI()

    def __init__(self):
        self.__state.append(BoardState())

    def playerMove(self, new_state: BoardState):
        if self.is_over() and self.state_peek().getTurn() == Player.HUMAN:
            self.__update_state(new_state)

    def playerMove(self, from_pos: int, dx: int, dy: int) -> MoveFeedBack:
        to_pos: int = from_pos + dx + BoardState.SIDE_LENGTH * dy
        if to_pos > self.getState().state.length:  # change
            return MoveFeedBack.NOT_ON_BOARD

        jump_successors: list[BoardState] = self.state_peek().get_successors(True)
        can_jump: bool = len(jump_successors) > 0
        if can_jump:
            for succ in jump_successors:
                if succ.get_from_pos == from_pos and succ.get_to_pos == to_pos:
                    self.__update_state(succ)
                    return MoveFeedBack.SUCCESS

            return MoveFeedBack.FORCED_JUMP

        if abs(dx) != abs(dy):
            return MoveFeedBack.NOT_DIAGONAL

        if self.get_state().state[to_pos] is not None:
            return MoveFeedBack.NO_FREE_SPACE

        non_jump_successors: list[BoardState] = self.state_peek().get_successor(from_pos, False)

        for succ in non_jump_successors:
            if succ.get_from_pos() == from_pos and succ.get_to_pos() == to_pos:
                self.__update_state()
                return MoveFeedBack.SUCCESS

        if dy > 1:
            return MoveFeedBack.NO_BACKWARD_MOVES_FOR_SINGLES

        if abs(dx) == 2:
            return MoveFeedBack.ONLY_SINGLE_DIAGONALS

        return MoveFeedBack.UNKNOWN_INVALID

    def move_feedback_click(self) -> MoveFeedBack:
        jump_successors: list[BoardState] = self.state_peek().get_successors(True)
        if len(jump_successors) > 0:
            return MoveFeedBack.FORCED_JUMP
        else:
            return MoveFeedBack.PIECE_BLOCKED

    def get_valid_moves(self, pos: int):
        return self.state_peek().get_successors(pos)
    
    
    def ai_move(self):
        if not self.is_over() and self.state_peek().get_turn() == Player.AI:
            new_state: BoardState = self.__ai.move(self.state_peek(), Player.AI)
            self.__update_state(new_state)

    def state_peek(self):
        return self.__state[len(self.__state) - 1]

    def __update_state(self, new_state: BoardState):
        self.__state.append(new_state)
        if len(self.__state) > self.__memory:
            self.__state.remove(self.__state[0])
