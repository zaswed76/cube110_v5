#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from gui import widgets as gui

icon_setting_size = 44
icon_game_size = 64
spacing_setting = 28
margin_setting = 0
stretch_game_tool = 2
stretch_display_layout = 11
stretch_display_widget = 35
stretch_setting_widget = 2


class GameBox(gui.Frame):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.box = gui.Box(gui.Box._vertical, self, 50, 50)
        self.box.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

    def create_button(self, options):
        button = gui.GameButton(options)
        button.setIconSize(QtCore.QSize(icon_game_size, icon_game_size))
        button.setFixedSize(icon_game_size, icon_game_size)
        self.box.insertWidget(options["index"], button)
        return button




class GlobalMenu(gui.MenegerFrame):

    def __init__(self, name, parent=None, visual_parent=None):
        super().__init__(name, parent)
        self.parent = parent
        self.setParent(visual_parent)

        self.tool_game_box = GameBox("tool_game", self)

        self.setting_widget = gui.ToolGame("setting")

        self.display_widget = gui.ToolGame("display")

        self.exit = gui.SettingButton("exit_button", icon_setting_size)
        self.volume = gui.SettingButton("volume_button", icon_setting_size)
        self.config = gui.SettingButton("config_button", icon_setting_size)

        display_layout = gui.Box(gui.Box._vertical, None, 0, 0)
        box_base = gui.Box(gui.Box._horizontal, self, 0, 0)
        self.setting_layout = gui.Box(gui.Box._horizontal,
                                 QWidget_parent=self.setting_widget,
                                 spacing=spacing_setting,
                                 margin=margin_setting)

        box_base.addWidget(self.tool_game_box, stretch_game_tool)
        box_base.addLayout(display_layout, stretch_display_layout)
        display_layout.addWidget(self.display_widget, stretch_display_widget)
        display_layout.addWidget(self.setting_widget, stretch_setting_widget)


        self.add_setting_buttons()
        self.set_actions_setting_buttons()

    def add_setting_buttons(self):
        self.setting_layout.addStretch(1)
        self.setting_layout.insertWidget(-1, self.config)
        self.setting_layout.insertWidget(-1, self.volume)
        self.setting_layout.insertWidget(-1, self.exit)
        self.setting_layout.addStretch(1)
        # self.setting_layout.insertSpacing(-1, 5)

    def set_actions_setting_buttons(self):
        self.parent.register_control(self.exit, "exit")

    def create_game_button(self, options):
        return self.tool_game_box.create_button(options)

    def add_plagin_game(self, game_plugins):
        for index, widg in enumerate(game_plugins):
            icon = widg.tool_icon
            self.controls.append(gui.GameButton("name", index, icon))
            self.controls[index].clicked.connect(self.press_game)
            self.global_game_window.tool_game_box.add_game_control(
                    self.controls[index])

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GlobalMenu("global_menu")
    main.show()
    sys.exit(app.exec_())