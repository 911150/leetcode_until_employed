#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
# from typing import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ceil = len(nums) // 2
        for i in range(0, len(nums)):
            d[nums[i]] += 1
            if d[nums[i]] > ceil: return nums[i]
                
# @lc code=end

