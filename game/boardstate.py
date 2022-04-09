from __future__ import annotations

import collections
from copy import copy
from math import inf

import numpy as np

from game.piece import Piece
from game.player import Player
from game.settings import Settings


class BoardState:
    """
     This class is a logic controller for the current board state.
     This class can also simulate possible states from the current state -
        - for:
                (a) Player movement - attack and non-attack moves
                (b) AI movement (minmax algorithm simulation)
    """

    DIMENSION = Settings.BOARD_DIMEN
    NO_SQUARES = DIMENSION * DIMENSION

    def __init__(self):
        """
            Initialises board attributes to default values.
        """
        self.turn: Player = Settings.FIRST_MOVE
        self.state = np.empty([BoardState.NO_SQUARES], dtype=Piece)
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

    def copy_board_state(self):
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

    def heuristic1(self, player: Player) -> float | int:
        """

        :param player:
        :return:
        """
        # max_int = Settings.MAX_VALUE
        opp_player = get_opposite(player)
        if self.piece_count[opp_player] == 0:
            return inf
        if self.piece_count[player] == 0:
            return -inf

        return self.piece_score(player) - self.piece_score(opp_player)

    def heuristic2(self, player: Player) -> float | int:
        # max_int = Settings.MAX_VALUE
        opp_player = get_opposite(player)
        if self.piece_count[opp_player] == 0:
            return inf
        if self.piece_count[player] == 0:
            return -inf

        return self.piece_score(player) // self.piece_score(opp_player)

    def piece_score(self, player: Player) -> int:
        return self.piece_count[player] + self.king_count[player]

    def get_all_states(self) -> list[BoardState]:
        gen_states = self.get_possible_state(True)
        if Settings.FORCE_CAPTURE:
            if len(gen_states) > 0:
                return gen_states
            else:
                return self.get_possible_state(False)
        else:
            gen_states.extend(self.get_possible_state(False))
            return gen_states

    def get_possible_state(self, jump: bool) -> list[BoardState]:
        result: list[BoardState] = []
        c_state = self.state
        turn_ = self.turn
        for i in range(len(c_state)):
            cur_piece: Piece = c_state[i]
            if cur_piece is not None:
                if cur_piece.player is turn_:
                    result.extend(self.get_possible_states(i, jump))
        return result

    def get_states_from_position(self, pos: int) -> list[BoardState]:
        if Settings.FORCE_CAPTURE:
            jumps = self.get_possible_state(True)
            has_jumps = len(jumps) > 0
            return self.get_possible_states(pos, has_jumps)
        else:
            result: list[BoardState] = []
            result.extend(self.get_possible_states(pos, True))
            result.extend(self.get_possible_states(pos, False))
            return result

    def get_possible_states(self, pos: int, jump: bool) -> list[BoardState]:
        if self.get_piece(pos).player != self.turn:
            raise ValueError(" This is not your piece in this position ")

        cpiece = self.state[pos]
        if jump:
            return self.get_attacking_states(cpiece, pos)

        return self.get_non_attacking_states(cpiece, pos)

    def get_non_attacking_states(self, piece: Piece, pos: int) -> list[BoardState]:
        result: list[BoardState] = []
        board_dimen = self.DIMENSION
        x = pos % board_dimen
        y = pos // board_dimen

        for dx, dy in piece.pos_moves():
            new_x = x + dx
            new_y = y + dy

            if not self._is_valid(new_y, new_x):
                continue
            if self._get_piece(new_y, new_x) is not None:
                continue

            new_pos = board_dimen * new_y + new_x
            result.append(self.__create_new_state(pos, new_pos, piece, False, dy, dx))

        return result

    def get_attacking_states(self, piece: Piece, pos: int) -> list[BoardState]:
        djump_pos = self.double_jump_pos
        if (djump_pos > 0) and pos != djump_pos:
            return []

        result = []
        side_length = self.DIMENSION
        x = pos % side_length
        y = pos // side_length
        _get_piece = self._get_piece

        for dx, dy in piece.pos_moves():
            new_x = x + dx
            new_y = y + dy

            if not self._is_valid(new_y, new_x):
                continue
            piece_pos = _get_piece(new_y, new_x)
            if (piece_pos is not None) and (piece_pos.player == get_opposite(piece.player)):
                new_x += dx
                new_y += dy
                if self._is_valid(new_y, new_x):
                    if _get_piece(new_y, new_x) is None:
                        new_pos = side_length * new_y + new_x
                        result.append(self.__create_new_state(pos, new_pos, piece, True, dy, dx))

        return result

    def __create_new_state(self, old_pos: int, new_pos: int, piece: Piece, jumped: bool, dy: int, dx: int):
        result: BoardState = self.copy_board_state()
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
            result.state[new_pos - self.DIMENSION * dy - dx] = None
            result.piece_count[opp_player] -= 1

            if len(result.get_attacking_states(piece, new_pos)) > 0 and king_conversion is False:
                result.turn = pplayer
                result.double_jump_pos = new_pos

        return result

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

    def __is_king_pos(self, pos: int, player: Player) -> bool:
        y = pos // self.DIMENSION
        if (y == 0) and player is Player.HUMAN:
            return True
        return (y == self.DIMENSION - 1) and (player is Player.AI)

    def _get_piece(self, y: int, x: int) -> Piece:
        return self.get_piece(self.DIMENSION * y + x)

    def _is_valid(self, x: int, y: int) -> bool:
        return (0 <= y < self.DIMENSION) and (0 <= x < self.DIMENSION)


def get_opposite(ptype: Player) -> Player:
    # return ptype * -1
    return Player.AI if ptype is Player.HUMAN else Player.HUMAN
