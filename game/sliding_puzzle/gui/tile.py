from typing import Optional, Tuple

from PySide2.QtCore import QRectF, QRect
from PySide2.QtGui import QPainter, Qt, QFont
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent


class Tile(QGraphicsRectItem):

    def __init__(self, text: int, rect: QRect):
        _width = rect.width()
        _height = rect.height()
        super(Tile, self).__init__(0, 0, _width, _height)
        self.idx_pos: Tuple[int, int] = (rect.y(), rect.x())
        self.setPos(rect.x() * _width, rect.y() * _height)
        self._size = (_width, _height)

        self._text: str = str(text + 1)
        self._font = QFont()
        self._font.setPixelSize((_width * _height) ** 0.43)

    def set_new_pos(self, new_pos: Tuple[int, int]):
        print(f"new pos {new_pos}")
        self.idx_pos = new_pos
        self.setPos(new_pos[1] * self._size[0], new_pos[0] * self._size[0])

    """ ----------------- MoveMent ----------------- """

    def boundingRect(self) -> QRectF:
        c_bound = super().boundingRect()
        new_bound = QRectF(0, 0, c_bound.width() * 0.85, c_bound.height() * 0.85)
        new_bound.moveCenter(c_bound.center())
        return new_bound

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.gray)
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
        super().advance(phase)
