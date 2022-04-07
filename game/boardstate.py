from __future__ import annotations

import collections
from copy import copy

import numpy as np

from game.piece import Piece
from game.player import Player, get_opposite
from game.settings import Settings


class BoardState:
    """
     This class is a logic controller for the current board state.
     This class can also simulate possible states from the current state -
        - for:
                (a) Player movement - attack and non-attack moves
                (b) AI movement (minmax algorithm simulation)
    """

    SIDE_LENGTH = Settings.BOARD_DIMEN
    NO_SQUARES = SIDE_LENGTH * SIDE_LENGTH

    def __init__(self):
        """
            Initialises board attributes to default values.
        """
        self.turn: Player = Settings.FIRST_MOVE
        self.state: list[Piece | None] = [None] * self.NO_SQUARES
        self.piece_count: dict = {Player.AI: 0, Player.HUMAN: 0}
        self.king_count: dict = {Player.AI: 0, Player.HUMAN: 0}
        self.from_pos = -1
        self.to_pos = -1
        self.double_jump_pos = -1

    @staticmethod
    def initialize_board() -> BoardState:
        """
            Method populates initial state with Pieces.
            state contains null/None values for cells that are empty
            state is filled with checker patten in mind
        """
        bs = BoardState()
        bs.turn = Settings.FIRST_MOVE
        SIDE_LENGTH = Settings.BOARD_DIMEN
        cur_state = bs.state
        for i in range(len(cur_state)):
            y = i // SIDE_LENGTH  # row
            x = i % SIDE_LENGTH  # col

            if (x + y) % 2 == 1:  # checks if position is even or odd

                if y < 3:  # row boundary for AI pieces
                    cur_state[i] = Piece(Player.AI, False)
                elif y > 4:  # row boundary for Player pieces
                    cur_state[i] = Piece(Player.HUMAN, False)

        # count the ai and human using collections
        counts = collections.Counter(piece.player for piece in cur_state if piece)
        ai_count = counts.get(Player.AI, 0)
        human_count = counts.get(Player.HUMAN, 0)

        bs.piece_count[Player.AI] = ai_count
        bs.piece_count[Player.HUMAN] = human_count

        bs.king_count[Player.AI] = 0
        bs.king_count[Player.HUMAN] = 0
        return bs

    def deep_copy(self):
        """
        Method used to copy the current state.
        :return: temporary state to simulate player moves from given position
        """
        tmp_board_state = BoardState()
        tmp_board_state.state = np.copy(self.state)
        return tmp_board_state

    def compute_heuristic(self, player: Player) -> int:
        """
        Method used to pick heuristic function
        default is heuristic 1
        :param player:
        :return:
        """
        if Settings.HEURISTIC == 1:
            return self.heuristic1(player)
        return self.heuristic2(player)

    def heuristic1(self, player: Player) -> int:
        """

        :param player:
        :return:
        """
        max_int = Settings.MAX_VALUE
        opp_player = get_opposite(player)
        if self.piece_count[opp_player] == 0:
            return max_int
        if self.piece_count[player] == 0:
            return -max_int

        return self.piece_score(player) - self.piece_score(opp_player)

    def heuristic2(self, player: Player) -> int:
        max_int = Settings.MAX_VALUE
        opp_player = get_opposite(player)
        if self.piece_count[opp_player] == 0:
            return max_int
        if self.piece_count[player] == 0:
            return -max_int

        return self.piece_score(player) // self.piece_score(opp_player)

    def piece_score(self, player: Player) -> int:
        return self.piece_count[player] + self.king_count[player]

    def get_successors(self) -> list[BoardState]:
        successors = self.get_successors_jump(True)
        if Settings.FORCE_CAPTURE:
            has_successors = len(successors) > 0
            if has_successors:
                return successors
            else:
                ss = self.get_successors_jump(False)
                return ss
        else:
            successors.extend(self.get_successors_jump(False))
            return successors

    def get_successors_jump(self, jump: bool) -> list[BoardState]:
        result: list[BoardState] = []
        c_state = self.state
        turn_ = self.turn
        for i in range(len(c_state)):
            cur_piece: Piece = c_state[i]
            if cur_piece is not None:
                if cur_piece.player is turn_:
                    result.extend(self.get_successors_pos_jump(i, jump))
        return result

    def get_successors_pos(self, pos: int) -> list[BoardState]:
        if Settings.FORCE_CAPTURE:
            jumps = self.get_successors_jump(True)
            has_jumps = len(jumps) > 0
            return self.get_successors_pos_jump(pos, has_jumps)
        else:
            result: list[BoardState] = []
            result.extend(self.get_successors_pos_jump(pos, True))
            result.extend(self.get_successors_pos_jump(pos, False))
            return result

    def get_successors_pos_jump(self, pos: int, jump: bool) -> list[BoardState]:
        if self.get_piece(pos).player != self.turn:
            raise ValueError(" This is not your piece in this position ")

        cpiece = self.state[pos]
        if jump:
            return self.jump_successors(cpiece, pos)

        return self.non_jump_successors(cpiece, pos)

    def non_jump_successors(self, piece: Piece, pos: int) -> list[BoardState]:
        result: list[BoardState] = []
        side_length = self.SIDE_LENGTH
        x = pos % side_length
        y = pos // side_length

        for dx in piece.x_moves():
            for dy in piece.y_moves():
                new_x = x + dx
                new_y = y + dy
                if self.__is_valid(new_y, new_x):
                    if self.__get_piece(new_y, new_x) is None:
                        new_pos = side_length * new_y + new_x
                        result.append(self.__create_new_state(pos, new_pos, piece, False, dy, dx))

        return result

    def jump_successors(self, piece: Piece, pos: int) -> list[BoardState]:
        result = []
        side_length = self.SIDE_LENGTH
        djump_pos = self.double_jump_pos

        if (djump_pos > 0) and pos != djump_pos:
            return result

        x = pos % side_length
        y = pos // side_length

        for dx in piece.x_moves():
            for dy in piece.y_moves():
                new_x = x + dx
                new_y = y + dy

                if self.__is_valid(new_y, new_x):
                    if (self.__get_piece(new_y, new_x) is not None) and (
                            self.__get_piece(new_y, new_x).player == get_opposite(piece.player)):
                        new_x += dx
                        new_y += dy
                        if self.__is_valid(new_y, new_x):
                            if self.__get_piece(new_y, new_x) is None:
                                new_pos = side_length * new_y + new_x
                                result.append(self.__create_new_state(pos, new_pos, piece, True, dy, dx))

        return result

    def __create_new_state(self, old_pos: int, new_pos: int, piece: Piece, jumped: bool, dy: int, dx: int):
        result: BoardState = self.deep_copy()
        result.piece_count = copy(self.piece_count)
        result.king_count = copy(self.piece_count)
        # TODO may be missing
        king_conversion = False

        pplayer = piece.player
        if self.__is_king_pos(new_pos, pplayer):
            piece = Piece(pplayer, True)
            king_conversion = True
            result.king_count[pplayer] += 1

        result.state[old_pos] = None
        result.state[new_pos] = piece

        result.from_pos = old_pos
        result.to_pos = new_pos

        opp_player = get_opposite(pplayer)
        result.turn = opp_player

        if jumped:
            result.state[new_pos - self.SIDE_LENGTH * dy - dx] = None
            result.piece_count[opp_player] -= 1

            if len(result.jump_successors(piece, new_pos)) > 0 and king_conversion is False:
                result.turn = pplayer
                result.double_jump_pos = new_pos

        return result

    def __is_king_pos(self, pos: int, player: Player) -> bool:
        y = pos // self.SIDE_LENGTH
        if (y == 0) and player is Player.HUMAN:
            return True
        return (y == self.SIDE_LENGTH - 1) and (player is Player.AI)

    def get_to_pos(self):
        return self.to_pos

    def get_from_pos(self):
        return self.from_pos

    def get_turn(self):
        return self.turn

    def is_game_over(self) -> bool:
        pc = self.piece_count
        return (pc[Player.AI] == 0) or (pc[Player.HUMAN] == 0)

    def get_piece(self, rel_pos: int) -> Piece:
        return self.state[rel_pos]

    def __get_piece(self, y: int, x: int) -> Piece:
        return self.get_piece(self.SIDE_LENGTH * y + x)

    def __is_valid(self, x: int, y: int) -> bool:
        return (0 <= y < self.SIDE_LENGTH) and (0 <= x < self.SIDE_LENGTH)
