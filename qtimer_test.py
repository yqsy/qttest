import threading

import time

import sys
from PyQt5.QtCore import QThreadPool, QRunnable, QTimer, QObject
from PyQt5.QtWidgets import QApplication


class TimerTest(QObject):
    def __init__(self):
        super(TimerTest, self).__init__()
        self._init_time()

    def _init_time(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._timer_out)
        self.timer.start(1000)
        self.timer.stop()

    def _timer_out(self):
        print('timer out, thread id: ', threading.get_ident())


def main():
    app = QApplication(sys.argv)

    print('main thread id: ', threading.get_ident())

    timer_test = TimerTest()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
