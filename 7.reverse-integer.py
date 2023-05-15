#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        num = int(''.join(list(str(abs(x)))[::-1]))
        if abs(num) > 2 ** 31: return 0
        if x < 0:
            return -num
        return num


# if __name__ == '__main__': 
#     s = Solution()
#     print(s.reverse(-1))
#     print(s.reverse(0))
#     print(s.reverse(123))
#     print(s.reverse(-321))
#     print(s.reverse(120))

# @lc code=end

