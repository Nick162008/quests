import sqlite3
import sys
from PyQt5 import uic
from addEditCoffeeForm_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = sqlite3.connect('coffe.sqlite.db')
        self.cur = self.con.cursor()
        it = [i[0] for i in self.cur.execute("SELECT id FROM coffes").fetchall()]
        for i in it:
            self.comboBox_2.addItem(str(i))
        self.pushButton.clicked.connect(self.change)
        self.pushButton_2.clicked.connect(self.add)
        self.table()

    def table(self):
        result = self.cur.execute(
            """select id, name_sort, stepen_fire, vid_coffe, opicane, cost, obem from coffes""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ["id", "Название сорта", "Степень прожарки", "Вид коффе", "Описание", "Цена", "Объем"])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def change(self):
        if self.comboBox.currentText() == 'name_sort':
            que = self.cur.execute(f"""UPDATE coffes
                                       SET name_sort = '{self.lineEdit.displayText()}'
                                       WHERE id = '{self.comboBox_2.currentIndex() + 1}'""")
            self.con.commit()

        elif self.comboBox.currentText() == 'stepen_fire':
            que = self.cur.execute(f"""UPDATE coffes
                                       SET stepen_fire = '{self.lineEdit.displayText()}'
                                       WHERE id = '{self.comboBox_2.currentIndex() + 1}'""")
            self.con.commit()

        elif self.comboBox.currentText() == 'vid_coffe':
            que = self.cur.execute(f"""UPDATE coffes
                                       SET vid_coffe = '{self.lineEdit.displayText()}'
                                       WHERE id = '{self.comboBox_2.currentIndex() + 1}'""")
            self.con.commit()

        elif self.comboBox.currentText() == 'opicane':
            que = self.cur.execute(f"""UPDATE coffes
                                       SET opicane = '{self.lineEdit.displayText()}'
                                       WHERE id = '{self.comboBox_2.currentIndex() + 1}'""")
            self.con.commit()

        elif self.comboBox.currentText() == 'cost':
            que = self.cur.execute(f"""UPDATE coffes
                                       SET cost = '{self.lineEdit.displayText()}'
                                       WHERE id = '{self.comboBox_2.currentIndex() + 1}'""")
            self.con.commit()

        elif self.comboBox.currentText() == 'obem':
            que = self.cur.execute(f"""UPDATE coffes
                                       SET obem = '{self.lineEdit.displayText()}'
                                       WHERE id = '{self.comboBox_2.currentIndex() + 1}'""")
            self.con.commit()
        self.table()

    def add(self):
        que = self.cur.execute(f"""INSERT INTO coffes(name_sort) VALUES('{self.lineEdit_2.displayText()}')""")
        self.con.commit()
        self.table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
