import random
import time
from copy import deepcopy
from typing import Tuple

from PySide2.QtCore import Slot, Signal, QCoreApplication
from PySide2.QtWidgets import QListWidget

from teon.game.sliding_puzzle.engine.algorithms import ai_play, Search, Heuristic
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
        self._search_type = Search.ASTAR
        self._heuristic_type = Heuristic.MANHATTAN
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
            QCoreApplication.processEvents()

    @Slot()
    def slot_show_solution(self):
        """call the backtracking algorithm when the button (show current state) is clicked"""
        moves_view = self._result_widget
        moves_view.clear()

        plays = ai_play(deepcopy(self._board), self._search_type, self._heuristic_type)
        for move, direction in plays:
            moves_view.addItem(str(direction))

    @Slot()
    def slot_solve_board(self):
        """Simulate how the computer performs the backtracking for the user  """
        plays = ai_play(deepcopy(self._board), self._search_type, self._heuristic_type)
        tiles = self.scene.tiles

        for i, (move, _) in enumerate(plays):
            self.move_tile_piece(move)
            utils.qt_sleep(400)

    @Slot(Search)
    def slot_search_type(self, s_type: Search):
        self._search_type = s_type

    @Slot(Heuristic)
    def slot_heuristic(self, h_type: Heuristic):
        """set the heuristic used in the sliding puzzle
            manhattan or misplaced tiles
        """
        self._heuristic_type = h_type

    @Slot()
    def slot_show_svg(self):
        """
            Render the svg produced by the search algorithm  in a new dialog
        """
        search_diag = SvgDialog(f"{self._search_type.name}.svg", self.scene.parent())
        search_diag.show()

    def _init_connections(self):
        self.scene.tile_clicked[Tile].connect(self.tile_clicked)
