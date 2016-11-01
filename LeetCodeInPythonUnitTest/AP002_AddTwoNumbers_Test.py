import unittest

from LeetCodeInPython.AP002_AddTwoNumbers import ListNode,Solution

class MyTestCase(unittest.TestCase):
    def test_addTwoNumbers(self):
        s = Solution()
        l1 = ListNode(0)
        l1.next = ListNode(1)
        l2 = ListNode(0)
        l2.next = ListNode(1)
        l2.next.next = ListNode(2)
        erl = ListNode(0)
        erl.next = ListNode(2)
        erl.next.next = ListNode(2)
        rl = s.addTwoNumbers(l1,l2)
        while True:
            if rl.next != None:
                self.assertEqual(rl.val, erl.val)
                rl = rl.next
                erl = erl.next
            else:
                self.assertEqual(rl.val, erl.val)
                break


if __name__ == '__main__':
    unittest.main()
