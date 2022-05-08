import random
import time

from PySide2.QtCore import QObject, Slot, Signal
from PySide2.QtWidgets import QMessageBox

from teon.game.connect4.engine.board import CBoard, Player
from teon.game.connect4.gui.connect4scene import TScene
from teon.utils import utils


class Connect4Controller(QObject):
    sig_update_scene = Signal()

    def __init__(self, b_row: int, b_col: int, scene: TScene, parent=None):
        super(Connect4Controller, self).__init__(parent)
        self.scene = scene
        board = self.scene.init_grid(b_row, b_col)
        self.turn = Player.ONE
        self.AI = Player.TWO
        self.board = CBoard(b_row, b_col)
        self._is_gameover = False
        self._init_connection()

    @Slot(int)
    def slot_column_clicked(self, col: int):
        print(f"current turn ")
        is_placed, row = self.board.place_piece(col, self.turn)
        if not is_placed:
            return

        self.scene.slot_update_pos((row, col), self.turn)
        if self.board.has_won((row, col)):
            self.show_gameover()
        self.turn = Player(self.turn * -1)
        utils.qt_sleep(500)
        self.ai_play()

    def ai_play(self):
        if self.turn != self.AI:
            return
        time.sleep(0.5)
        board = self.board
        positions = board.open_pos()
        self.slot_column_clicked(random.choice(positions))

    def show_gameover(self):
        self._is_gameover = True
        msg_box = QMessageBox(QMessageBox.Information, "Game-over", f"You Win Player {self.turn}")
        msg_box.exec_()

    def _init_connection(self):
        self.sig_update_scene.connect(self.scene.update())
