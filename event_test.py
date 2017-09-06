import sys
import traceback

from PyQt5.QtCore import QStateMachine, QState, QEventTransition, QEvent
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QSizePolicy


# refer: http://doc.qt.io/qt-5/qtwidgets-statemachine-eventtransitions-example.html
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()

        button1 = QPushButton('fuck1')

        vbox.addWidget(button1)

        button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        vbox.setContentsMargins(80, 80, 80, 80)

        self.setLayout(vbox)

        machine = QStateMachine(self)
        s1 = QState()
        s1.assignProperty(button1, "text", "Outside")
        s2 = QState()
        s2.assignProperty(button1, "text", "Inside")

        enter_transition = QEventTransition(button1, QEvent.Enter)
        enter_transition.setTargetState(s2)
        s1.addTransition(enter_transition)

        leave_transition = QEventTransition(button1, QEvent.Leave)
        leave_transition.setTargetState(s1)
        s2.addTransition(leave_transition)

        s3 = QState()
        s3.assignProperty(button1, 'text', 'Pressing...')

        press_transition = QEventTransition(button1, QEvent.MouseButtonPress)
        press_transition.setTargetState(s3)
        s2.addTransition(press_transition)

        release_transition = QEventTransition(button1, QEvent.MouseButtonRelease)
        release_transition.setTargetState(s2)
        s3.addTransition(release_transition)

        machine.addState(s1)
        machine.addState(s2)
        machine.addState(s3)

        machine.setInitialState(s1)
        machine.start()


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
