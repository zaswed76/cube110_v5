#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore

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
        self.setFixedWidth(66)
        self.box = QtGui.QHBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)

    def add_action(self, action):
        self.box.addWidget(action)






class Tool(QtGui.QToolBar):
    def __init__(self, height, parent=None):

        super().__init__(parent)
        self.setFixedHeight(height)
        self.setMovable(False)
        self.button = {}

    def init_group(self, *actions_name):
        group = Group()
        for name in actions_name:
            self.button[name] = ToolButton(name, self)
            group.add_action(self.button[name])
        self.addWidget(group)





