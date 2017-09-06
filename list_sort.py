import sys
import traceback

from PyQt5.QtCore import QAbstractListModel, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QListView, QTableView


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 500)

        hbox = QHBoxLayout()
        tableview = QTableView()
        hbox.addWidget(tableview)
        self.setLayout(hbox)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['年龄', '身高', '体重'])

        items = [
            [19, 180, 60],
            [20, 179, 61],
            [21, 178, 62],
            [22, 177, 63]
        ]

        for ele1 in items:
            for idx, ele2 in enumerate(ele1):
                ele1[idx] = QStandardItem(str(ele2))

        for item in items:
            model.appendRow(item)

        sort_model = QSortFilterProxyModel()
        sort_model.setDynamicSortFilter(True)
        sort_model.setSourceModel(model)

        tableview.setModel(sort_model)
        tableview.setSortingEnabled(True)


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
