import random
from copy import copy

def dual_pivot(items,start=0,end=None):
    if end == None:
        end = len(items) - 1
    #TODO: should use insertion sort for small sublists
    if end - start < 2:
        return
    print "items", items
    print "rng", start,end
    # the start of slices is 0-based,
    # but the end of slices is 1-based
    # this is the sort of thing that makes me not like python
    a = items[start:end+1]
    print "a", a
    size = end - start
    mids = [None]*size
    low_pos = start
    hi_pos = end
    mid_pos = 0
    pivot1idx = random.randrange(size)
    pivot2idx = pivot1idx
    while pivot2idx == pivot1idx:
        pivot2idx = random.randrange(size)
    print "pivot idx", pivot1idx, pivot2idx
    if a[pivot1idx] > a[pivot2idx]:
        tmp = pivot1idx
        pivot1idx = pivot2idx
        pivot2idx = tmp
    pivot1 = a[pivot1idx]
    pivot2 = a[pivot2idx]
    print "pivots", pivot1, pivot2
    for i in range(0,end-start+1):
        if i == pivot1idx or i == pivot2idx:
            continue
        if a[i] <= pivot1:
            items[low_pos] = a[i]
            low_pos += 1
        elif a[i] > pivot2:
            items[hi_pos] = a[i]
            hi_pos -= 1
        else:
            mids[mid_pos] = a[i]
            mid_pos += 1
    print "meti", items
    items[low_pos] = pivot1
    items[hi_pos] = pivot2
    items[low_pos+1:hi_pos] = mids[0:mid_pos]
    dual_pivot(items,start,low_pos-1)
    dual_pivot(items,low_pos+1,hi_pos-1)
    dual_pivot(items,hi_pos+1,end)
