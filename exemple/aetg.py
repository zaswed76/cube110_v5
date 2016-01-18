#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Test2:
    def __init__(self):
        self._a = None
        print("_a" in self.__dir__())




class A(Test2):
    def __init__(self):
        super().__init__()





a = A()





