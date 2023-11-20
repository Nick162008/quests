import sys
from math import sin, cos, pi
from random import randint

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        if status == 1:
            R = randint(20, 100)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(int(self.coords_[0] - R / 2),
                                int(self.coords_[1] - R / 2), R, R)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')

    def mousePressEvent(self, event):
        self.coords_ = [event.x(), event.y()]
        if (event.button() == Qt.LeftButton):
            self.status = 1
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords_ = [event.x(), event.y()]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
            self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec_())
