#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from functools import partial
import yaml
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
import paths
from gui import widgets as gui
from cube_manager import menu_window
from libs import plugin


class BaseWindow(QtGui.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.config = config
        print(type(self.config['global_game_window']['spacing_setting']))
        self.showFullScreen()
        self.center = gui.MenegerFrame("center_frame")
        self.setCentralWidget(self.center)

        self.adapter_plugin = plugin.AdapterPluginsGame(
                "game_plugin", 'game', "GamePlugin")
        self.game_widgets = []
        self.controls = []

        box = gui.Box(gui.Box._horizontal, self.center, 0, 0)

        self.stack = gui.StackedLayout()
        box.addLayout(self.stack)

        self.global_game_window = menu_window.GlobalMenu(
                "global_menu", parent=self,
                visual_parent=self.center,
        config=config["global_game_window"])
        self.stack.add_widget(self.global_game_window)


    def register_control(self, control_object, slot, *args):
        control_object.clicked.connect(getattr(self, slot))

    @pyqtSlot()
    def exit(self):
        sys.exit()

    def add_game(self, game):
        self.stack.addWidget(game)

    def add_games(self):

        mod_objects = self.adapter_plugin.plugin_objects(
                self.adapter_plugin.paths)
        for game_widget in mod_objects:
            object_name = game_widget.object_name
            index = game_widget.index
            button_name = game_widget.tool_button_name
            home_btn = game_widget.home_btn

            self.plugin_valid(index, button_name, object_name)

            home_btn.clicked.connect(self.return_to_global_window)
            self.stack.insertWidget(index, game_widget)



            button = self.global_game_window.create_game_button(button_name, index)
            button.clicked.connect(partial(self.press_game, index))

    def plugin_valid(self, *atr):
        for i in atr:
            if i is None:

                raise Exception("ERROR - {} not None".format(i))

    @pyqtSlot(int)
    def press_game(self, s):
        pass
        self.stack.setCurrentIndex(s)

    def return_to_global_window(self):
        self.stack.setCurrentIndex(0)


if __name__ == '__main__':


    css_default = "user1.css"
    css_path = os.path.join(paths.get_css_dir(), css_default)


    app = QtGui.QApplication(sys.argv)
    # app.addLibraryPath("/home/serg/project/cube110_v5/libs")
    # print(app.libraryPaths())
    app.setStyleSheet(open('{}'.format(css_path), "r").read())
    m = BaseWindow()
    m.add_games()

    m.show()
    sys.exit(app.exec_())