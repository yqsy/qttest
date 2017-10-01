"""
测试触发信号
*void	connected()
*void	disconnected()
*void	error(QAbstractSocket::SocketError socketError)
void	hostFound()
void	proxyAuthenticationRequired(const QNetworkProxy &proxy, QAuthenticator *authenticator)
*void	stateChanged(QAbstractSocket::SocketState socketState)

void	aboutToClose()
*void	bytesWritten(qint64 bytes)
void	channelBytesWritten(int channel, qint64 bytes)
void	channelReadyRead(int channel)
void	readChannelFinished()
*void	readyRead()

void	destroyed(QObject *obj = Q_NULLPTR)
void	objectNameChanged(const QString &objectName)
"""
import sys
import traceback
import logging

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
from PyQt5.QtWidgets import QApplication

FORMAT = '%(asctime)s %(thread)d %(levelname)s %(filename)s:%(lineno)d %(message)s'

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[]
)

logger = logging.getLogger(__name__)


class QDebug(object):
    pass


IP = '45.32.17.217'
PORT = 8000

class SocketTest(QObject):
    def __init__(self, parent=None):
        super(SocketTest, self).__init__(parent)

    def init_socket(self):
        self.socket = QTcpSocket(self)

        def connected():
            logger.info('connected , local port:{}'.format(self.socket.localPort()))
            # self.socket.write('fuck u'.encode(encoding='utf8'))

        def disconnect():
            logger.info('disconnected')

            self.socket.connectToHost(IP, PORT)

        @pyqtSlot(QAbstractSocket.SocketError)
        def error(err):
            dict = {
                0: 'QAbstractSocket::ConnectionRefusedError',
                1: 'QAbstractSocket::RemoteHostClosedError',
                2: 'QAbstractSocket::HostNotFoundError',
                3: 'QAbstractSocket::SocketAccessError',
                4: 'QAbstractSocket::SocketResourceError',
                5: 'QAbstractSocket::SocketTimeoutError',
                6: 'QAbstractSocket::DatagramTooLargeError',
                7: 'QAbstractSocket::NetworkError',
                8: 'QAbstractSocket::AddressInUseError',
                9: 'QAbstractSocket::SocketAddressNotAvailableError',
                10: 'QAbstractSocket::UnsupportedSocketOperationError',
                12: 'QAbstractSocket::ProxyAuthenticationRequiredError',
                13: 'QAbstractSocket::SslHandshakeFailedError',
                11: 'QAbstractSocket::UnfinishedSocketOperationError',
                14: 'QAbstractSocket::ProxyConnectionRefusedError',
                15: 'QAbstractSocket::ProxyConnectionClosedError',
                16: 'QAbstractSocket::ProxyConnectionTimeoutError',
                17: 'QAbstractSocket::ProxyNotFoundError',
                18: 'QAbstractSocket::ProxyProtocolError',
                19: 'QAbstractSocket::OperationError',
                20: 'QAbstractSocket::SslInternalError',
                21: 'QAbstractSocket::SslInvalidUserDataError',
                22: 'QAbstractSocket::TemporaryError',
                -1: 'QAbstractSocket::UnknownSocketError'
            }

            logger.info(dict[err])

        @pyqtSlot(QAbstractSocket.SocketState)
        def _state_changed(state):
            # http://doc.qt.io/qt-5/qabstractsocket.html#SocketState-enum
            dict = {
                0: 'QAbstractSocket::UnconnectedState',
                1: 'QAbstractSocket::HostLookupState',
                2: 'QAbstractSocket::ConnectingState',
                3: 'QAbstractSocket::ConnectedState',
                4: 'QAbstractSocket::BoundState',
                6: 'QAbstractSocket::ClosingState',
                5: 'QAbstractSocket::ListeningState'
            }

            logger.info(dict[state])

        def ready_ready():
            logger.info('ready read', end=': ')

            #logger.info(self.socket.readAll(q))

            self.socket.close()

        @pyqtSlot(int)
        def bytes_written(bytes):
            logger.info('{} bytes send'.format(bytes))

        #self.socket.connected.connect(connected)
        #self.socket.disconnected.connect(disconnect)
        self.socket.stateChanged.connect(_state_changed)
        self.socket.error.connect(error)
        # self.socket.readyRead.connect(ready_ready)
        # self.socket.bytesWritten.connect(bytes_written)
        self.socket.connectToHost(IP, PORT)


def main():
    sys.stdout.flush()
    sys.excepthook = traceback.print_exception

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(console)

    app = QApplication(sys.argv)
    socket = SocketTest()
    socket.init_socket()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
