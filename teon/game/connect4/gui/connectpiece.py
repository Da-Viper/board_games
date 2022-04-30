from typing import Optional

from PySide2.QtCore import QSize, QRectF, QRect
from PySide2.QtGui import QPainter, QColor, QPen, Qt
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent

from teon.game.connect4.engine.board import Player


class ConnectPiece(QGraphicsRectItem):
    DARK = QColor("#ba5546")
    LIGHT = QColor("#f8ec5a")

    def __init__(self, rect: QRect, player: Player = Player.EMPTY):
        super(ConnectPiece, self).__init__(rect)
        # self.g_scale
        # self.pos = pos
        self.player = player

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        super().paint(painter, option, widget)
        if not self.player:
            return
        center = self.boundingRect().center()
        rect = self.rect()
        color = ConnectPiece.DARK if self.player == Player.ONE else ConnectPiece.LIGHT
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setBrush(color)
        pen = QPen(Qt.SolidPattern, 5)
        painter.setPen(pen)
        painter.drawEllipse(center, rect.width() / 3, rect.height() / 3)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(f"from press event {self.pos}")

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(f"the type of scene: {type(self.scene())}")
        self.scene().tile_clicked.emit(self)
        super().mouseReleaseEvent(event)
