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
        self.resize(500, 500)
        self.root_path = os.path.dirname(__file__)
        self.index = 2
        self.tool_icon = os.path.join(self.root_path, "resource/icons",
                                      "tool.png")
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)
        self.label = QtGui.QLabel("1")
        self.label.setPixmap(QtGui.QPixmap(self.tool_icon).scaled(178, 178))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.box.addWidget(self.label)

    def __doc__(self):
        return "{}".format(plugin.WidgetPlugin)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.show()
    sys.exit(app.exec_())