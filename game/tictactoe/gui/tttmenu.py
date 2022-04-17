from typing import List

from PySide2.QtCore import QRect, Signal, Slot
from PySide2.QtWidgets import QDialog, QPushButton, QGraphicsScene

from game.tictactoe.engine.board import TBoard
from game.tictactoe.gui.tile import Tile
from game.tictactoe.engine.tttcontroller import TTTController
from game.tictactoe.gui.ui_files.ui_tictactoemenu import Ui_TictactoeMenu


class TScene(QGraphicsScene):
    tile_clicked = Signal(Tile)

    def __init__(self, board_size: int, rect: QRect, parent=None):
        super(TScene, self).__init__(rect, parent)
        self.setItemIndexMethod(QGraphicsScene.NoIndex)

        self._controller = TTTController(board_size)
        self._tiles = []
        self.init_grid(board_size)
        self.init_connections()

    def init_grid(self, size: int) -> List[Tile]:
        item_width = int(self.width() // size)
        item_height = int(self.height() // size)

        for i in range(size * size):
            col, row = divmod(i, size)
            item_pos = QRect(row * item_width, col * item_height, item_width, item_height)
            curr_tile = Tile(i, item_pos)
            self.addItem(curr_tile)
            self._tiles.append(curr_tile)
        return self._tiles

    def init_connections(self):
        self.tile_clicked[Tile].connect(self._controller.update_cell)


class TTTMenu(QDialog):

    def __init__(self, parent=None):
        super(TTTMenu, self).__init__(parent)
        self.ui = Ui_TictactoeMenu()
        self.ui.setupUi(self)
        self.view = self.ui.g_view
        self.view.setGeometry(0, 0, 600, 600)
        print(f"view rect {self.view.sceneRect(), self.view.geometry()}")
        self.scene = TScene(4, self.view.geometry(), self)
        self.view.setScene(self.scene)
        self.setMinimumSize(600, 600)
        self.adjustSize()
