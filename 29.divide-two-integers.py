#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res, i = 0, 0

        if dividend > 2147483647:
            return 2147483647
        if dividend < -2147483647:
            return -2147483647



        while res <= abs(dividend):
            res += abs(divisor)
            i += 1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return i-1
        else:
            return -(i-1)

# if __name__ == '__main__': 
#     s = Solution()
#     print(s.divide(dividend = 10, divisor = 3))

# @lc code=end

