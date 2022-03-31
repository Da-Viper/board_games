from enum import Enum

from PySide2.QtCore import Qt, QLineF
from PySide2.QtWidgets import QGraphicsItem, QGraphicsSceneMouseEvent, QApplication

from game.piece import Piece


class Color(Enum):
    RED = 0
    BLACK = 1


class GamePiece(QGraphicsItem):

    def __init__(self, pos: int, g_pos: tuple, piece: Piece, color: Color):
        """

        :param pos: the position on the board in 1d
        :param g_pos: the gui position on the board 2d
        """
        super().__init__()
        self.setToolTip("Click and drag to move the game piece")
        self.setCursor(Qt.OpenHandCursor)
        self.setAcceptedMouseButtons(Qt.LeftButton)

        self.pos = pos
        self.g_pos = g_pos
        self.piece = piece
        self.color = color

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        super().mousePressEvent(event)
        self.setCursor(Qt.ClosedHandCursor)
        event.setAccepted(True)
        self.update()

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        super().mouseMoveEvent(event)
        if QLineF(event.screenPos(),
                  event.buttonDownScreenPos(Qt.LeftButton)).length() < QApplication.startDragDistance():
            return
        rect = self.boundingRect().toRect()

