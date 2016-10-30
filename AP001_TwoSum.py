# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


'''

Given an array of integers,
return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index_1st in range(len(nums) - 1):
            for index_2nd in range(index_1st+1,len(nums)):
                if (nums[index_1st] + nums[index_2nd]) == target:
                    return [index_1st,index_2nd]

s = Solution()
print s.twoSum(nums = [2,7,11,15],target=9)
