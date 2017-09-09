import sys
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QFrame, QScrollBar, \
    QStyle, QProxyStyle


class YqProxyStyle(QProxyStyle):
    def drawControl(self, QStyle_ControlElement, QStyleOption, QPainter, widget=None):
        # 全部自己画吧
        # super().drawControl(QStyle_ControlElement, QStyleOption, QPainter, widget)

        # QStyle_ControlElement enum控件类型
        # http://doc.qt.io/qt-5/qstyle.html#ControlElement-enum

        # QStyleOption QStyleOptionViewItem
        # The QStyleOptionViewItem class is used to describe the parameters used to draw an item in a view widget.
        # http://doc.qt.io/qt-5/qstyleoptionviewitem.html

        # QPainter
        # https://doc.qt.io/qt-5/qpainter.html

        # widget
        # 具体哪个控件类

        # print(type(QStyle_ControlElement))
        # print(type(QStyleOption))
        # print(type(QPainter))
        # print(type(widget))

        if QStyle_ControlElement == QStyle.CE_ItemViewItem:
            if isinstance(widget, YqCategoryBaseView):
                # 画拖动目的地址的!!!
                # https://doc.qt.io/qt-5/qpainter.html#RenderHint-enum
                # QPainter.setRenderHint(QPainter.Antialiasing, True)  # 抗锯齿
                # pen = QPen()
                # pen.setStyle(Qt.SolidLine)
                # pen.setColor(QColor('#3498DB'))
                # pen.setWidth(1)
                # QPainter.setPen(pen)
                # QPainter.setBrush(Qt.NoBrush)
                #
                # rect = widget.visualItemRect(widget.currentItem())
                # rect.setWidth(rect.width() - 2)
                # QPainter.drawRect(rect)


class YqCategoryItemBase(QTreeWidgetItem):
    pass


class YqCategoryBaseView(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.header().hide()

        # QTreeView
        # If this property is true the treeview will animate expansion and collapsing of branches.
        # If this property is false, the treeview will expand or collapse branches immediately
        # without showing the animation.
        self.setAnimated(True)

        # QFrame Sets the frame style to style.
        self.setFrameStyle(QFrame.NoFrame)  # QFrame draws nothing

        # QAbstractScrollArea
        # Allows touch events (see QTouchEvent) to be sent to the widget.
        # Must be set on all widgets that can handle touch events.
        # Without this attribute set, events from a touch device will be sent as mouse events.
        self.viewport().setAttribute(Qt.WA_AcceptTouchEvents, True)

        # QWidget
        # Indicates that this widget should get a QFocusFrame around it. Some widgets draw their own focus
        # halo regardless of this attribute. Not that the QWidget::focusPolicy also plays the main role in
        # whether something is given focus or not, this only controls whether or not this gets the focus frame.
        # This attribute is only applicable to macOS.
        self.setAttribute(Qt.WA_MacShowFocusRect, False)

        # QAbstractItemView
        # The ellipsis should appear in the middle of the text.
        self.setTextElideMode(Qt.ElideMiddle)

        # QTreeView
        # indentation of the items in the tree view.
        self.setIndentation(22)

        # QWidget
        # This property holds the cursor shape for this widget
        self.setCursor(Qt.ArrowCursor)

        # QWidget
        # This property holds whether mouse tracking is enabled for the widget
        self.setMouseTracking(True)

        # QAbstractScrollArea
        self.verticalScrollBar().setSingleStep(30)

        # QAbstractScrollArea never shows a scroll bar.
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # TODO: 自绘滚动条
        # self.scroll_bar = YqScrollBar(self);

        self.setStyle(YqProxyStyle())


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()

        treewidget = YqCategoryBaseView()
        hbox.addWidget(treewidget)
        self.setLayout(hbox)

        for _ in range(10):
            treewidget.addTopLevelItem(QTreeWidgetItem(['1']))


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
