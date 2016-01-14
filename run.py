#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
import paths
from edit_scr import edit_main
from cube_manager import main
from libs import data



css_default = "base.css"
css_path = os.path.join(paths.get_css_dir(), css_default)

app = QtGui.QApplication(sys.argv)
app.setStyleSheet(open('{}'.format(css_path), "r").read())
m = main.BaseWindow()
m.add_games()
# m.add_games_to_stack()
# m.create_tool_buttons()
m.show()
sys.exit(app.exec_())
