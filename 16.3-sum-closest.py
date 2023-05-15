#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # find three integers in nums such that the sum is closest to the the target
        
        # slow solution
        from itertools import combinations
        subsets = list(combinations(nums, 3))
        csum = 9999999999
        c = None
        for s in subsets:
            if (r:= abs(sum(s) - target)) < csum:
                csum = r
                c = s
        return sum(c)
    
        # fast solution -> sort the nums first -> then:
        # if we are lower increment, if higher, decrement or some shit
    

if __name__ == '__main__': 
    s = Solution()
    print(s.threeSumClosest(nums = [-1,2,1,-4], target = 1))

# @lc code=end

