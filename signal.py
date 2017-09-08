import sys
import threading
import traceback

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import QComboBox, QApplication, QWidget, QProgressBar, QPushButton, QDialog, QProgressDialog


class MyThread(QThread):
    update = pyqtSignal(int)
    total = pyqtSignal(int)
    end = pyqtSignal(int)

    def __init__(self, parent, n):
        super().__init__(parent)
        self.n = n

    def run(self):
        print('MyThread thread id: ', threading.get_ident())

        self.total.emit(self.n)

        for i in range(self.n):
            self.msleep(30)
            self.update.emit(i)

        self.end.emit(self.n)


class App(QWidget):
    def __init__(self):
        super().__init__()
        button = QPushButton('hello', self)
        button.clicked.connect(self.create_progressdialog)

    def create_progressdialog(self):
        dialog = QProgressDialog(self)

        thread = MyThread(self, 100)
        dialog.setMinimum(0)
        thread.total.connect(dialog.setMaximum)

        def update(i):
            print('update() thread id: ', threading.get_ident())

            dialog.setValue(i)

        thread.update.connect(update)
        thread.end.connect(update)

        thread.start()
        dialog.exec_()


def main():
    sys.excepthook = traceback.print_exception
    print('main thread id: ', threading.get_ident())
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()