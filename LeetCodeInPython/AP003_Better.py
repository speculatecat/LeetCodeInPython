# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == "":
            return 0

        sv = []
        slen = len(s)
        slenMax = 0
        for i in range(slen):
            sv.append([])
            stemp = ''
            for j in range(i):
                sv[i].append(0)
            for k in range(i,slen):
                if not (s[k] in stemp):
                    stemp += s[k]
                    sv[i].append(1)
                else:
                    break
            for l in range(k,slen):
                sv[i].append(0)
            if sum(sv[i]) > slenMax:
                slenMax = sum(sv[i])
            if slen - i < slenMax:
                break

        return slenMax
