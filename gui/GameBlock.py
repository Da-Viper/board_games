from PySide2.QtGui import QPainter, Qt
from PySide2.QtWidgets import QGraphicsRectItem, QStyleOptionGraphicsItem, QWidget, QGraphicsItem

from game.settings import Settings


class BTile(QGraphicsRectItem):

    def __init__(self, pos_x, pos_y, parent=None):
        super(BTile, self).__init__(parent)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.Pressed = False

        scale = Settings.G_WIDTH
        self.setRect(pos_x * scale, pos_y * scale, scale, scale)

        if ((pos_x % 2) + (pos_y % 2)) % 2 == 0:
            self.color = Qt.black
        else:
            self.color = Qt.white
        self.highlight_color = Qt.gray

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget):
        super().paint(painter, option, widget)
        print(f"the bounding rect is {self.boundingRect()}")
        painter.drawRoundRect(self.boundingRect(), 5, 5)

        painter.fillRect(self.boundingRect(), self.color)
        # painter.drawRoundRect(-10, -10, constants.T_WIDTH, constants.T_HEIGHT, 5, 5)
