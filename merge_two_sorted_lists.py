# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1 + list2
        sl = sorted(l, key=lambda x: x.val)
        for i in range(0,len(sl)-1):
            sl[i].next = sl[i+1]
        sl[len(sl)-1].next = None

        return sl

            