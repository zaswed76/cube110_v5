#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore

margin = 4
spacing = 4


class Box(QtGui.QBoxLayout):
    _horizontal = QtGui.QBoxLayout.LeftToRight
    _vertical = QtGui.QBoxLayout.TopToBottom

    def __init__(self, direction, QWidget_parent=None,
                 margin=margin, spacing=spacing):
        super().__init__(direction, QWidget_parent)
        self.setDirection(direction)
        self.setMargin(margin)
        self.setSpacing(spacing)


class ToolButton(QtGui.QToolButton):
    def __init__(self, name, parent=None):
        super().__init__()
        self.parent = parent
        self._name = name
        print(self._name, "OBJ")
        self.setObjectName(self.name)

    @property
    def name(self):
        return str(self._name)

    @name.setter
    def name(self, name):
        print(name)
        self._name = str(name)


class GameButton(ToolButton):
    _name_button = "game_button"

    def __init__(self, options):
        super().__init__(options['tool_icon_objectname'])

        self.icon_path = options['tool_icon']
        self.icon_path_hover = options['tool_icon_hover']
        self.index = options['index']
        self._name = options['tool_icon_objectname']
        # # self.name = self._name_button + str(options['name'])
        # print(options['tool_icon_objectname'], "EEEE")
        self.setObjectName(self._name)




    def add_icon(self, icon_path):
        if not os.path.isfile(icon_path):
            self.setText("NOT\nICON")
        else:
            self.setIcon(QtGui.QIcon(icon_path))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

class SettingButton(QtGui.QPushButton):
    def __init__(self, name, size):
        """

        :type size_button: int
        :type size_icon: int
        :type name: str
        """
        super().__init__()
        self.setObjectName(name)
        self.setIconSize(QtCore.QSize(size, size))
        self.setFixedSize(size + 2, size + 2)


class Frame(QtGui.QFrame):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.setObjectName(name)
        self.setParent(parent)


class MenegerFrame(Frame):
    def __init__(self, name, parent=None):
        super().__init__(name, parent=None)


class ToolGame(Frame):
    def __init__(self, name, parent=None):
        super().__init__(name, parent=None)


class FaderWidget(QtGui.QWidget):
    def __init__(self, old_widget, new_widget):
        QtGui.QWidget.__init__(self, new_widget)

        self.old_pixmap = QtGui.QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)
        self.pixmap_opacity = 1.0

        self.timeline = QtCore.QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(999)
        self.timeline.start()

        self.resize(new_widget.size())
        self.show()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()

    def animate(self, value):
        self.pixmap_opacity = 1.0 - value
        self.repaint()


class StackedLayout(QtGui.QStackedLayout):
    def __init__(self, parent=None, *__args):
        super().__init__(*__args)


    def add_widget(self, QWidget):
        self.addWidget(QWidget)

