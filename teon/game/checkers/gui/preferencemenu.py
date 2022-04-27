from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog

from teon.game.checkers.engine.player import Player
from teon.game.checkers.engine.settings import Settings
from teon.game.checkers.gui.ui_files.ui_preference import Ui_Dialog as UIPreferenceDialog


class PreferenceMenu(QDialog):
    def __init__(self, parent=None):
        super(PreferenceMenu, self).__init__(parent)
        self.ui = UIPreferenceDialog()
        self.ui.setupUi(self)

        self.ui.btngrp_difficulty.setId(self.ui.btn_rad_easy, 1)
        self.ui.btngrp_difficulty.setId(self.ui.btn_rad_med, 2)
        self.ui.btngrp_difficulty.setId(self.ui.btn_rad_hard, 3)
        self.ui.buttonBox.accepted.connect(self.selected_preference)

    @Slot()
    def selected_preference(self):
        checked_button = self.ui.btngrp_difficulty.checkedId()
        print(f"the checked button {checked_button}")
        if checked_button == 1:
            difficulty = 1
        elif checked_button == 2:
            difficulty = 6
        else:
            difficulty = 8

        Settings.AI_DEPTH = difficulty
        Settings.FIRST_MOVE = Player.HUMAN if self.ui.btn_rad_player.isChecked() else Player.AI
        Settings.FORCE_CAPTURE = True

        print("#############################")
        print("new settings")
        print(f"AI_DEPTH: {Settings.AI_DEPTH}")
        print(f"First MOve: {Settings.FIRST_MOVE}")
        print(f"Force Capture: {Settings.FORCE_CAPTURE}")
        print("#############################")
        print()
