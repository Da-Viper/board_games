from typing import Optional

from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent

from game.tictactoe.engine.board import Player


class Tile(QGraphicsRectItem):
    X = "assets/x-mark.svg"
    O = "assets/o-mark.svg"

    def __init__(self, pos, rect):
        super(Tile, self).__init__(rect)
        self.pos = pos
        # self.toggled = False
        self.player: int = Player.EMPTY

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        rect = self.rect().toRect()
        if self.player:
            svg = Tile.X if self.player == Player.ONE else Tile.O
            pixmap = QPixmap(svg)

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
