from typing import Optional

from PySide2.QtCore import Signal
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent


class Tile(QGraphicsRectItem):

    def __init__(self, pos, rect):
        super(Tile, self).__init__(rect)
        self.pos = pos

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        # rect = self.rect()
        # print(f"Btile {rect}")
        painter.drawRect(self.boundingRect())

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(f"from press event {self.pos}")

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        # print(f"{self.pos} tile clicked ")
        print(f"the type of scene: {type(self.scene())}")
        self.scene().tile_clicked.emit(self.pos)
        super().mouseReleaseEvent(event)
