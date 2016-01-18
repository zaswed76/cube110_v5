#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

class A:
    def __init__(self):
        pass

    def get_data(self, path):
        with open(path, "r") as obj:
            return yaml.load(obj)



