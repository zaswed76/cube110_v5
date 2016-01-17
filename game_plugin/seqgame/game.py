#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
from libs import plugin
from game_plugin.seqgame import conf



class GamePlugin(plugin.WidgetPlugin):
    def __init__(self):
        super().__init__()
        self.setObjectName(conf.object_name)
        self.root_path = os.path.dirname(__file__)

        css_path = os.path.join(self.root_path, conf.style_dir,
                                conf)
        self.setStyleSheet(open('{}'.format(css_path), "r").read())

        self.tool_button_name = conf.tool_object_name
        self.index = conf.index
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)
        self.label = QtGui.QPushButton()
        self.label.setObjectName('game1')
        self.label.setFixedSize(600, 600)

        self.label.setText(str(self.index))
        self.box.addWidget(self.label, 0, QtCore.Qt.AlignCenter)

    @property
    def home_btn(self):
        return self.label

    def __doc__(self):
        return "{}".format(plugin.WidgetPlugin)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.show()
    sys.exit(app.exec_())
