#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSlot

class ClickableLabel(QtGui.QLabel):
    clicked = QtCore.pyqtSignal(int, int)

    def mouseReleaseEvent(self, e):
        QtGui.QLabel.mouseReleaseEvent(self, e)
        self.clicked.emit(e.x(), e.y())


class MainWidget(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.signalMapper = QtCore.QSignalMapper()
        layout = QtGui.QVBoxLayout()
        for i in range(10):
            label = ClickableLabel('Label %s' % i)
            label.clicked.connect(self.signalMapper.map)
            self.signalMapper.setMapping(label, i)
            layout.addWidget(label)
        self.signalMapper.mapped.connect(self.showUnit)
        self.setLayout(layout)

    @pyqtSlot(int, int)
    def showUnit(self, *args, index=None):
        print(args)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWidget()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())