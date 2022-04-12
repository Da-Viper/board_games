from PySide2.QtCore import Slot, QObject
from PySide2.QtWidgets import QPushButton


class TTTController(QObject):

    def __init__(self, parent=None):
        super(TTTController, self).__init__(parent)

    def run(self):
        pass

    def _init_connections(self):
        pass

    @Slot(int)
    def update_cell(self, pos: int):
        print(f"from controller current pos : {pos}")

    def update(self, tile: QPushButton):
        print(f"clicked button {self.view.ui.board_grid.indexOf(tile)}")
