#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if empty string return none
        if not s:
            return ''

        if len(s) == 1:
            return s[0]

        longest = ''

        for i in range(0, len(s)): # move forward
            for j in range(i+1, len(s)+1): # slide along
                curr = s[i:j]
                # print(i, j, curr)
                if curr == curr[::-1]:
                    if len(curr) > len(longest):
                        longest = curr
        return longest
        

# if __name__ == '__main__': 
#     s = Solution()
#     # print(s.longestPalindrome(s = "babad"))
#     # print(s.longestPalindrome(s = "cbbd"))
#     print(s.longestPalindrome(s = "bb"))
# @lc code=end

