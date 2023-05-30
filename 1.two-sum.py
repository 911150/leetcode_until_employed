#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}  # use a set instead?
        for i in range(len(nums)):
            if (s:=target - nums[i]) in hasmap.keys(): return [i, hasmap[s]]
            hasmap[nums[i]] = i
    

# @lc code=end

