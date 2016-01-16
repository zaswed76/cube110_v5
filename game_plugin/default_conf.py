#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import dirname, join


_resource = "resource"
_icons = "icons"
_tool_name_icon = "tool.png"
_tool_name_icon_hover = "tool_hover.png"
_tool_name_icon_pressed = "tool_pressed.png"


_root_path = dirname(__file__)
_icons_path = join(_root_path, _resource, _icons)

_tool_icon = join(_icons_path, _tool_name_icon)
_tool_icon_hover = join(_icons_path, _tool_name_icon_hover)
_tool_icon_pressed = join(_icons_path, _tool_name_icon_pressed)
_index = 1



