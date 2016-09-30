#!/usr/bin/python3

import sys
from DivisorsGenerator import *

if len(sys.argv) <= 1:
	print('too few arguments')
else:
	print(DivisorsGenerator(sys.argv[1]).get())

