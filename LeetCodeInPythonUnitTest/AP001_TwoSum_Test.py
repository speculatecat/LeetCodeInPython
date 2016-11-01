import unittest

from LeetCodeInPython.AP001_TwoSum import Solution

class MyTestCase(unittest.TestCase):
    def test_twoSum(self):
        nums = [2,7,11,15]
        target = 9
        s = Solution()
        result = s.twoSum(nums=nums,target=target)
        self.assertEqual(result, [0,1])


if __name__ == '__main__':
    unittest.main()
