#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # n1 = int(''.join([str(x) for x in l1])) + int(''.join([str(x) for x in l2]))
        # return [int(c) for c in str(n1)][::-1]
        t = l1.val + l2.val
        curr1 = l1.next
        curr2 = l2.next
        rem = 0
        prev = ListNode(val=t, next=None)        

        while curr1 or curr2:
            if curr1.next is None:
                t = curr2.val
                curr2 = curr2.next
            elif curr2.next is None:
                t = curr2.val
                curr1 = curr1.next
            else:
                s = curr1.val + curr2.val + rem # absorb the remainder
                rem = 0
                if s > 9:
                    t = s % 10
                    rem += 1
                else:
                    t = s
                # print(curr1.val, curr2.val, rem, s)
            # here use t to make the list ting
            temp = ListNode(val=t, next=None)
            prev.next = temp
            prev = temp
        return prev


# if __name__ == '__main__': 
#     s = Solution()
#     print(s.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
#     print(s.addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))


# @lc code=end

