import sys
from PyQt5.QtCore import QObject, QTimer, pyqtSlot
from PyQt5.QtWidgets import QApplication


class MyTime(QTimer):
    def __init__(self, *args, **kwargs):
        super(MyTime, self).__init__(*args, **kwargs)

    def __del__(self):
        print('del')


class Worker(QObject):
    def __init__(self):
        super(Worker, self).__init__()

        # 如果不设置父对象就会被销毁
        timer = MyTime(self)
        timer.timeout.connect(self.xxx)
        timer.start(300)

    # 这个装饰函数一定要用哦
    @pyqtSlot()
    def xxx(self):
        print('xxx')


class CCC():
    def __del__(self):
        print('ccc del')


def fuck():
    ccc = CCC()

def main():
    app = QApplication(sys.argv)

    worker = Worker()

    fuck()

    # 猜测是exec_里面会不断的回收没有parent的资源(当然是qt的垃圾回收,和python自己的垃圾回收不要扯上,那是gc,有空研究~)
    # !!! 怎么好像python自己的回收也是及时的?
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
