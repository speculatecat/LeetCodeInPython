# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example:
e1
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

e2
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

# TD Pass but Time out.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)

        sortNums = self.insertionSort(nums)
        length = len(sortNums)
        if length%2 != 0:
            return float(sortNums[length/2])
        else:
            r_nums1 = sortNums[length/2]
            r_nums2 = sortNums[(length/2) - 1]
            return float(float(r_nums1+r_nums2)/2)


    def insertionSort(self,nums):
        length = len(nums)
        for outer in range(1,length):
            temp = nums[outer]
            inner = outer
            while inner > 0 and nums[inner - 1] >= temp:
                nums[inner] = nums[inner -1]
                inner = inner - 1
            nums[inner] = temp
        return nums