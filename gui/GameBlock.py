from __future__ import annotations

import typing
from typing import List

from PySide2.QtCore import QPointF, QLineF, QRectF
from PySide2.QtGui import QPainter, Qt, QCursor, QPen, QTransform
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsItem, \
    QGraphicsSceneMouseEvent

from game.game import Game
from game.movefeedback import MoveFeedBack
from game.piece import Piece
from game.player import Player
from game.settings import Settings


class BTile(QGraphicsRectItem):

    def __init__(self, pos_x, pos_y, parent=None):
        scale = Settings.G_WIDTH
        super(BTile, self).__init__(0, 0, scale, scale, parent)
        self.setPos(pos_x * scale, pos_y * scale)

        if ((pos_x % 2) + (pos_y % 2)) % 2 == 0:
            self.color = Qt.black
        else:
            self.color = Qt.white
        self.highlight_color = Qt.gray

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget):
        super().paint(painter, option, widget)
        painter.fillRect(self.rect(), self.color)

    def toggle_highlight(self):
        self.color = Qt.gray
        self.update()


class GPiece(QGraphicsRectItem):

    def __init__(self, x: int, y: int, piece: Piece, pos: int = 0, parent=None):
        self.scale = Settings.G_WIDTH
        scale = self.scale
        super(GPiece, self).__init__(0, 0, scale, scale, parent)

        self.board_pos = pos
        self.setPos(x * scale, y * scale)
        self.piece: Piece = piece
        self.color = Qt.black
        self.last_pos = self.pos()
        self._dragged = False

        if piece.player is Player.HUMAN:
            self.setFlags(QGraphicsItem.ItemIsSelectable
                          | QGraphicsItem.ItemIsMovable)

            self.color = Qt.red
            self.setCursor(Qt.ClosedHandCursor)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: typing.Optional[QWidget]) -> None:
        center = self.boundingRect().center()
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setBrush(self.color)
        pen = QPen(Qt.SolidPattern, 5)
        painter.setPen(pen)
        scale = 0.8 * self.scale
        painter.drawEllipse(center, scale / 3, scale / 3)
        if self.piece.is_king:
            painter.setPen(Qt.NoPen)
            painter.setBrush(Qt.white)
            painter.drawEllipse(center, scale / 9, scale / 9)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self._dragged = True
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:

        # if self._dragged:
        print(f"dragged item: {self.pos()}")
        if self._dragged:
            col_items: List[QGraphicsItem] = self.collidingItems()

            # TODO use contains
            if not col_items:
                self.setPos(self.last_pos)
            else:
                closest_item = col_items[0]
                short_dist = 1000000
                for item in col_items:
                    line = QLineF(item.sceneBoundingRect().center(), self.sceneBoundingRect().center())

                    if line.length() < short_dist:
                        short_dist = line.length()

                        closest_item = item

                if isinstance(closest_item, BTile) and closest_item.color is Qt.white:
                    self.setPos(closest_item.pos())
                    self.last_pos = self.pos()
                else:
                    self.setPos(self.last_pos)

            self._dragged = False

        super().mouseReleaseEvent(event)
