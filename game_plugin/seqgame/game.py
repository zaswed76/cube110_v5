#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from PyQt4 import QtGui

from game_plugin.seqgame import conf as cfg
from libs import plugin

root_path = os.path.dirname(__file__)


class GamePlugin(plugin.WidgetPlugin):
    def __init__(self):
        super().__init__(cfg.object_name, root_path, cfg.index,
                         cfg.tool_object_name, cfg.style_name)
        self.name = cfg.object_name
        self.root_path = root_path
        self.index = cfg.index
        self.tool_btn_name = cfg.tool_object_name
        self.setObjectName(self.name)
        self.style_file = cfg.style_name

        self.exit_btn = QtGui.QPushButton("EXIT", self)

        css_path = self.css_file(self.root_path, cfg.style_dir,
                                 self.style_file)
        self.setStyleSheet(open('{}'.format(css_path), "r").read())

    @property
    def home_btn(self):
        return self.exit_btn

    def __doc__(self):
        return "{}".format(plugin.WidgetPlugin)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GamePlugin()
    main.show()
    sys.exit(app.exec_())
