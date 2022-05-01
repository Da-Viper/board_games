from typing import Optional, Tuple

from PySide2.QtCore import QRectF, QRect
from PySide2.QtGui import QPainter, Qt, QFont, QPen, QColor
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent


class Tile(QGraphicsRectItem):
    COLOUR = QColor("#f0d9b5")
    OUTLINE = QColor("#292828")

    def __init__(self, text: int, rect: QRect):
        _width = rect.width()
        _height = rect.height()
        super(Tile, self).__init__(0, 0, _width, _height)
        self.idx_pos: Tuple[int, int] = (rect.y(), rect.x())
        self.setPos(rect.x() * _width, rect.y() * _height)
        self._size = (_width, _height)
        self.scale_pos = rect.x() * _width, rect.y() * _height

        self._text: str = str(text + 1)
        self._font = QFont()
        self._font.setPixelSize((_width * _height) ** 0.43)
        self._update_speed = 3
        self._next_pos = (-1, -1)

    def set_new_pos(self, new_pos: Tuple[int, int]):
        self.idx_pos = new_pos
        self._next_pos = (new_pos[0] * self._size[0], new_pos[1] * self._size[0])
        self.update()

    """ ----------------- MoveMent ----------------- """

    def boundingRect(self) -> QRectF:
        c_bound = super().boundingRect()
        new_bound = QRectF(0, 0, c_bound.width() * 0.85, c_bound.height() * 0.85)
        new_bound.moveCenter(c_bound.center())
        return new_bound

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Tile.COLOUR)
        pen = QPen(Qt.SolidPattern, 3)
        pen.setColor(Tile.OUTLINE)
        painter.setPen(pen)
        painter.setFont(self._font)
        painter.drawRoundRect(self.boundingRect(), 20, 20)
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self._text)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        pass

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.scene().tile_clicked.emit(self)
        super().mouseReleaseEvent(event)

    def advance(self, phase: int) -> None:
        if not phase:
            return
        pos_x, pos_y = self.pos().x(), self.pos().y()

        next_pos = self._next_pos
        if next_pos[0] != -1 or next_pos[1] != -1:

            x_dist = next_pos[0] - pos_x
            y_dist = next_pos[1] - pos_y

            if pos_x != next_pos[0] and x_dist > 1:
                pos_x += self._update_speed
            elif x_dist < -self._update_speed:
                pos_x -= self._update_speed
            else:
                pos_x = next_pos[0]

            if pos_y != next_pos[1] and y_dist > 1:
                pos_y += self._update_speed
            elif y_dist < -self._update_speed:
                pos_y -= self._update_speed
            else:
                pos_y = next_pos[1]

            self.setPos(pos_x, pos_y)
            if pos_x == next_pos[0] and pos_y == next_pos[1]:
                self._next_pos = (-1, -1)
        self.setPos(pos_x,pos_y)
