import sys
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QTreeView, QHBoxLayout, QStyledItemDelegate, QStyleOptionProgressBar, \
    QStyle, QProgressBar


class MyDelegate(QStyledItemDelegate):
    """
    渲染treeview中的一栏成progressbar
    """

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex):
        super().paint(QPainter, QStyleOptionViewItem, QModelIndex)

        # print('({} {})'.format(QModelIndex.row(), QModelIndex.column()))
        if QModelIndex.column() == 4:
            progressbar = QStyleOptionProgressBar()
            # style
            view_bar = QProgressBar()

            view_bar.setStyleSheet('QProgressBar {'
                                   'border-radius: 25px;'
                                   'border: 2px solid;'
                                   'background-color: pink;}'
                                   )

            progressbar.initFrom(view_bar)

            # 位置
            progressbar.rect = QStyleOptionViewItem.rect

            # 获取当前数值和最大数值like:1500/3600
            current_progress = QModelIndex.model().data(QModelIndex, Qt.DisplayRole)
            two_ele = current_progress.split('/')
            current = int(two_ele[0])
            max = int(two_ele[1])

            # 设置progressbar 进度
            progressbar.minimum = 0
            progressbar.maximum = max
            progressbar.progress = current

            # 居中
            progressbar.textAlignment = Qt.AlignCenter

            # 文字
            progressbar.text = '{0:.2f}%'.format(current / max)
            progressbar.textVisible = True

            # QPainter.save()
            view_bar.style().drawControl(QStyle.CE_ProgressBar, progressbar, QPainter, view_bar)
            # QPainter.restore()


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(1000, 500)
        treeview = QTreeView()

        box = QHBoxLayout()
        box.addWidget(treeview)
        self.setLayout(box)

        treeview.setModel(self.get_tree_model())
        treeview.setItemDelegate(MyDelegate())

    def get_tree_model(self):
        item_model = QStandardItemModel()
        root = item_model.invisibleRootItem()

        item_model.setHorizontalHeaderLabels(['名称', '账号', '交易类型', '金额', '进度', '委托详情', '开始时间', '结束时间'])

        row1 = ['组合指令2', '37000033/37000034', '买入', '1.50万', '1500/3600', '15', '13:01:12', '13:01:12']

        for idx, ele in enumerate(row1):
            row1[idx] = QStandardItem(ele)

        row1_1 = ['37000033', '', '买入', '7032.00', '700/1600', '7', '']
        for idx, ele in enumerate(row1_1):
            row1_1[idx] = QStandardItem(ele)

        row1_1_1 = ['SZ000002 万科A', '', '买入', '1183.00', '100/100', '1', '', '']
        for idx, ele in enumerate(row1_1_1):
            # 每一个元素都是一个item!!!!!!!!!!
            row1_1_1[idx] = QStandardItem(ele)


        root.appendRow(row1)
        row1[0].appendRow(row1_1)
        row1_1[0].appendRow(row1_1_1)

        row1[2].setData(QBrush(Qt.red), Qt.ForegroundRole)
        row1_1[2].setData(QBrush(Qt.red), Qt.ForegroundRole)
        row1_1_1[2].setData(QBrush(Qt.red), Qt.ForegroundRole)

        row1[5].setData(QBrush(QColor(43, 145, 175)), Qt.ForegroundRole)
        row1_1[5].setData(QBrush(QColor(43, 145, 175)), Qt.ForegroundRole)
        row1_1_1[5].setData(QBrush(QColor(43, 145, 175)), Qt.ForegroundRole)

        return item_model


def main():
    sys.excepthook = traceback.print_exception
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
