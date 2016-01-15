#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Widget(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.label = QtGui.QLabel("text")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color: green")
        font = QtGui.QFont('Helvetica', 24, QtGui.QFont.Bold)
        self.label.setFont(font)

        self.resize(500, 500)
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(5)
        self.box.setSpacing(0)
        self.box.addWidget(self.label)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())