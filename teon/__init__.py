import importlib.resources
import os
import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QApplication, QStyleFactory

from teon.startmenu.mainmenu import MainMenu


def start_game():
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    pt = "QT_QPA_PLATFORMTHEME"
    print(QStyleFactory.keys())
    print(f"env {os.environ.get(pt)}")
    app.setStyle("Adwaita-Dark")
    print(f"style: {app.style().objectName()}")

    if sys.platform == "win32":
        app.setStyle("Fusion")

    style_file = importlib.resources.open_text("assets", "mine.qss")
    with style_file as f:
        _style = f.read()
        app.setStyleSheet(_style)

    gmenu = MainMenu()
    gmenu.show()
    sys.exit(app.exec_())
