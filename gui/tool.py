#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore

margin = 8
spacing = 10
icon_size=16

class ToolButton(QtGui.QToolButton):
    def __init__(self, name, parent=None):
        super().__init__()
        self.parent = parent
        self.name = name
        self.setObjectName(name)


class Group(QtGui.QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(27)
        self.box = QtGui.QHBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(10)

    def add_action(self, action):
        self.box.addWidget(action)


class Tool(QtGui.QToolBar):
    def __init__(self, height, parent=None):
        super().__init__(parent)
        self.setFixedHeight(height)
        self.setMovable(False)
        self.button = {}

    def init_group(self, *actions_name, icon_size=icon_size):
        count_act = len(actions_name)
        width_group = (icon_size * count_act) + (margin * 2) + (
        (count_act - 1) * spacing)
        group = Group()
        print(width_group)
        group.setFixedWidth(120)

        for name in actions_name:
            self.button[name] = ToolButton(name, self)
            group.add_action(self.button[name])
        self.addWidget(group)
