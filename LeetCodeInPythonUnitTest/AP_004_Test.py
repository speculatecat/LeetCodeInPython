# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com
import unittest
from LeetCodeInPython.AP_004 import Solution

class MyTestCase(unittest.TestCase):
    def test_findMedianSortedArrayg(self):
        s = Solution()
        t1_nums1 = [1,3]
        t1_nums2 = [2]
        r1_nums = s.findMedianSortedArrays(t1_nums1,t1_nums2)
        er1_nums = float(2)
        self.assertEqual(r1_nums,er1_nums)

        t2_nums1 = [1,2]
        t2_nums2 = [3,4]
        r2_nums = s.findMedianSortedArrays(t2_nums1,t2_nums2)
        er2_nums = float(2.5)
        self.assertEqual(r2_nums,er2_nums)

    def test_insertionSort(self):
        s = Solution()
        nums = [6,10,0,6,5,8,7,4,2,7]
        rNums = s.insertionSort(nums)
        erNums = [0,2,4,5,6,6,7,7,8,10]
        self.assertEqual(rNums,erNums)

if __name__ == '__main__':
    unittest.main()
