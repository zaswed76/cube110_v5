#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from functools import partial
from PyQt4 import QtGui
from PyQt4.QtCore import QObject, pyqtSlot
from gui import widgets as gui
from cube_manager import menu_window
from libs import plugin


class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        self.center = gui.MenegerFrame("center_frame")
        self.setCentralWidget(self.center)

        self.adapter_plugin = plugin.AdapterPluginsGame(
                "games", 'game', "GamePlugin")
        self.game_widgets = []
        self.controls = []

        box = gui.Box(gui.Box._horizontal, self.center, 0, 0)

        self.stack = gui.StackedLayout()
        box.addLayout(self.stack)

        self.global_game_window = menu_window.GlobalMenu(
                "global_menu", parent=self,
                visual_parent=self.center)
        self.stack.addWidget(self.global_game_window)


    def register_control(self, control_object, slot, *args):
        control_object.clicked.connect(getattr(self, slot))

    @pyqtSlot()
    def exit(self):
        sys.exit()

    def add_game(self, game):
        self.stack.addWidget(game)

    def add_games(self, ):
        mod_objects = self.adapter_plugin.plugin_objects(
                self.adapter_plugin.paths)
        for game_widget in mod_objects:
            game_widget.label.clicked.connect(self.return_to_global_window)
            self.stack.addWidget(game_widget)
            index = game_widget.index
            icon = game_widget.tool_icon
            button = self.global_game_window.create_game_button(
                index,
                icon)
            button.clicked.connect(partial(self.press_game, index))

    @pyqtSlot(int)
    def press_game(self, s):
        pass
        self.stack.setCurrentIndex(s)

    def return_to_global_window(self):
        self.stack.setCurrentIndex(0)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())
