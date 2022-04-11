import os
import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QApplication, QStyleFactory

from game.checkers.gui.gamemenu import GameMenu
from gui.mainmenu import MainMenu


def main():
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)
    pt = "QT_QPA_PLATFORMTHEME"
    # print(os.environ)
    print(QStyleFactory.keys())
    print(f"env {os.environ.get(pt)}")
    app.setStyle("Adwaita-Dark")
    print(f"style: {app.style().objectName()}")

    gmenu = MainMenu()
    gmenu.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
