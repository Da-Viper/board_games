from os.path import join
from typing import Optional

from PySide2.QtCore import QSize, QRectF
from PySide2.QtGui import QPainter, Qt
from PySide2.QtSvg import QSvgRenderer
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent

from assets import asset_path
from teon.game.n_queens.engine.board import Pos


class Tile(QGraphicsRectItem):
    QUEEN = join(asset_path, "queen.svg")
    INVALID = join(asset_path, "x-mark-red.svg")
    FIXED = join(asset_path, "f-queen.svg")

    def __init__(self, piece: Pos, pos, rect):
        super(Tile, self).__init__(rect)
        self.pos = pos
        self.p_pos = piece

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:
        super().paint(painter, option, widget)
        self_rect = self.rect()
        piece_pos = self.p_pos
        conflict, has_queen, is_fixed = piece_pos.conflicts > 0, piece_pos.has_queen, piece_pos.is_fixed
        svg = None
        if not conflict and not has_queen:
            return
        if has_queen:
            if is_fixed:
                painter.fillRect(self_rect, Qt.green)
            svg = Tile.QUEEN
        elif conflict:
            svg = Tile.INVALID
        rect = QRectF(self_rect)
        rect.setSize(QSize(self_rect.width() * 0.6, self_rect.height() * 0.6))
        rect.moveCenter(self.rect().center())
        renderer = QSvgRenderer(svg)
        renderer.render(painter, rect)
        painter.drawRect(self_rect)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        pass

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(f"the type of scene: {type(self.scene())}")
        self.scene().tile_clicked.emit(self)
        super().mouseReleaseEvent(event)
