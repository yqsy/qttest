import sys
import traceback
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QTreeWidget, QTreeWidgetItem


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        treewidget = QTreeWidget()
        vbox.addWidget(treewidget)

        self.setLayout(vbox)

        treewidget.setColumnCount(3)

        item1 = QTreeWidgetItem(['1', '2', '3'])
        treewidget.addTopLevelItem(item1)

        item2 = QTreeWidgetItem(['1', '2', '3'])
        item1.addChild(item2)


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
