from __future__ import annotations

import typing

from PySide2.QtGui import QPainter, Qt, QPen
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsItem

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
        self.is_highlighted = False
        self.__state = None

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget):
        super().paint(painter, option, widget)
        painter.fillRect(self.rect(), self.color)

    def toggle_highlight(self):
        if self.is_highlighted:
            self.color = Qt.white
        else:
            self.is_highlighted = True
            self.color = Qt.gray

        self.update()

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state


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
