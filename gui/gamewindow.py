from PySide2.QtGui import QBrush, Qt, QPen, QPainter, QColor
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow, QWidget, QDialog

from game.settings import Settings


class GameWindow(QDialog):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        self.setWindowTitle("Checkers Game widget")
        # self.setGeometry(0, 0, Settings.G_WIDTH, Settings.G_HEIGHT)
        # self.setGeometry(300,200,640, 520) # TODO CHange later

        self.create_ui()
        print("got to here")
        # self.show()

    def create_ui(self):
        scene = QGraphicsScene(self)
        bounds = scene.itemsBoundingRect()
        bounds.setWidth(bounds.width() * 0.9)
        bounds.setHeight(bounds.height() * 0.9)

        green_brush = QBrush(Qt.green)
        black_pen = QPen(Qt.black)
        black_pen.setWidth(5)
        ellipse = scene.addEllipse(10, 10, 200, 200, black_pen, green_brush)

        view = QGraphicsView(scene, self)
        view.fitInView(bounds, Qt.KeepAspectRatio)
        view.setRenderHint(QPainter.Antialiasing)
        view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        view.setBackgroundBrush(QColor(255, 255, 255))
        view.setWindowTitle("Checkers")
        view.showMaximized()

        view.setGeometry(0, 0, Settings.G_WIDTH, Settings.G_HEIGHT)
        # self.view.setGeometry(0,0, 640,520)

    def __draw_scene(self, scene: QGraphicsScene):
        x_offset = 10
        y_offset = 85
