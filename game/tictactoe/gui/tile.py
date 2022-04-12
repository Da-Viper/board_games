from typing import Optional

from PySide2.QtCore import Signal
from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent


class Tile(QGraphicsRectItem):
    X = "assets/xmark-solid.svg"

    def __init__(self, pos, rect):
        super(Tile, self).__init__(rect)
        self.pos = pos
        self.toggled = False

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        rect = self.rect().toRect()
        if self.toggled:
            pixmap = QPixmap(Tile.X)
            painter.drawPixmap(rect, pixmap)
        else:
            painter.drawRect(self.rect())

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(f"from press event {self.pos}")

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        # print(f"{self.pos} tile clicked ")
        print(f"the type of scene: {type(self.scene())}")
        self.scene().tile_clicked.emit(self)
        super().mouseReleaseEvent(event)
