from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QDialog, QSpacerItem, QSizePolicy, QPushButton

from game.sliding_puzzle.engine.pcontroller import PController
from game.sliding_puzzle.gui.puzzlescene import PuzzleScene
from game.sliding_puzzle.gui.ui_files.ui_slidingpuzzlemenu import Ui_SlidingPuzzleMenu


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
        self._timer = QTimer(self)

        self.adjustSize()
        self._init_connections()

    def _init_ui(self):
        hspacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.btn_shuffle = QPushButton("Shuffle")
        self.ui.horizontalLayout.addWidget(self.ui.btn_shuffle)
        self.ui.horizontalLayout.addItem(hspacer)

    def _init_connections(self):
        self._timer.timeout.connect(self.scene.advance)
        self._timer.start(50)
        self.ui.btn_shuffle.clicked.connect(self._controller.slot_shuffle_clicked)
        self.ui.btn_show_solution.clicked.connect(self._controller.slot_show_solution)
