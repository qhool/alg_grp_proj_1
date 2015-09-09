#!/usr/bin/env python
import sort_tester
import unittest
import sys

class SortTest(sort_tester.SortTester):
    #TestSorts expects in-place sort
    def sort(self,items):
        items.sort()

if __name__ == '__main__':
    unittest.main()
