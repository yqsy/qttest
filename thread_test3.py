import threading
import time

import sys

from PyQt5.QtCore import QThreadPool, QRunnable, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication

"""
这个是wiz笔记的思路,直接往线程池里扔函数对象,函数执行完触发signal
"""
class Task(QRunnable):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self):
        self.func()


class Work(QObject):
    def __init__(self, *args, **kwargs):
        super(Work, self).__init__(*args, **kwargs)

    result_ready = pyqtSignal(str)

    def do_work(self):
        time.sleep(1)

        print('Work thread id {}'.format(threading.get_ident()))

        self.result_ready.emit('okokok')


@pyqtSlot(str)
def handle_results(result):
    print('handle_results thread id {}'.format(threading.get_ident()))
    print(result)


def main():
    app = QApplication(sys.argv)

    print('main thread id {}'.format(threading.get_ident()))

    work = Work()
    work.result_ready.connect(handle_results)

    def foo():
        work.do_work()

    QThreadPool.globalInstance().start(Task(foo))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
