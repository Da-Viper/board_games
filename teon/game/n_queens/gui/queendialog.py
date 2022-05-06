from PySide2.QtCore import Slot, QTimer
from PySide2.QtWidgets import QDialog, QPushButton, QSpacerItem, QSizePolicy

from teon.game.n_queens.engine.queencontroller import QueenController
from teon.game.n_queens.gui.queenscene import NQueenScene
from teon.game.n_queens.gui.ui_files.ui_nqueens_dialog import UI_NQueensMenu
from teon.game.n_queens.gui.ui_files.ui_nqueenpreference import Ui_NQueenPrefDialog


class NQueensMenu(QDialog):

    def __init__(self, queen_size: int, parent=None):
        super(NQueensMenu, self).__init__(parent)
        self.ui = UI_NQueensMenu()
        self.ui.setupUi(self)
        self.__init_ui()
        self._view = self.ui.g_view
        self._view.setGeometry(0, 0, 600, 600)
        self._scene = NQueenScene(self._view.geometry(), self)
        self._controller = QueenController(self._scene, queen_size)
        self._view.setScene(self._scene)
        self.setMinimumSize(600, 600)
        self._timer = QTimer(self)
        self.__init_connection()
        self.adjustSize()

    def __init_ui(self):
        btn_reset = self.ui.btn_undo
        btn_reset.setText("Reset")
        btn_show_moves = self.ui.btn_new_game
        btn_show_moves.setText("Current state solutions")
        self.ui.btn_prev_sol = QPushButton("Prev")
        self.ui.btn_next_sol = QPushButton("Next")
        self.ui.btn_simulate = QPushButton("Simulate")
        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.horizontalLayout.addWidget(self.ui.btn_prev_sol)
        self.ui.horizontalLayout.addItem(spacer1);
        self.ui.horizontalLayout.addWidget(self.ui.btn_next_sol);
        self.ui.horizontalLayout.addItem(spacer2)
        self.ui.horizontalLayout.addWidget(self.ui.btn_simulate)
        self.ui.horizontalLayout.addItem(spacer3)
        self.ui.btn_prev_sol.setVisible(False)
        self.ui.btn_next_sol.setVisible(False)

    def __init_connection(self):
        self.ui.btn_new_game.clicked.connect(self._show_solutions)
        self.ui.btn_undo.clicked.connect(self._reset_game)
        self.ui.btn_prev_sol.clicked.connect(lambda: self._controller.show_solution(False))
        self.ui.btn_next_sol.clicked.connect(lambda: self._controller.show_solution(True))
        self.ui.btn_simulate.clicked.connect(lambda: self._controller.slot_simulate())
        self._timer.start(250)
        self._timer.timeout.connect(self._scene.advance)
        self.finished.connect(lambda: self._timer.stop())

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


class NQueensPrefDialog(QDialog):

    def __init__(self, parent=None):
        super(NQueensPrefDialog, self).__init__(parent)
        self.ui = Ui_NQueenPrefDialog()
        self.ui.setupUi(self)
        self.ui.spinBox.setMaximum(13)  # max value
        self.ui.spinBox.setMinimum(4)  # min nqueen value
        self.ui.spinBox.setValue(8)  # default value
        self.__init_connections()
        self.adjustSize()

    def __init_connections(self):
        self.ui.buttonBox.accepted.connect(self._start_nqueens)

    @Slot()
    def _start_nqueens(self):
        game = NQueensMenu(self.ui.spinBox.value(), self)
        game.exec_()
