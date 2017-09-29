"""
测试触发信号
void	connected()
void	disconnected()
void	error(QAbstractSocket::SocketError socketError)
void	hostFound()
void	proxyAuthenticationRequired(const QNetworkProxy &proxy, QAuthenticator *authenticator)
void	stateChanged(QAbstractSocket::SocketState socketState)

void	aboutToClose()
void	bytesWritten(qint64 bytes)
void	channelBytesWritten(int channel, qint64 bytes)
void	channelReadyRead(int channel)
void	readChannelFinished()
void	readyRead()

void	destroyed(QObject *obj = Q_NULLPTR)
void	objectNameChanged(const QString &objectName)
"""
import sys
import traceback

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QApplication


class SocketTest(QObject):
    def __init__(self, parent=None):
        super(SocketTest, self).__init__(parent)

    def init_socket(self):
        self.socket = QTcpSocket(self)

        def connected():
            print('connected')
            self.socket.write('fuck u'.encode(encoding='utf8'))

        def disconnect():
            print('disconnected')

        def ready_ready():
            print('ready read', end=': ')

            print(self.socket.readAll())

            self.socket.close()

        @pyqtSlot(int)
        def bytes_written(bytes):
            print('{} bytes send'.format(bytes))

        self.socket.connected.connect(connected)
        self.socket.disconnected.connect(disconnect)
        self.socket.readyRead.connect(ready_ready)
        self.socket.bytesWritten.connect(bytes_written)

        self.socket.connectToHost('202.5.19.132', 22)


def main():
    sys.stdout.flush()
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    socket = SocketTest()
    socket.init_socket()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
