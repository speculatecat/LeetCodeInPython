import unittest
from  LeetCodeInPython.AP003_LongestSubstringWithoutRepeatingCharacters import Solution


class MyTestCase(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):

        solution = Solution()
        s1 = 'abcabcbb'
        result1 = solution.lengthOfLongestSubstring(s1)
        eSubString = 'abc'
        elength = 3
        self.assertEqual(result1[0], eSubString)
        self.assertEqual(result1[1],elength)
        s2 = 'bbbbb'
        result2 = solution.lengthOfLongestSubstring(s2)
        eSubString2 = 'b'
        elength2 = 1
        self.assertEqual(result2[0],eSubString2)
        self.assertEqual(result2[1],elength2)
        s3 = 'pwwkew'
        result3 = solution.lengthOfLongestSubstring(s3)
        eSubString3 = 'wke'
        elength3 = 3
        self.assertEqual(result3[0], eSubString3)
        self.assertEqual(result3[1], elength3)
        s4 = 'dvdf'
        result4 = solution.lengthOfLongestSubstring(s4)
        eSubString4 = 'vdf'
        elength4 = 3
        self.assertEqual(result4[0], eSubString4)
        self.assertEqual(result4[1], elength4)
        s5 = 'anviaj'
        result5 = solution.lengthOfLongestSubstring(s5)
        eSubString5 = 'nviaj'
        elength5 = 5
        self.assertEqual(result5[0], eSubString5)
        self.assertEqual(result5[1], elength5)
        s6 = 'nfpdmpi'
        result6 = solution.lengthOfLongestSubstring(s6)
        eSubString6 = 'nfpdm'
        elength6 = 5
        self.assertEqual(result6[0], eSubString6)
        self.assertEqual(result6[1], elength6)
        s7 = 'bpoiexpqhmebhhu'
        result7 = solution.lengthOfLongestSubstring(s7)
        eSubString7 = 'xpqhmeb'
        elength7 = 8
        self.assertEqual(result7[0], eSubString7)
        self.assertEqual(result7[1], elength7)


if __name__ == '__main__':
    unittest.main()
