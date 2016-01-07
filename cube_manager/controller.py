#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Controller:
    def __init__(self, main):
        self.main = main

    def exit(self):
        self.main.exit()
