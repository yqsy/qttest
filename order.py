import sys
import traceback

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHBoxLayout
from copy import copy


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(1000, 500)
        tableview = QTableView()

        box = QHBoxLayout()
        box.addWidget(tableview)
        self.setLayout(box)

        model = QStandardItemModel(0, 6)
        model.setHorizontalHeaderLabels(['账号', '市场', '代码', '股票名称', '交易类型', '分配量'])

        # QStandardItem


        item = []
        row = ['37000033', 'SZ', '0000002', '万科A', '买入', '100']
        for _, ele in enumerate(row):
            item.append(QStandardItem(ele))

        model.appendRow(item)

        tableview.setModel(model)


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
