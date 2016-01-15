#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class BaseWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # -------------------------------------------

        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)

class MyClass(BaseWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.pyqtConfigure()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = MyClass()
    main.show()
    sys.exit(app.exec_())