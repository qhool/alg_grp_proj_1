#!/usr/bin/env python
import sys
sys.path.append("lib/") #probably a better way to do this
import random
import SortMonitor

c = SortMonitor.Comparable(2)
d = SortMonitor.Comparable(3)
c < d
print c.comparisons
print d.comparisons
el = SortMonitor.Sequence([SortMonitor.Comparable(random.randrange(1000)) for x in range(1,1000)])
#print el
el.sort()
#print el
print reduce(lambda tot, c: tot + c.comparisons, el, 0)
print el.updates
