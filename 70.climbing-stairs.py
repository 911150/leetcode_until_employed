#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        s,l = 1 , 2
        for _ in range(2, n): 
            # swapping `s` and `l`
            s, l = l, s + l 
        return l if n > 1 else s

   
        
# @lc code=end

