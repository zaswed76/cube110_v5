#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from glob import glob

search_in = r'E:\temp\source_folder_mp3'
move_to = r'E:\temp\target folder_mp3'
pat = "*.mp3"


def move(search_in, move_to):
    lst = glob(os.path.join(search_in, pat))
    for totalonrun, source in enumerate(lst):
        target_file = os.path.join(move_to, os.path.basename(source))
        os.rename(source, target_file)
        print("файл - {} перемещён".format(source))
    print("всего перемещено - {} файлов".format(len(lst)))


move(search_in, move_to)
