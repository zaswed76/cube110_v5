#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from PyQt4 import QtGui, QtCore
import paths
from gui import base, tool
from libs import data

setting_file = os.path.join(paths.get_edit_settings(),
                            "edit_settings.json")
config = data.JsonData(setting_file)
config.load()


class EditWindow(base.Main):
    tool_area = {"bottom": QtCore.Qt.BottomToolBarArea,
                 "top": QtCore.Qt.TopToolBarArea}
    def __init__(self):
        super().__init__()
        self.setFixedSize(604, 604)
        self.config = config
        self.tool = tool.Tool(config["height_tool"], parent=self)
        self.addToolBar(self.tool_area[config["tool_area"]], self.tool)
        self.tool.init_group("prev", "next")
