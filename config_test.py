import sys
import traceback

from PyQt5.QtCore import QLocale, QDir, QSettings, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, \
    QListView


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        print(QLocale.system().name())

        path = QDir().homePath() + '/.quickwt'

        # print(path)
        # QDir().mkpath(path)

        setting = QSettings(path + '/quickwt.ini', QSettings.IniFormat)

        title = setting.value('title', 'null')

        self.setWindowTitle(title)

        formlayout = QFormLayout()
        title_line_edit = QLineEdit(title)
        formlayout.addRow('窗口名', title_line_edit)

        hbox = QHBoxLayout()
        hbox.addStretch()
        save_button = QPushButton('保存')
        hbox.addWidget(save_button)

        iplist = setting.value('iplist', ['127.0.0.1', '172.16.0.0', '10.0.0.0'])

        listview = QListView()
        model = QStandardItemModel()
        for ip in iplist:
            print(ip)
            model.appendRow(QStandardItem(ip))

        vbox2 = QVBoxLayout()
        vbox2.addWidget(listview)
        listview.setModel(model)

        def saveconfig():
            setting.setValue('title', title_line_edit.text())

            iplistnew = []

            for i in range(model.rowCount()):
                # 这里不能用 takeRow ,因为放的时候放的是QStandardItem 不是 [QStandardItem,QStandardItem]
                item = model.takeItem(i)

                iplistnew.append(item.data(Qt.DisplayRole))

            setting.setValue('iplist', iplistnew)

        save_button.clicked.connect(saveconfig)

        vbox = QVBoxLayout()
        vbox.addLayout(formlayout)
        vbox.addLayout(vbox2)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
