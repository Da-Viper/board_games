from typing import List

from PySide2.QtGui import QBrush, Qt, QPen, QPainter, QColor
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow, QWidget, QDialog, QGraphicsItemGroup, \
    QGraphicsItem

from game.settings import Settings
from gui.GameBlock import BTile


class GDialog(QDialog):

    def __init__(self, parent=None):
        super(GDialog, self).__init__(parent)
        self.setMinimumSize(Settings.T_WIDTH * Settings.G_WIDTH + 20, Settings.T_HEIGHT * Settings.G_HEIGHT + 20)
        self.g_group: QGraphicsItemGroup = QGraphicsItemGroup()
        self.tiles: [QGraphicsItem] = []
        self.scene: QGraphicsScene = QGraphicsScene(self)
        self.view: QGraphicsView = QGraphicsView(self.scene, self)
        self.tiles: List[QGraphicsItem] = [None] * Settings.SQUARE_NO
        self.create_scene()
        self.add_tiles()

    def create_scene(self):
        scene = self.scene
        view = self.view
        scene.setSceneRect(0, 0, Settings.T_WIDTH * Settings.G_WIDTH, Settings.T_HEIGHT * Settings.G_HEIGHT)
        view.setGeometry(0, 0, Settings.T_WIDTH * Settings.G_WIDTH + 20, Settings.T_HEIGHT * Settings.G_HEIGHT + 20)

        scene.addItem(self.g_group)

        view.show()

    def add_tiles(self):
        for i in range(Settings.SQUARE_NO):
            grid_x = i % Settings.T_DIMEN
            grid_y = i // Settings.T_DIMEN
            self.tiles[i] = BTile(grid_x, grid_y)
            self.g_group.addToGroup(self.tiles[i])

    def add_pieces(self):
        for i in range(Settings.SQUARE_NO):
            pass
