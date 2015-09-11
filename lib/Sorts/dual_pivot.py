import random
import Sorts
from copy import copy

# dual-pivot quicksort, as described in
# http://iaroslavski.narod.ru/quicksort/DualPivotQuicksort.pdf
def dual_pivot(T,left=0,right=None):
    if right == None:
        right = len(T) - 1
    size =  right - left + 1
    # the lower limit of 17 is according to the paper
    if right - left + 1 < 17:
        Sorts.insertion(T,left,right)
        return

    pivot1idx = random.randrange(left,right+1)
    T[left],T[pivot1idx] = T[pivot1idx],T[left]
    pivot2idx = random.randrange(left+1,right+1)
    T[right],T[pivot2idx] = T[pivot2idx],T[right]
    #make sure left pivot is smaller
    if T[left] > T[right]:
        T[left],T[right] = T[right],T[left]
    P1, P2 = T[left], T[right]
    K = L = left + 1
    G = right - 1
    while K <= G:
        if T[K] < P1:
            T[L],T[K] = T[K],T[L]
            L += 1
            K += 1
        elif T[K] > P2:
            T[K],T[G] = T[G],T[K]
            # we haven't examined the value that was at T[G]
            # K is not advanced, so we will check it next
            G -= 1
        else:
            K += 1
    #swap pivots into final positions
    T[left],T[L-1] = T[L-1],T[left]
    T[right],T[G+1] = T[G+1],T[right]
    dual_pivot(T,left,L-1)
    dual_pivot(T,L,G)
    dual_pivot(T,G+1,right)
