from PyQt5.QtNetwork import QLocalSocket


def main():
    local_socket = QLocalSocket()

    local_socket.connectToServer()


if __name__ == '__main__':
    main()