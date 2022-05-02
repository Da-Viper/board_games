import random
import time
from copy import deepcopy
from typing import Tuple

from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import QListWidget

from teon.game.sliding_puzzle.engine.algorithms import ai_play
from teon.game.sliding_puzzle.engine.pboard import PBoard
from teon.game.sliding_puzzle.gui.puzzlescene import PuzzleScene
from teon.game.sliding_puzzle.gui.svgview import SvgDialog
from teon.game.sliding_puzzle.gui.tile import Tile
from teon.utils import utils


class PController:
    tile_clicked = Signal(Tile)

    def __init__(self, board_size: int, scene: PuzzleScene, result_view: QListWidget):
        # self._board = PBoard(board)
        self.scene = scene
        self._board_state = self.scene.draw_board(board_size)
        self._board = PBoard(self._board_state, board_size)
        self._init_connections()
        self._result_widget = result_view
        self.slot_shuffle_clicked()

    @Slot(Tile)
    def tile_clicked(self, tile: Tile):
        current_pos = tile.idx_pos
        tiles = self.scene.tiles
        cpos = current_pos[0] * self._board.size + current_pos[1]
        new_pos = self._board.move_piece(current_pos)
        npos = new_pos[0] * self._board.size + new_pos[1]

        if new_pos != (-1, -1):
            tiles[cpos], tiles[npos] = tiles[npos], tiles[cpos]
            tile.set_new_pos(new_pos)

    def move_tile_piece(self, pos: Tuple[int, int]):
        new_pos = self._board.move_piece(pos)
        tiles = self.scene.tiles
        pos_1 = pos[0] * self._board.size + pos[1]
        new_pos_1 = new_pos[0] * self._board.size + new_pos[1]
        tile_at_pos = tiles[pos_1]
        tiles[new_pos_1], tiles[pos_1] = tiles[pos_1], tiles[new_pos_1]

        if new_pos != (-1, -1):
            print("setting new pos")
            tile_at_pos.set_new_pos(new_pos)

    @Slot()
    def slot_shuffle_clicked(self):
        board = self._board
        board_size = board.size
        tiles = self.scene.tiles
        shuffle_time = time.time() + 0.5  # millis

        while time.time() < shuffle_time:
            n_row, n_col = random.choice(list(board.get_blank_neighbours()))
            n_pos = n_row * board_size + n_col
            current_tile = tiles[n_pos]
            if current_tile:
                self.tile_clicked(current_tile)
        print(f"current board state: {board.puzzle}")

    @Slot()
    def slot_show_solution(self):
        moves_view = self._result_widget
        moves_view.clear()

        print("got to showing item")
        plays = ai_play(deepcopy(self._board))
        for move, direction in plays:
            moves_view.addItem(str(direction))

    @Slot()
    def slot_solve_board(self):
        print("go here")
        plays = ai_play(deepcopy(self._board))
        tiles = self.scene.tiles
        # start = time.time()
        for i, (move, _) in enumerate(plays):
            print(tiles)
            self.move_tile_piece(move)
            utils.qt_sleep(400)

    @Slot()
    def slot_show_svg(self):
        print("got here")
        search_diag = SvgDialog("udo.svg")
        search_diag.exec_()

    def _init_connections(self):
        self.scene.tile_clicked[Tile].connect(self.tile_clicked)
