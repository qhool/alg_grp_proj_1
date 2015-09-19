import numpy as np
import math


class HeapSort:

  def __init__(self, array):
    self.length = len(array) - 1 
    self.array = array

  def parent(self, i):
    return ((i-1)//2)

  def left(self, i):
    return 2*i

  def right(self, i):
    return 2*i + 1


  def max_heapify(self, i):
    left = self.left(i)
    right = self.right(i)
    if left <= self.length and self.array[left] > self.array[i]:
      largest = left
    else: 
      largest = i 
    if right <= self.length and self.array[right] > self.array[largest]:
      largest = right
    if largest != i:
      self.array[i], self.array[largest] = self.array[largest], self.array[i]
      self.max_heapify(largest)


  def build_max_heap(self):
    for i in range(self.parent(self.length + 1), -1, -1):
      self.max_heapify(i)
      

  def heapsort(self):
    self.build_max_heap()
    for i in range(self.length, 0, -1):
      self.array[0], self.array[i] = self.array[i], self.array[0]
      self.length -= 1
      self.max_heapify(0)

    return self.array


def heapsort(ar):
  heapity = HeapSort(ar)
  heapity.heapsort()


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
      temp = A[p:r+1]
      heapsort(temp)
      A[p:r+1] = temp
  else:
      q = partition(A, p, r)  # assume this function does pivot selection, p is the final position of the pivot
      introsort(A, p, q - 1, maxdepth - 1)
      introsort(A, q + 1, r, maxdepth - 1)



# A = [234,2342,34,34,32,12,1,3,4,6,3,2,8,9,6,5,4,3,3,2,1]
# print A
# #quicksort(A)
# #heapsort(A)
# introsort(A)
# print A
