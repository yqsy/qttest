import threading

import time

import sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication


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
        


class Controller(QObject):
    begin_work = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.work = Work(self)
        self.thread = MyThread(self)

        self.begin_work.connect(self.work.do_work)
        self.work.moveToThread(self.thread)

        self.work.result_ready.connect(self.handle_results)
        self.thread.start()

    @pyqtSlot(str)
    def handle_results(self, result):
        print('handle_results id {}'.format(threading.get_ident()))
        print(result)


# http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
# 没有使用到线程,直接在主线程的processEvents上执行
def main():
    print('main id {}'.format(threading.get_ident()))

    controller = Controller()

    controller.begin_work.emit()

    QApplication.processEvents()


if __name__ == '__main__':
    main()
