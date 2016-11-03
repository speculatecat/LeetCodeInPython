# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        subStringArr = []
        sIndex = 0
        subStringArr.append([])
        for letter in s:
            if not (letter in subStringArr[sIndex]):

                subStringArr[sIndex].append(letter)
            else:
                sIndex = sIndex + 1
                subStringArr.append([])
                subStringArr[sIndex].append(letter)

        # first filter result
        fftargetIndex = 0
        fflength = 0
        ffsubString = ''
        for index in range(len(subStringArr)):
            if len(subStringArr[index]) > fflength:
                fflength = len(subStringArr[index])
                fftargetIndex = index
        for s in subStringArr[fftargetIndex]:
            ffsubString += s

        if len(subStringArr) > 0:
            for i in range(1,len(subStringArr)):
                while True:
                    if not(subStringArr[i - 1][-1:][0] in subStringArr[i]) and len(subStringArr[i]) > 1:
                        tempStringArr = subStringArr[i - 1][-1:]
                        tempStringArr.extend(subStringArr[i])
                        subStringArr[i] = tempStringArr
                        tempStringArr = []
                        subStringArr[i - 1].remove(subStringArr[i - 1][-1:][0])
                    else:
                        break

        targetIndex = 0
        length = 0
        subString = ''
        for index in range(len(subStringArr)):
            if len(subStringArr[index]) > length:
                length = len(subStringArr[index])
                targetIndex = index
        for s in subStringArr[targetIndex]:
            subString += s

        if fflength > length:
            return (ffsubString,fflength)
        else:
            return (subString,length)



