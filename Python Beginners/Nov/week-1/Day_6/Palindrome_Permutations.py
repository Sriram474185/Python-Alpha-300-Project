from os import *
from sys import *
from collections import *
from math import *

def palindromeString(s):
    freq_map = Counter(s)
    odd_count = 0
    for count in freq_map.values():
        if count % 2 != 0:
            odd_count += 1
    if odd_count <= 1:
        return True
    else:
        return False            
    pass