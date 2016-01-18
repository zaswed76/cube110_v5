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
        # self.object_name = conf.object_name
        self.root_path = os.path.dirname(__file__)
        self.index = conf.index
        self.tool_button_name = conf.tool_object_name
        self.setObjectName(self.object_name)





        self.exit_btn = QtGui.QPushButton("EXIT", self)

        css_path = self.css_file(self.root_path, conf.style_dir,
                                conf.style_name)
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
