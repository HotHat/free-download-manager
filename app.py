import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (
    QMenu,
    QPushButton
)
from PyQt5.QtCore import (
    QPoint,
    QRect,
    QPropertyAnimation,
    QEasingCurve,
)

from gui import Ui_MainWindow
from speed_pop_frame import SpeedPopFrame




class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frame_6.setGeometry(self.geometry())
        # self.ui.c.setGeometry(self.geometry())
        self.setStyleSheet("{background-color: #ff0000}")
        # self.ui.label.setGeometry(self.ui.cmb_speech.geometry())
        self.is_search_show = True
        self.le_search_width = None
        print("--connect slot--")
        # self.ui.btn_add.clicked.connect(self.on_btn_add_clicked)
        # self.ui.btn_start.clicked.connect(self.on_btn_start_clicked)

    def on_btn_add_pressed(self):
        """qt auto-connect slot match pattern on_pushButton_clicked
        url:https://doc.qt.io/qt-5/designer-using-a-ui-file.html#automatic-connections"""
        print("btn_plus clicked")

    def on_btn_start_pressed(self):
        print("btn_start clicked")

    def on_btn_stop_pressed(self):
        print("btn_stop clicked")

    def on_btn_trash_pressed(self):
        print("btn_trash clicked")

    def on_btn_select_dir_pressed(self):
        print("btn_select_dir clicked")
        print(self.ui.centralwidget.geometry())
        self.ui.label.setGeometry(self.ui.cmb_speech.geometry())
        # self.ui.label.po
        # self.ui.label.raise_()
        print(self.ui.label.geometry())
        print(self.geometry())
        print(self.ui.centralwidget.geometry())
        pos = self.ui.cmb_speech.mapTo(self, QPoint(0, 0))
        np = QPoint(pos.x(), pos.y() - self.ui.speed_pop.height())
        self.ui.speed_pop.move(np)
        # self.speed_pop.setGeometry(self.ui.cmb_speech.geometry())

        # self.ui.tip.move(QPoint(0, self.ui.centralwidget.height() - 200))
        # self.tip = QPushButton(self.ui.centralwidget)
        # self.tip.setText("Push Button")
        # self.tip.setStyleSheet("background-color: #ff0000")
        # self.tip.raise_()
        # self.tip.setGeometry(QRect(0, self.ui.centralwidget.height() - 100, 100, 100))

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        # print(self.ui.label.geometry())
        print(self.geometry())
        print('cmb search geometry: ', self.ui.cmb_speech.geometry())
        self.ui.frame_6.setGeometry(self.ui.centralwidget.geometry())
        pos = self.ui.cmb_speech.mapTo(self, QPoint(0, 0))
        print('pos: ', pos)
        self.ui.label.setGeometry(QRect(pos.x(), pos.y(), self.ui.cmb_speech.width(), self.ui.cmb_speech.height()))
        np = QPoint(pos.x(), pos.y() - self.ui.speed_pop.height())
        self.ui.speed_pop.move(np)



    def on_btn_search_pressed(self):
        if self.le_search_width is None:
            self.le_search_width = self.ui.le_search.width()
        print("btn_search clicked")
        if self.is_search_show:
            geometry = self.ui.le_search.geometry()
            self.anim = QPropertyAnimation(self.ui.le_search, b"geometry")
            self.anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.anim.setDuration(1000)
            self.anim.setStartValue(geometry)
            self.anim.setEndValue(QRect(geometry.x() + self.le_search_width, geometry.y(), 0, geometry.height()))
            self.anim.start()
        else:
            geometry = self.ui.le_search.geometry()
            self.anim = QPropertyAnimation(self.ui.le_search, b"geometry")
            self.anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.anim.setDuration(1000)
            self.anim.setStartValue(geometry)
            self.anim.setEndValue(QRect(geometry.x() - self.le_search_width, geometry.y(), self.le_search_width, geometry.height()))
            self.anim.start()
        self.is_search_show = not self.is_search_show


    def on_btn_menu_pressed(self,):
        print("btn_menu clicked")
        sender = self.sender()
        contextMenu = QMenu(self)
        contextMenu.setStyleSheet('{border-radius: 15px;}')
        past_from_clipboard = contextMenu.addAction("从剪贴板粘贴")
        past_url = contextMenu.addAction("从文件粘贴URL")
        contextMenu.addSeparator()
        act_start_all_bt_dw = contextMenu.addAction("开始全部种子下载")
        act_stop_all_bt_dw = contextMenu.addAction("停止全部种子下载")
        menu_port = contextMenu.addMenu("导出/导入")
        menu_port.addAction("导出所有下载项")
        menu_port.addAction("导入下载项")
        menu_port.addSeparator()
        menu_port.addAction("导出设置")
        menu_port.addAction("导入设置")
        act_about = contextMenu.addAction("关于")
        contextMenu.addSeparator()
        act_quit = contextMenu.addAction("退出")
        action = contextMenu.exec_(sender.mapToGlobal(QPoint(sender.x() - sender.width() - contextMenu.width(), sender.y() + 20)))
        # print(sender)
        # print(sender.geometry().getCoords())
        # print(sender.geometry().getRect())
        # print(sender.x() + self.x())
        # print(sender.y() + self.y())
        # print(sender.frameGeometry().x())
        # print(QtWidgets.QWidget.mapToGlobal(QPoint(sender.x() + self.x(), sender.y() + self.y())))
        # print(QtWidgets.QWidget.mapToGlobal(QPoint(sender.x(), sender.y())))
        # print(sender.geometry().topLeft())
        # print(sender.geometry().())
        # print('------------------')
        # print(sender.mapToGlobal(QPoint(sender.x(), sender.y())))
        # print('------------------')
        if action == act_quit:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = AppWindow()
    application.show()
    sys.exit(app.exec_())



