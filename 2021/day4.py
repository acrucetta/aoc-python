import util
import sys
import re
import numpy as np
import pandas as pd

from util import log

'''
Day 4
'''

'''
General notes:
    1. One input is the first two lines of the input file.
    2. The rest of the input is a grid of 5x5 numbers. 
    3. We need to walk through the bingo list and iterate over each grid.
    4. Each grid must be stored in some form of list of list or dictionary containing
    each of the 5x5 numbers.
'''

with open(file='2021/data/04.txt') as f:
    line1, line2 = next(f).strip(), next(f).strip()
    print(line1 + " " + line2)





