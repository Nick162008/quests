import sqlite3
import sys
from PyQt5 import uic, Qt
from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffe.sqlite.db')
        self.cur = self.con.cursor()
        self.table()

    def table(self):
        cur = self.con.cursor()
        result = cur.execute("""select name_sort, stepen_fire, vid_coffe, opicane, cost, obem from coffes""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ["Название сорта", "Степень прожарки", "Вид коффе", "Описание", "Цена", "Объем"])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
