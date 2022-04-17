from typing import Optional

from PySide2.QtCore import QSize, QRectF
from PySide2.QtGui import QPainter
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent

from game.tictactoe.engine.board import Player


class Tile(QGraphicsRectItem):
    QUEEN = "assets/queen.svg"
    INVALID = "assets/x-mark-red.svg"

    def __init__(self, pos, rect):
        super(Tile, self).__init__(rect)
        self.pos = pos
        self.player: int = Player.EMPTY

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        super().paint(painter, option, widget)
        if self.player:
            self_rect = self.rect()
            rect = QRectF(self_rect)
            rect.setSize(QSize(self_rect.width() * 0.6, self_rect.height() * 0.6))
            rect.moveCenter(self.rect().center())
            svg = Tile.QUEEN if self.player == Player.ONE else Tile.INVALID
            renderer = QSvgRenderer(svg)
            renderer.render(painter, rect)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(f"from press event {self.pos}")

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        # print(f"{self.pos} tile clicked ")
        print(f"the type of scene: {type(self.scene())}")
        self.scene().tile_clicked.emit(self)
        super().mouseReleaseEvent(event)
