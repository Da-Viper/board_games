from PySide2.QtCore import Slot, Signal, QObject

from game.n_queens.engine.board import NQueen, Piece
from game.n_queens.gui.queenscene import NQueenScene
from game.n_queens.gui.tile import Tile


class QueenController(QObject):
    update_gui = Signal(tuple)

    def __init__(self, scene: NQueenScene, size: int, parent=None):
        super(QueenController, self).__init__(parent)
        self.scene = scene
        # self.board = NQueen(size)
        board = self.scene.init_grid(size)
        print(f" got board {board}")
        self.board = NQueen(board, size)
        self._init_connection()

    @Slot(Tile)
    def update_cell(self, clicked_tile: Tile):
        pos = clicked_tile.pos
        tile_piece = clicked_tile.p_pos

        if tile_piece.has_queen:
            self.board.remove_queen(pos)
        elif tile_piece.conflicts > 0:
            return
        else:
            self.board.place_queen(pos)
        self.update_gui.emit(pos)

    @Slot(tuple)
    def slot_update_gui(self):
        print(f"board {self.board.board}")
        self.scene.update()

    def _init_connection(self):
        self.scene.tile_clicked[Tile].connect(self.update_cell)
        self.update_gui.connect(self.slot_update_gui)
