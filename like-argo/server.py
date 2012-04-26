# -*- coding: utf-8 -*-
from chaofeng import Server
import frame
from chaofeng.g import marks,mark,static
import config

if __name__ == '__main__' :
    s = Server(marks[config.root])
    s.run()
