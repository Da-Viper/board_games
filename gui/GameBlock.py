import typing
from typing import List

from PySide2.QtCore import QPointF, QLineF
from PySide2.QtGui import QPainter, Qt, QCursor
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsItem, \
    QGraphicsSceneMouseEvent

from game.piece import Piece
from game.player import Player
from game.settings import Settings


class BTile(QGraphicsRectItem):

    def __init__(self, pos_x, pos_y, parent=None):
        super(BTile, self).__init__(parent)

        scale = Settings.G_WIDTH
        self.setRect(pos_x * scale, pos_y * scale, scale, scale)

        if ((pos_x % 2) + (pos_y % 2)) % 2 == 0:
            self.color = Qt.black
        else:
            self.color = Qt.white
        self.highlight_color = Qt.gray

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget):
        super().paint(painter, option, widget)
        # print(f"the bounding rect is {self.boundingRect()}")
        painter.drawRoundRect(self.boundingRect(), 5, 5)

        painter.fillRect(self.boundingRect(), self.color)
        # painter.drawRoundRect(-10, -10, constants.T_WIDTH, constants.T_HEIGHT, 5, 5)


class GPiece(QGraphicsRectItem):

    def __init__(self, x: int, y: int, pos: int, piece: Piece, parent=None):
        self.scale = Settings.G_WIDTH
        scale = self.scale
        super(GPiece, self).__init__(x * scale, y * scale, scale, scale, parent)
        self.piece: Piece = piece
        self.color = Qt.black
        self.setFlags(QGraphicsItem.ItemIsSelectable
                      | QGraphicsItem.ItemIsMovable)
        self.last_pos = self.scenePos()
        self._dragged = False

        if piece.player is Player.HUMAN:
            self.color = Qt.red
            self.setCursor(Qt.ClosedHandCursor)
        print(f" the type is {piece.player}")

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: typing.Optional[QWidget]) -> None:
        # super().paint(painter, option, widget)
        center = self.boundingRect().center()
        # print(f"gpiece_pos {center}")
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setBrush(self.color)
        scale = 0.8 * self.scale
        painter.drawEllipse(center, scale / 3, scale / 3)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self._dragged = True
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self._dragged:
            col_items: List[QGraphicsItem] = self.collidingItems()

            # TODO use contains
            if not col_items:
                self.setPos(self.last_pos)
            else:
                closestItem = col_items[0]
                short_dist = 100000
                for item in col_items:
                    if isinstance(item, GPiece):
                        closestItem = self
                        break

                    line = QLineF(item.sceneBoundingRect().center(), self.sceneBoundingRect().center())

                    if line.length() < short_dist:
                        short_dist = line.length()
                        closestItem = item

                if closestItem is self:
                    self.setPos(self.last_pos)
                else:
                    self.setPos(closestItem.scenePos())
                    self.last_pos = self.scenePos()

            self._dragged = False

        super().mouseReleaseEvent(event)

