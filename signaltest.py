import logging
import sys
import traceback

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication

FORMAT = '%(asctime)s %(thread)d %(levelname)s %(filename)s:%(lineno)d:%(funcName)s %(message)s'

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[]
)

logger = logging.getLogger()


class Test1(QObject):
    testsignal = pyqtSignal()

    def __init__(self):
        super(Test1, self).__init__()

    @pyqtSlot()
    def slot1(self):
        logger.debug('slot1')


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        pass


def main():
    # 设置cmd窗口作为输出handler
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter(FORMAT))
    console.flush = sys.stdout.flush
    logger.addHandler(console)

    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)

    test1 = Test1()

    # 重复两次连接 会产生两次事件
    test1.testsignal.connect(test1.slot1)
    test1.testsignal.connect(test1.slot1)

    # disconnect一次会把所有这个函数的事件删掉
    test1.testsignal.disconnect(test1.slot1)
    test1.testsignal.emit()
    # widget = MyWidget()
    # widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
