#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums) == nums:
            return nums

        # if len(nums) > 2:

        if nums[-1] == min(nums):
            




        pass
        



        
# @lc code=end

