# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time Out
        # n = len(s)
        # ans = 0
        # for i in range(0,n):
        #     for j in range(i+1,n+1):
        #         if self.allUnique(s,i,j):
        #             ans = max(ans,j-i)
        # return ans
        n = len(s)
        aSet = set()
        ans = 0
        i = 0
        j = 0
        while (i < n and j < n):
            if not (s[j] in aSet):
                aSet.add(s[j])
                j += 1
                ans = max(ans,j-i)
            else:
                aSet.remove(s[i])
                i += 1
        return ans

    def allUnique(self,s,start,end):
        """
        :param s: str
        :param start: int
        :param end: int
        :return: bool
        """
        aSet = set()
        for i in range(start,end):
            ch = s[i]
            if ch in aSet:
                return False
            else:
                aSet.add(ch)
        return True
