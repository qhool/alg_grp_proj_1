import numpy as np
import math
import math
import numpy as np
import time
import copy

class HeapSort:

  def __init__(self, array, start, last):
    self.length = last - start + 1 
    self.array = array
    self.start = start
    self.last = last

  def parent(self, i):
    return (((i-self.start))//2) + self.start

  def left(self, i):
    return 2*(i-self.start) + self.start

  def right(self, i):
    return 2*(i-self.start) + 1 + self.start

  def swap(self, i, j):
    self.array[i], self.array[j] = self.array[j], self.array[i]


  def max_heapify(self, i):
    left = self.left(i)
    right = self.right(i)
    if left <= self.last and self.array[left] > self.array[i]:
      largest = left
    else: 
      largest = i 
    if right <= self.last and self.array[right] > self.array[largest]:
      largest = right
    if largest != i:
      self.swap(i, largest)
      self.max_heapify(largest)


  def build_max_heap(self):
    for i in range(self.parent(self.last), self.start-1, -1):
      self.max_heapify(i)
      

  def heapsort(self):
    self.build_max_heap()
    for i in range(self.last, self.start-1, -1):
      self.array[self.start], self.array[i] = self.array[i], self.array[self.start]
      self.last -= 1
      self.max_heapify(self.start)

    return self.array


def heapsort(ar, start = 0, last = False):
  if not last:
    last = len(ar) - 1
  HeapSort(ar, start, last).heapsort()

def partition(A, p, r):
    i = p - 1
    for j in range(p, r):
        if A[j] < A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r],  A[i + 1]
    return i + 1


def quicksort(A, p = 0, r = None):
    if r == None:
        r = len(A) - 1
    if p < r:
        x = np.random.randint(p, r + 1)
        A[r], A[x] = A[x], A[r]
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def introsort(A, p=0, r = None, maxdepth = None):
  if len(A) == 0:
    return
  if maxdepth == None:
    maxdepth = math.floor(math.log(len(A))) * 2
  if r == None:
    r = len(A)-1

  if p >= r:
    return  # base case
  elif maxdepth == 0:
      heapsort(A,p,r)
  else:
      q = partition(A, p, r)  # assume this function does pivot selection, p is the final position of the pivot
      introsort(A, p, q - 1, maxdepth - 1)
      introsort(A, q + 1, r, maxdepth - 1)


A = [234,2342,34,34,32,12,1,3,4,6,3,2,8,9,6,5,4,3,3,2,1]
print A
# #quicksort(A)
# #heapsort(A)
introsort(A)
print A
