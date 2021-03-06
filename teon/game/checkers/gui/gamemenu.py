from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog

from teon.game.checkers.engine.settings import Settings
from teon.game.checkers.gui.gamescene import GameScene
from teon.game.checkers.gui.preferencemenu import PreferenceMenu
from teon.game.checkers.gui.ui_files.ui_checkers import Ui_Form as UICheckers
from teon.game.checkers.gui.ui_files.ui_menu import Ui_Form as UIGameMenu


class GameMenu(QDialog):

    def __init__(self, parent=None):
        super(GameMenu, self).__init__(parent)

        self.ui = UIGameMenu()
        self.ui.setupUi(self)
        self.setWindowTitle("Checkers")

        # connecting signal and slots
        self.ui.btn_start.clicked.connect(self.show_preference)
        self.ui.btn_exit.clicked.connect(self.exit_game)

    @Slot()
    def show_preference(self):
        pref_dialog = PreferenceMenu(self)
        pref_dialog.accepted.connect(self.start_checkers)
        pref_dialog.exec_()

    @Slot()
    def show_rules(self):
        pass

    @Slot()
    def exit_game(self):
        self.close()

    @Slot()
    def start_checkers(self):
        checker_dialog = CheckersWindow(self)
        checker_dialog.exec_()


class CheckersWindow(QDialog):

    def __init__(self, parent=None):
        super(CheckersWindow, self).__init__(parent)
        self.ui = UICheckers()
        self.ui.setupUi(self)
        self.setWindowTitle("Checkers")
        self.setMinimumSize(Settings.G_BOARD_DIMEN + 50, Settings.G_BOARD_DIMEN + 80)
        self.scene = GameScene(self)
        self.ui.gview.setScene(self.scene)
        self.ui.gview.setGeometry(0, 0, Settings.G_BOARD_DIMEN, Settings.G_BOARD_DIMEN)
        self.scene.setSceneRect(self.ui.gview.geometry())

        # connect buttons
        self.ui.btn_reset.clicked.connect(self.reset_scene)
        self.ui.btn_undo.clicked.connect(self.scene.slot_undo_clicked)

    def close_window(self):
        self.close()

    @Slot()
    def reset_scene(self):
        self.scene = None
        self.scene = GameScene(self)
        self.ui.gview.setScene(self.scene)
        self.ui.btn_undo.clicked.connect(self.scene.slot_undo_clicked)
