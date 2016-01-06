#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from gui import widgets as gui

icon_setting_size = 44
spacing_setting = 28
margin_setting = 7
stretch_game_tool = 2
stretch_display_layout = 9
stretch_display_widget = 35
stretch_setting_widget = 2


class GlobalMenu(gui.MenegerFrame):


    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.setParent(parent)

        self.tool_game_widget = gui.ToolGame("tool_game")
        self.setting_widget = gui.ToolGame("setting")
        self.display_widget = gui.ToolGame("display")

        self.exit = gui.SettingButton("exit_button", icon_setting_size)
        self.volume = gui.SettingButton("volume_button", icon_setting_size)
        self.config = gui.SettingButton("config_button", icon_setting_size)

        display_layout = gui.Box(gui.Box._vertical, None, 0, 0)
        box_base = gui.Box(gui.Box._horizontal, self, 0, 0)
        setting_layout = gui.Box(gui.Box._horizontal,
                                 QWidget_parent=self.setting_widget,
                                 spacing=spacing_setting,
                                 margin=margin_setting)

        box_base.addWidget(self.tool_game_widget, stretch_game_tool)
        box_base.addLayout(display_layout, stretch_display_layout)
        display_layout.addWidget(self.display_widget, stretch_display_widget)
        display_layout.addWidget(self.setting_widget, stretch_setting_widget)

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