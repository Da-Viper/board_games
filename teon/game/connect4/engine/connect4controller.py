from PySide2.QtCore import QObject, Slot

from teon.game.connect4.engine.board import CBoard, Player
from teon.game.connect4.gui.connect4scene import TScene


class Connect4Controller(QObject):

    def __init__(self, b_row: int, b_col: int, scene: TScene, parent=None):
        super(Connect4Controller, self).__init__(parent)
        self.scene = scene
        board = self.scene.init_grid(b_row, b_col)
        self.turn = Player.ONE

        self.board = CBoard(b_row, b_col)

    @Slot(int)
    def slot_column_clicked(self, col: int):
        print(f"current turn ")
        is_placed, row = self.board.place_piece(col, self.turn)
        if not is_placed:
            return

        self.scene.slot_update_pos((row, col), self.turn)
        self.turn *= -1

    def show_gameover(self):
        # todo message dialog game over
        pass

