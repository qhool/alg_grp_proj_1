#!/usr/bin/env python
import sys
sys.path.append("lib/")
import Sorts

a = [1,3,2,5,7,11,20,2,1,44]
Sorts.dual_pivot(a)
print a
