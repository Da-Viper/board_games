from PySide2.QtCore import QRect, Signal, QTimer
from PySide2.QtWidgets import QGraphicsScene, QDialog

from game.sliding_puzzle.engine.pcontroller import PController
from game.sliding_puzzle.gui.tile import Tile
from game.tictactoe.gui.ui_files.ui_tictactoemenu import Ui_TictactoeMenu


class PuzzleScene(QGraphicsScene):
    tile_clicked = Signal(Tile)

    def __init__(self, board_size: int, geometry: QRect, parent=None):
        super(PuzzleScene, self).__init__(geometry, parent)
        self.board_size = board_size
        md_board = self._draw_board()
        self._controller = PController(md_board, board_size)
        self._init_connections()

    def _draw_board(self):
        size = self.board_size
        item_width = int(self.width() // size)
        item_height = int(self.height() // size)

        board = []
        for i in range(size * size - 1):
            col, row = divmod(i, size)
            item_pos = QRect(row, col, item_width, item_height)
            curr_tile = Tile(i, item_pos)
            board.append(i + 1)
            self.addItem(curr_tile)
        board.append(0)
        return board

    def _init_connections(self):
        self.tile_clicked[Tile].connect(self._controller.tile_clicked)
        pass


class SlidingMenu(QDialog):

    def __init__(self, parent=None):
        super(SlidingMenu, self).__init__(parent)
        self.ui = Ui_TictactoeMenu()
        self.ui.setupUi(self)
        self.view = self.ui.g_view
        self.view.setGeometry(0, 0, 600, 600)
        print(f"view rect {self.view.sceneRect(), self.view.geometry()}")
        self.scene = PuzzleScene(4, self.view.geometry(), self)
        self.view.setScene(self.scene)
        self.setMinimumSize(600, 600)
        self._timer = QTimer(self)

        self.adjustSize()
        self._init_connections()

    def _init_connections(self):
        self._timer.timeout.connect(self.scene.advance)
        self._timer.start(30)
