import sys
from PyQt5.QtCore import QObject, QTimer, pyqtSlot
from PyQt5.QtWidgets import QApplication


class Worker(QObject):
    def __init__(self):
        super(Worker, self).__init__()

        timer = QTimer(self)
        timer.timeout.connect(self.xxx)
        timer.start(1000)

    # 这个装饰函数一定要用哦
    @pyqtSlot()
    def xxx(self):
        print('xxx')


def main():


    app = QApplication(sys.argv)

    worker = Worker()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
