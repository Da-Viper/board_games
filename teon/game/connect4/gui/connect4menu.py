from PySide2.QtCore import QRect
from PySide2.QtWidgets import QDialog

from teon.game.connect4.engine.connect4controller import Connect4Controller
from teon.game.connect4.gui.connect4scene import TScene
from teon.game.connect4.gui.ui_files.ui_connect4 import Ui_Connect4Menu


class Connect4Menu(QDialog):
    ROW = 6
    COL = 7

    def __init__(self, parent=None):
        super(Connect4Menu, self).__init__(parent)
        self.ui = Ui_Connect4Menu()
        self.ui.setupUi(self)
        self.view = self.ui.g_view
        self.view.setGeometry(0, 0, 700, 600)

        self.scene = TScene(Connect4Menu.ROW, Connect4Menu.COL, self.view.geometry(), self)
        self._controller = Connect4Controller(Connect4Menu.ROW, Connect4Menu.COL, self.scene)
        self.view.setScene(self.scene)
        self.setFixedSize(750, 740)
        self.adjustSize()
        self.__init_connections()

    def __init_connections(self):
        self.ui.btn_0.clicked.connect(lambda: self._controller.slot_column_clicked(0))
        self.ui.btn_1.clicked.connect(lambda: self._controller.slot_column_clicked(1))
        self.ui.btn_2.clicked.connect(lambda: self._controller.slot_column_clicked(2))
        self.ui.btn_3.clicked.connect(lambda: self._controller.slot_column_clicked(3))
        self.ui.btn_4.clicked.connect(lambda: self._controller.slot_column_clicked(4))
        self.ui.btn_5.clicked.connect(lambda: self._controller.slot_column_clicked(5))
        self.ui.btn_6.clicked.connect(lambda: self._controller.slot_column_clicked(6))
