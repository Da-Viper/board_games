from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QDialog

from teon.game.sliding_puzzle.engine.algorithms import Heuristic, Search
from teon.game.sliding_puzzle.engine.pcontroller import PController
from teon.game.sliding_puzzle.gui.puzzlescene import PuzzleScene
from teon.game.sliding_puzzle.gui.ui_files.ui_slidingpuzzlemenu import Ui_SlidingPuzzleMenu


class SlidingMenu(QDialog):

    def __init__(self, parent=None):
        super(SlidingMenu, self).__init__(parent)
        self.ui = Ui_SlidingPuzzleMenu()
        self.ui.setupUi(self)
        self._init_ui()
        self.view = self.ui.g_view
        self.view.setGeometry(0, 0, 600, 600)
        self.scene = PuzzleScene(self.view.geometry(), self)
        self._controller = PController(3, self.scene, self.ui.listWidget)
        self.view.setScene(self.scene)
        self.setMinimumSize(600, 600)
        self._timer = QTimer(self.scene)

        self.adjustSize()
        self._init_connections()

    def _init_ui(self):
        self.ui.btn_show_svg.setDisabled(True)

    def _init_connections(self):
        self._timer.timeout.connect(self.scene.advance)
        self._timer.start(30)
        self.finished.connect(lambda: self._timer.stop())

        self.ui.btn_solve.clicked.connect(self._controller.slot_solve_board)
        self.ui.btn_shuffle.clicked.connect(self._controller.slot_shuffle_clicked)
        self.ui.btn_show_solution.clicked.connect(self._controller.slot_show_solution)
        self.ui.btn_show_solution.clicked.connect(lambda: self.ui.btn_show_svg.setDisabled(False))
        self.ui.btn_show_svg.clicked.connect(self._controller.slot_show_svg)
        # heuristic
        self.ui.btn_manhattan.clicked.connect(lambda: self._controller.slot_heuristic(Heuristic.MANHATTAN))
        self.ui.btn_misplaced.clicked.connect(lambda: self._controller.slot_heuristic(Heuristic.MISPLACED))
        # search
        self.ui.btn_astar.clicked.connect(lambda: self._controller.slot_search_type(Search.ASTAR))
        self.ui.btn_idastar.clicked.connect(lambda: self._controller.slot_search_type(Search.IDASTAR))
        # self.ui.btn_id
