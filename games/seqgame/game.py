#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
from libs import plugin


class GamePlugin(plugin.WidgetPlugin):
    """
    bbb
    """
    def __init__(self):
        super().__init__()

        self.root_path = os.path.dirname(__file__)
        self.index = 1
        # self.tool_icon = os.path.join(self.root_path, "resource/icons",
        #                               "tool.png")
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)
        self.label = QtGui.QPushButton()
        self.label.setFixedSize(600, 600)
        print(self.tool_icon)
        self.label.setIcon(QtGui.QIcon(self.tool_icon))
        self.box.addWidget(self.label, 0, QtCore.Qt.AlignCenter)

    def __doc__(self):
        return "{}".format(plugin.WidgetPlugin)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.show()
    sys.exit(app.exec_())