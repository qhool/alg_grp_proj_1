import unittest
from copy import copy
from random import randrange

class SortTester(unittest.TestCase):
    def multiplicities(self,items):
        d = dict()
        for i in items:
            if not i in d:
                d[i] = 0
            d[i] += 1
        return d

    def assertSorted(self,orig,items):
        self.assertEqual(len(orig),len(items))
        for i in range(1,len(items)):
            self.assertTrue(items[i] >= items[i-1])
        self.assertEqual(self.multiplicities(orig),self.multiplicities(items))

    def test_inorder(self):
        for i in range(1,100):
            for d in [-1,1,-2,2]:
                items = range(1,i,d)
                srt = copy(items)
                self.sort(srt)
                self.assertSorted(items,srt)


    def test_random(self):
        for n in range(500):
            for i in range(3):
                items = [ randrange(1000) for x in range(n) ]
                srt = copy(items)
                self.sort(srt)
                self.assertSorted(items,srt)
