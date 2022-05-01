from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QDialog, QSpacerItem, QSizePolicy, QPushButton

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
        print(f"view rect {self.view.sceneRect(), self.view.geometry()}")
        self.scene = PuzzleScene(self.view.geometry(), self)
        self._controller = PController(3, self.scene, self.ui.listWidget)
        self.view.setScene(self.scene)
        self.setMinimumSize(600, 600)
        self._timer = QTimer(self.scene)

        self.adjustSize()
        self._init_connections()

    def _init_ui(self):
        hspacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.btn_shuffle = QPushButton("Shuffle")
        self.ui.horizontalLayout.addWidget(self.ui.btn_shuffle)
        self.ui.horizontalLayout.addItem(hspacer)

        self.ui.btn_show_svg = self.ui.btn_undo
        self.ui.btn_show_svg.setDisabled(True)
        self.ui.btn_undo.setText("Search Tree")

    def _init_connections(self):
        self._timer.timeout.connect(self.scene.advance)
        self._timer.start(5)
        self.finished.connect(lambda: self._timer.stop())

        self.ui.btn_solve.clicked.connect(self._controller.slot_solve_board)
        self.ui.btn_shuffle.clicked.connect(self._controller.slot_shuffle_clicked)
        self.ui.btn_show_solution.clicked.connect(self._controller.slot_show_solution)
        self.ui.btn_show_solution.clicked.connect(lambda: self.ui.btn_show_svg.setDisabled(False))
        self.ui.btn_show_svg.clicked.connect(self._controller.slot_show_svg)
