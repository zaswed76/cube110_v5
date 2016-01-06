#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from gui import widgets as gui


class GlobalMenu(gui.MenegerFrame):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.setParent(parent)

        self.tool_game_widget = gui.ToolGame("tool_game")
        self.setting_widget = gui.ToolGame("setting")
        self.display_widget = gui.ToolGame("display")

        self.exit = gui.SettingButton("exit_button", 48)
        self.volume = gui.SettingButton("volume_button", 48)
        self.config = gui.SettingButton("config_button", 48)

        display_layout = gui.Box(gui.Box._vertical)
        box_base = gui.Box(gui.Box._horizontal, self)
        setting_layout = gui.Box(gui.Box._horizontal,
                                 QWidget_parent=self.setting_widget,
                                 spacing=35)

        box_base.addWidget(self.tool_game_widget, 2)
        box_base.addLayout(display_layout, 9)
        display_layout.addWidget(self.display_widget, 35)
        display_layout.addWidget(self.setting_widget, 1)

        setting_layout.addStretch(1)
        setting_layout.insertWidget(-1, self.config)
        setting_layout.insertWidget(-1, self.volume)
        setting_layout.insertWidget(-1, self.exit)
        setting_layout.insertSpacing(-1, 5)

    def setting_button(self, name):
        pass



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GlobalMenu("global_menu")
    main.show()
    sys.exit(app.exec_())