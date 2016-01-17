#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

def get_data(path):
    with open(path, "r") as obj:
        return yaml.load(obj)
x = get_data("test.yaml")["dct"]
print(type(x["a"]))