from collections import defaultdict
from collections import Counter
import math


def unique_list(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

def check_list(l, x, n):
    i = 0
    try:
        for _ in range(n):
            i = l.index(x, i)+1
        return True
    except ValueError:
        return False