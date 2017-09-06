import sys
import traceback
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label1 = QLabel('Hello World')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(QLabel('你好,世界'))

        self.setLayout(vbox)


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)

    app.setStyleSheet('QLabel {'
                      'color: white;'
                      'background-color: red;'
                      '}')

    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
