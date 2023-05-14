#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

import math

# @lc code=start
# from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(log(m + n))
        nums = sorted(nums1 + nums2)
        l = len(nums)
        if l % 2 != 0:
            return nums[int(l/2)]
        else:
            return (nums[l//2] + nums[(l//2-1)]) / 2

# if __name__ == '__main__': 
#     s = Solution()
#     s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])


# @lc code=end

