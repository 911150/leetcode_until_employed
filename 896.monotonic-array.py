#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
# from numpy import all, diff
# import numpy as np

# Your runtime beats 72.97 % of python3 submissions

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            elif nums[i] < nums[i-1]:
                increasing = False
        return increasing or decreasing
        # return np.all(np.diff(nums) >= 0) or np.all(np.diff(nums) <= 0)
            
            
# @lc code=end

