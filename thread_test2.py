import threading

import time
import traceback

import sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication

"""
这个例子是work带slot 开启工作,把work move到线程上,再用signal 触发 slot, 再触发work的 signal 表示工作完成了
"""

class Work(QObject):
    def __init__(self, *args, **kwargs):
        super(Work, self).__init__(*args, **kwargs)

    result_ready = pyqtSignal(str)

    @pyqtSlot()
    def do_work(self):
        time.sleep(1)

        print('Work thread id {}'.format(threading.get_ident()))

        self.result_ready.emit('okokok')


class MyThread(QThread):
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)

    def run(self):
        print('MyThread thread id {}'.format(threading.get_ident()))

        self.exec_()


# 要搞懂的问题!! parent() 和 moveToThread 概念是否一样? 不一样吧
# 下面这个是最佳实践了感觉
class Controller(QObject):
    begin_work = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.thread = MyThread(self)

        # The object cannot be moved if it has a parent.
        self.work = Work()

        self.work.moveToThread(self.thread)

        self.begin_work.connect(self.work.do_work)

        self.work.result_ready.connect(self.handle_results)
        self.thread.start()

    @pyqtSlot(str)
    def handle_results(self, result):
        print('handle_results id {}'.format(threading.get_ident()))
        print(result)


# http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
def main():
    sys.excepthook = traceback.print_exception

    print('main thread id {}'.format(threading.get_ident()))

    controller = Controller()

    controller.begin_work.emit()

    app = QApplication(sys.argv)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
