#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start

# from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ma = 0

        while l < r:
            # area defined by minimum height of line * dist between lines
            a = min(height[l], height[r]) * (r - l)
            ma = max(ma, a)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ma




        
# @lc code=end

