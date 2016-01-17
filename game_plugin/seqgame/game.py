#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
from libs import plugin
from game_plugin.seqgame import conf

print(dir(conf))


class GamePlugin(plugin.WidgetPlugin):

    def __init__(self):
        super().__init__()
        self.setObjectName(conf.object_name)
        self.root_path = os.path.dirname(__file__)
        self.options = dict(
                style_path = conf.style_path,
                tool_icon_objectname = conf.tool_object_name,
                name = conf.object_name,
                index=conf.index,
                tool_icon=conf.tool_icon,
                tool_icon_hover=conf.tool_icon_hover,
                tool_icon_pressed=conf.tool_icon_pressed
        )
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)
        self.label = QtGui.QPushButton()
        self.label.setObjectName('game1')
        self.label.setFixedSize(600, 600)

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
