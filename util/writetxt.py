# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

import codecs
import time
f = codecs.open('%s.txt'%int(time.time()), 'wt')
f.write("hello")
f.write("\n")
f.write("word")