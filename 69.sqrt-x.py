#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    from math import floor, sqrt
    
    # cheating??
    # def mySqrt(self, x: int) -> int:
    #     return self.floor(self.sqrt(x))
    
    # actual
    def mySqrt(self, x: int) -> int:
        upper_limit = x // 2
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        track = 1
        for y in range(1, upper_limit+1):
            if y * y <= x:
                track = y
            else:
                break
        return track
        

if __name__ == '__main__': 
    s = Solution()
    s.mySqrt(1)

# @lc code=end

