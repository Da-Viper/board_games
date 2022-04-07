import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QApplication

from gui.gamemenu import GameMenu


def main():
    run_checkers()


def run_checkers():
    # game setup
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)

    # with open("../style.qss", "r") as f:
    #     _style = f.read()
    #     app.setStyleSheet(_style)
    # app.setStyle("Windows")
    gmenu = GameMenu()
    gmenu.show()
    # end
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
