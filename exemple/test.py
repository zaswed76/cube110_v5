#!/usr/bin/env python
# -*- coding: utf-8 -*-


a = {"x": 10, "y": 20}

class A:
    def __init__(self, **kwargs):
        pass
        self.__dict__.update(kwargs)

q = A(**a)
print(q.x)