import random
import time
from typing import List

from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import QGraphicsScene

from game.sliding_puzzle.engine.pboard import PBoard
from game.sliding_puzzle.gui.puzzlescene import PuzzleScene
from game.sliding_puzzle.gui.tile import Tile


class PController:
    tile_clicked = Signal(Tile)

    def __init__(self, board_size: int, scene: PuzzleScene):
        # self._board = PBoard(board)
        self.scene = scene
        self._board_state = self.scene.draw_board(board_size)
        self._board = PBoard(self._board_state, board_size)
        self._init_connections()
        self.slot_shuffle_clicked()

    @Slot(Tile)
    def tile_clicked(self, tile: Tile):
        print(f"\tTile clicked from pos: {tile.idx_pos}")
        new_pos = self._board.swap_pos(tile.idx_pos)
        print(f"\tView : \n{self._board._view}")
        tile.new_pos = new_pos
        if new_pos != (-1, -1):
            tile.set_new_pos(new_pos)

    @Slot()
    def slot_shuffle_clicked(self):
        board = self._board
        shuffle_time = time.time() + 0.5  # millis
        while time.time() < shuffle_time:
            tiles_list = self.scene.tiles

            n_pos = random.choice(list(board.get_blank_neighbours()))
            new_pos = board.swap_pos(n_pos)
            t_pos = n_pos[0] * board.size + n_pos[1]
            b_pos = new_pos[0] * board.size + new_pos[1]

            tile = tiles_list[t_pos]
            tiles_list[t_pos], tiles_list[b_pos] = tiles_list[b_pos], tiles_list[t_pos]
            tile.set_new_pos(new_pos)

    def _init_connections(self):
        self.scene.tile_clicked[Tile].connect(self.tile_clicked)
