from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog, QPushButton, QSpacerItem, QSizePolicy

from game.n_queens.engine.queencontroller import QueenController
from game.n_queens.gui.queenscene import NQueenScene
from game.tictactoe.gui.ui_files.ui_tictactoemenu import Ui_TictactoeMenu


class NQueensMenu(QDialog):

    def __init__(self, parent=None):
        super(NQueensMenu, self).__init__(parent)
        self.ui = Ui_TictactoeMenu()
        self.ui.setupUi(self)
        self.__init_ui()
        self.__init_connection()
        self.view = self.ui.g_view
        self.view.setGeometry(0, 0, 600, 600)
        print(f"view rect {self.view.sceneRect(), self.view.geometry()}")
        self.scene = NQueenScene(self.view.geometry(), self)
        self._controller = QueenController(self.scene, 4)
        self.view.setScene(self.scene)
        self.setMinimumSize(600, 600)
        self.adjustSize()

    def __init_ui(self):
        btn_reset = self.ui.btn_undo
        btn_reset.setText("Reset")
        btn_show_moves = self.ui.btn_new_game
        btn_show_moves.setText("Current state solutions")
        self.ui.btn_prev_sol = QPushButton("Prev")
        self.ui.btn_next_sol = QPushButton("Next")
        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.horizontalLayout.addWidget(self.ui.btn_prev_sol)
        self.ui.horizontalLayout.addItem(spacer1)
        self.ui.horizontalLayout.addWidget(self.ui.btn_next_sol)
        self.ui.horizontalLayout.addItem(spacer2)
        self.ui.btn_prev_sol.setVisible(False)
        self.ui.btn_next_sol.setVisible(False)

    def __init_connection(self):
        self.ui.btn_new_game.clicked.connect(self._show_solutions)
        self.ui.btn_undo.clicked.connect(self._reset_game)
        self.ui.btn_prev_sol.clicked.connect(lambda: self._controller.show_solution(False))
        self.ui.btn_next_sol.clicked.connect(lambda: self._controller.show_solution(True))

    def _reset_game(self):
        self.enable_btns(False)
        self._controller.reset_game()

    def _show_solutions(self):
        self.enable_btns(True)
        self._controller.generate_solution()

    @Slot(bool)
    def enable_btns(self, enabled: bool):
        self.ui.btn_prev_sol.setVisible(enabled)
        self.ui.btn_next_sol.setVisible(enabled)
