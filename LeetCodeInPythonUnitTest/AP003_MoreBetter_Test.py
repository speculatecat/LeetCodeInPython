import unittest

from LeetCodeInPython.AP003_MoreBetter import Solution

class MyTestCase(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        s = Solution()
        s1 = 'abcabcbb'
        r1 = s.lengthOfLongestSubstring(s1)
        elen1 = 3
        self.assertEqual(r1, elen1)
        s2 = 'bbbbb'
        r2 = s.lengthOfLongestSubstring(s2)
        elen2 = 1
        self.assertEqual(r2, elen2)
        s3 = 'pwwkew'
        r3 = s.lengthOfLongestSubstring(s3)
        elen3 = 3
        self.assertEqual(r3, elen3)
        s4 = 'dvdf'
        r4 = s.lengthOfLongestSubstring(s4)
        elen4 = 3
        self.assertEqual(r4, elen4)
        s5 = 'anviaj'
        r5 = s.lengthOfLongestSubstring(s5)
        elen5 = 5
        self.assertEqual(r5, elen5)
        s6 = 'nfpdmpi'
        r6 = s.lengthOfLongestSubstring(s6)
        elen6 = 5
        self.assertEqual(r6, elen6)
        s7 = 'bpoiexpqhmebhhu'
        r7 = s.lengthOfLongestSubstring(s7)
        elen7 = 8
        self.assertEqual(r7, elen7)
        s8 = ""
        r8 = s.lengthOfLongestSubstring(s8)
        elen8 = 0

    def test_allUnique(self):
        s = Solution()
        str = 'abcabcbb'
        r1 = s.allUnique(str,0,3)
        er1 = True
        self.assertEqual(r1,er1)
        r2 = s.allUnique(str,0,4)
        er2 = False
        self.assertEqual(r2,er2)



if __name__ == '__main__':
    unittest.main()
