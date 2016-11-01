# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

'''
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
        """
        carry = 0
        rl = ListNode(None)
        while True:
            if ((l1.val + l2.val + carry)/10 > 0):
                rlval = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) / 10
            else:
                rlval = (l1.val + l2.val + carry) % 10
                carry = 0
            if rl.val == None:
                rl.val = rlval
            else:
                crl = rl
                while True:
                    if crl.next == None:
                        crl.next = ListNode(rlval)
                        break
                    crl = crl.next

            if (l1.next == None and l2.next == None):
                if carry != 0:
                    fcrl = rl
                    while True:
                        if fcrl.next == None:
                            fcrl.next = ListNode(carry)
                            break
                        fcrl = fcrl.next
                    break
                else:
                    break
            else:
                if l1.next != None:
                    l1 = l1.next
                else:
                    l1 = ListNode(0)
                if l2.next != None:
                    l2 = l2.next
                else:
                    l2 = ListNode(0)
        return rl





# def main():
#     l1 = ListNode(5)
#     # l1.next = ListNode(4)
#     # l1.next.next = ListNode(3)
#     l2 = ListNode(5)
#     l2.next = ListNode(6)
#     # l2.next.next = ListNode(4)
#
#     rl = Solution().addTwoNumbers(l1,l2)
#     print rl.val
#     print rl.next.val
#     # print rl.next.next.val
#
#
# if __name__ == '__main__':
#     main()