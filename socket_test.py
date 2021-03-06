import sys
import traceback

from PyQt5.QtCore import QObject
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QApplication


IP = '192.168.1.4'
PORT = 17990

class SocketTest(QObject):
    def __init__(self, parent=None):
        super(SocketTest, self).__init__(parent)

    def connect(self):
        self.socket = QTcpSocket(self)

        self.socket.connectToHost(IP, PORT)

        if self.socket.waitForConnected(3000):
            print('Connected')

            self.socket.waitForReadyRead(3000)
            print(self.socket.bytesAvailable(), self.socket.readAll())

        else:
            print('Not Connected')



def main():
    sys.excepthook = traceback.print_exception
    #    app = QApplication(sys.argv)

    tcp_sock = SocketTest()

    tcp_sock.connect()


#    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
