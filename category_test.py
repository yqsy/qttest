import sys
import traceback

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPen, QColor, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QFrame, QScrollBar, \
    QStyle, QProxyStyle, QStyleOptionViewItem


class YqProxyStyle(QProxyStyle):
    def drawControl(self, QStyle_ControlElement, QStyleOption, QPainter, widget=None):
        # 全部自己画吧
        # super().drawControl(QStyle_ControlElement, QStyleOption, QPainter, widget)

        # QStyle_ControlElement enum控件类型
        # http://doc.qt.io/qt-5/qstyle.html#ControlElement-enum

        # QStyleOption QStyleOptionViewItem 可以得到QModelIndex哦
        # QStyleOptionViewItem contains all the information that QStyle functions need to draw the items for Qt's model/view classes.
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
                # 画的item
                item = widget.itemFromIndex(QStyleOption.index)

                item.draw_item_body(QPainter, QStyleOption)


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_item_body(self, QPainter, QStyleOption):
        if not isinstance(QStyleOption, QStyleOptionViewItem):
            raise Exception('fuck')

        selected = True if QStyleOption.state & QStyle.State_Selected else False

        # 通过item可以得到整个treewidget哦!
        # .style又回到了YqProxyStyle
        style = self.treeWidget().style()

        # 得到在treewidget中要画的方块?
        rect = style.subElementRect(QStyle.SE_ItemViewItemDecoration, QStyleOption, self.treeWidget())

        if not QStyleOption.icon.isNull():
            icon_size = 14
            rect.adjust(-6, 0, 0, 0)
            rect.setTop(QStyleOption.rect.top() + (QStyleOption.rect.height() - icon_size) / 2)
            rect.setWidth(icon_size)
            rect.setHeight(icon_size)
            if selected:
                QStyleOption.icon.paint(QPainter, rect, Qt.AlignCenter, QIcon.Selected)
            else:
                QStyleOption.icon.paint(QPainter, rect, Qt.AlignCenter, QIcon.Normal)


class YqFloderItem(YqCategoryItemBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        icon = QIcon()
        icon.addPixmap(QPixmap('./icon/comments.png'), QIcon.Normal)
        icon.addPixmap(QPixmap('./icon/comments_selected.png'), QIcon.Selected)

        self.setIcon(0, icon)


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

    def draw_item_body(self):
        pass


class MyWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()

        treewidget = YqCategoryBaseView()
        hbox.addWidget(treewidget)
        self.setLayout(hbox)

        num = 0

        for _ in range(10):
            treewidget.addTopLevelItem(YqFloderItem([str(num)]))
            num = num + 1

        root = treewidget.invisibleRootItem()

        for _ in range(3):
            root.addChild(YqFloderItem(root, [str(num)]))


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
