#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import yaml
from PyQt4 import QtGui
import paths
from cube_manager import main

def get_data(path):
    with open(path, "r") as obj:
        return yaml.load(obj)


css_default = "base.css"
config_default = "etc/config.yaml"
css_path = os.path.join(paths.get_css_dir(), css_default)

app = QtGui.QApplication(sys.argv)
app.setStyleSheet(open('{}'.format(css_path), "r").read())
config = get_data(config_default)
m = main.BaseWindow(config)
m.add_games()

m.show()
sys.exit(app.exec_())

