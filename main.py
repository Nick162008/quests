import sys
from random import randint

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.push_btn = QPushButton('окружность', self)
        self.push_btn.move(50, 50)
        self.push_btn.resize(200, 100)
        self.push_btn.clicked.connect(self.draw)

    def draw(self):
        R = randint(20, 100)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec_())
