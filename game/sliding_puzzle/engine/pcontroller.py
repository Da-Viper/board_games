import random
import time
from copy import deepcopy
from typing import List, Tuple

from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import QGraphicsScene, QListWidget

from game.sliding_puzzle.engine.algorithms import ai_play
from game.sliding_puzzle.engine.pboard import PBoard, Direction
from game.sliding_puzzle.gui.puzzlescene import PuzzleScene
from game.sliding_puzzle.gui.tile import Tile


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
        new_pos = self._board.move_piece(current_pos)

        if new_pos != (-1, -1):
            tile.set_new_pos(new_pos)

    @Slot()
    def slot_shuffle_clicked(self):
        board = self._board
        board_size = board.size
        tiles = self.scene.tiles
        shuffle_time = time.time() + 0.5  # millis

        while time.time() < shuffle_time:
            n_row, n_col = random.choice(list(board.get_blank_neighbours()))
            blank_row, blank_col = board.blank_idx
            n_pos = n_row * board_size + n_col
            blank_pos = blank_row * board_size + blank_col
            current_tile = tiles[n_pos]
            tiles[n_pos], tiles[blank_pos] = tiles[blank_pos], tiles[n_pos]
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

    def _init_connections(self):
        self.scene.tile_clicked[Tile].connect(self.tile_clicked)
