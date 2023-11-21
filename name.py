import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5 import uic
from random import randint
from ui_ui import Ui_MainWindow


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.circle)
        canvas = QPixmap(500, 500)
        self.label.setPixmap(canvas)

    def circle(self):
        x, y = [randint(10, 490) for i in range(2)]
        a = randint(10, 80)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(QColor(*[randint(0, 255) for _ in range(3)])))
        painter.setPen(pen)
        painter.drawEllipse(x, y, a, a)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())