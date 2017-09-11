import threading

import time

import sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication


class Work(QObject):
    result_ready = pyqtSignal(str)

    @pyqtSlot()
    def do_work(self):
        time.sleep(2)

        self.result_ready.emit('okokok')


class Controller(QObject):
    begin_work = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.work = Work()
        self.begin_work.connect(self.work.do_work)

        self.work.result_ready.connect(self.handle_results)

    @pyqtSlot(str)
    def handle_results(self, result):
        print(result)


# http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
# 没有使用到线程,直接在主线程的processEvents上执行
def main():
    controller = Controller()

    controller.begin_work.emit()

    QApplication.processEvents()


if __name__ == '__main__':
    main()
