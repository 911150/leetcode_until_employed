#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

if __name__ == '__main__':
    s = Solution()
    print(s.strStr(haystack = "sadbutsad", needle = "sad"))

# @lc code=end

