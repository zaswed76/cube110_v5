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
        """

        :param direction: Box._horizontal \ Box._vertical
        :param QWidget_parent: QWidget
        :param margin: поле вокруг
        :param spacing: интервал (шаг) между виджетами
        """
        super().__init__(direction, QWidget_parent)
        self.setDirection(direction)
        self.setMargin(margin)
        self.setSpacing(spacing)


class ToolButton(QtGui.QToolButton):
    def __init__(self, name, parent=None):
        super().__init__()
        self.parent = parent
        self._name = name
        self.setObjectName(self.name)

    @property
    def name(self):
        return str(self._name)

    @name.setter
    def name(self, name):
        print(name)
        self._name = str(name)


class GameButton(ToolButton):
    def __init__(self, object_name, index):
        super().__init__(object_name)
        self.index = index
        self.setObjectName(self._name)

    def __repr__(self):
        return """
        object - {};
        object_name - {};
        index - {}
        """.format(self.__class__.__name__, self._name, self.index)


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

