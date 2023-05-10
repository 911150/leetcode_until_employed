#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     s = str(x)
    #     l = len(s)
    #     # for i in range(0, len(s) // 2):
    #     for i in range(0, len(s) // 2):
    #         # if s[i] == s[l-i-1]:
    #         if s[i] == s[l-i-1]:
    #             continue
    #         else:
    #             return False
        
    #     return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]


# @lc code=end

