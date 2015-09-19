#!/usr/bin/env python
import sort_tester
import unittest
import sys
sys.path.append("lib")
import Sorts

class IntroSortTest(sort_tester.SortTester):
    def isStable(self):
        return False

    #TestSorts expects in-place sort
    def sort(self,items):
        Sorts.introsort(items)

if __name__ == '__main__':
    unittest.main()
