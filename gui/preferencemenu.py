from PySide2.QtWidgets import QDialog

from gui.ui_files.ui_preference import Ui_Dialog as UIPreferenceDialog


class PreferenceMenu(QDialog):
    def __init__(self, parent=None):
        super(PreferenceMenu, self).__init__(parent)
        self.ui = UIPreferenceDialog()
        self.ui.setupUi(self)


