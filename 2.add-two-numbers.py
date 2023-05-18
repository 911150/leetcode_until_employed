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
        n1, val1 = None, []
        n2, val2 = None, []
        if l1 and l2:
            n1, val1 = l1, [l1.val]
            n2, val2 = l2, [l2.val]
        else: # handle edge case bullshit
            pass 
        while n1.next:
            val1.append(n1.next.val)
            n1 = n1.next
        while n2.next:
            val2.append(n2.next.val)
            n2 = n2.next
        
        
        print(int(''.join(map(str, val1))[::-1]))
        print(int(''.join(map(str, val2))[::-1]))
        fnum = int(''.join(map(str, val1))[::-1]) + int(''.join(map(str, val2))[::-1])
        sver = [int(char) for char in str(fnum)]

        prev = ListNode(val=sver[-1].val, next=None)        
        for i in range(1, len(sver)-1):
            curr = ListNode(val=sver[i].val, next=prev)

        print(val1)
        print(val2)





# if __name__ == '__main__': 
#     s = Solution()
#     print(s.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
#     print(s.addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))


# @lc code=end

