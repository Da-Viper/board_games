from __future__ import annotations
from copy import deepcopy
from game.settings import Settings
from game.piece import Piece
from game.player import Player, get_opposite

import sys


class BoardState:
    SIDE_LENGTH = 8
    NO_SQUARES = SIDE_LENGTH * SIDE_LENGTH

    def __init__(self):
        self.turn = Settings.FIRST_MOVE
        self.state: list[Piece | None] = [None] * self.NO_SQUARES
        self.piece_count: dict = {}
        self.king_count: dict = {}
        self.from_pos = -1
        self.to_pos = -1
        self.double_jump_pos = -1
        self.__initialize_board()

    def __initialize_board(self):
        SIDE_LENGTH = self.SIDE_LENGTH
        cur_state = self.state
        for i in range(len(self.state)):
            y = i // SIDE_LENGTH
            x = i % SIDE_LENGTH

            if (x + y) % 2 == 1:

                if y < 3:
                    cur_state[i] = Piece(Player.AI, False)
                elif y > 4:
                    cur_state[i] = Piece(Player.HUMAN, False)

        ai_count = filter(lambda piece: piece is not None and piece.get_player() is Player.AI, cur_state)
        human_count = filter(lambda piece: piece is not None and piece.get_player() is Player.HUMAN, cur_state)
        self.piece_count[Player.AI] = ai_count
        self.piece_count[Player.HUMAN] = human_count

        self.king_count[Player.AI] = ai_count
        self.king_count[Player.HUMAN] = human_count

    def deep_copy(self):
        tmp_board_state = BoardState()
        tmp_board_state.state = deepcopy(self.state)
        return tmp_board_state

    # def compute_heuristic(self, player: Player) -> int:
    #     if (Settings.HEURISTIC == 1):
    #         return heurisitic1

    def heurisitic1(self, player: Player) -> int:
        max_int = sys.maxsize * 2 + 1
        opp_player = get_opposite(player)
        if self.piece_count[opp_player] == 0:
            return max_int
        if self.piece_count[player] == 0:
            return -max_int

        return self.piece_score(player) - self.piece_score(opp_player)

    def heurisitic2(self, player: Player) -> int:
        max_int = sys.maxsize * 2 + 1
        opp_player = get_opposite(player)
        if self.piece_count[opp_player] == 0:
            return max_int
        if self.piece_count[player] == 0:
            return -max_int

        return self.piece_score(player) // self.piece_score(opp_player)

    def piece_score(self, player: Player) -> int:
        return self.piece_count[player] + self.king_count[player]

    def jump_successors(self, piece: Piece, pos: int):
        result = []
        side_length = self.SIDE_LENGTH
        djump_pos = self.double_jump_pos

        if (djump_pos > 0) and pos != djump_pos:
            return result

        x = pos % side_length
        y = pos // side_length

        for dx in piece.get_x_movements():
            for dy in piece.get_y_movements():
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
        return self.from_pos

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
