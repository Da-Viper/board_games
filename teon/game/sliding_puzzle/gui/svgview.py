import sys

from PySide2 import QtWidgets
from PySide2.QtGui import QWheelEvent
from PySide2.QtSvg import QSvgWidget
from PySide2.QtWidgets import QGraphicsView, QGraphicsScene, QDialog, QVBoxLayout


class SVGView(QGraphicsView):
    def __init__(self, scene):
        super(SVGView, self).__init__(scene)

    def wheelEvent(self, event: QWheelEvent) -> None:
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        scale_factor = 1.15

        if event.delta() > 0:
            self.scale(scale_factor, scale_factor)
        else:
            self.scale(1 / scale_factor, 1 / scale_factor)
        super().wheelEvent(event)


class SvgDialog(QDialog):

    def __init__(self, img_path: str, parent=None):
        super(SvgDialog, self).__init__(parent)
        self.img_path = img_path
        self.initUI()

    def initUI(self):
        self.scene = QGraphicsScene(self)
        self.view = SVGView(self.scene)
        self.view.setBaseSize(600, 480)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.view)
        svg_widget = QSvgWidget(self.img_path)
        self.scene.addWidget(svg_widget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = SvgDialog("../engine/udo.svg")
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
