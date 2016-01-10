#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QObject, pyqtSlot
from gui import widgets as gui
from cube_manager import menu_window


class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        self.center = gui.MenegerFrame("center_frame")
        self.setCentralWidget(self.center)
        box = gui.Box(gui.Box._horizontal, self.center, 0, 0)

        self.stack = gui.StackedLayout()
        box.addLayout(self.stack)

        self.menu = menu_window.GlobalMenu("global_menu", parent=self,
                                           visual_parent=self.center)
        self.stack.addWidget(self.menu)

    def register_control(self, control_object, slot, *args):
        control_object.clicked.connect(getattr(self, slot))

    @pyqtSlot()
    def exit(self):
        sys.exit()

    def add_game(self, game):
        self.stack.addWidget(game)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())
