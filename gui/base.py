#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

from gui import tool


class Main(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.center = QtGui.QWidget()
        self.setCentralWidget(self.center)


    def add_tool(self, tool_bar):
        self.addToolBar(QtCore.Qt.BottomToolBarArea, tool_bar)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())