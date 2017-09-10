import sys
import threading

from PyQt5.QtCore import QRunnable, QThreadPool
from PyQt5.QtWidgets import QApplication, QWidget


class Task(QRunnable):
    def run(self):
        print(threading.get_ident())

class App(QWidget):
    def __init__(self):
        super().__init__()

        task = Task()


        QThreadPool.globalInstance().setMaxThreadCount(5)

        #QThreadPool.globalInstance().start(Task())

        threadpool = QThreadPool(self)
        threadpool.start(Task())




def main():
    app = QApplication(sys.argv)
    print('main:{}'.format(threading.get_ident()))
    ex = App()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
