#!/usr/bin/env python
import sort_tester
import unittest
import sys
sys.path.append("lib")
import Sorts

class InsertionTest(sort_tester.SortTester):
    #TestSorts expects in-place sort
    def sort(self,items):
        Sorts.insertion(items)

if __name__ == '__main__':
    unittest.main()
