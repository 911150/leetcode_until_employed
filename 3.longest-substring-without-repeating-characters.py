#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        m = 1

        for i in range(len(s)):
            c = 1
            for j in range(i+1, len(s)):
                #  makes all substrings
                if s[j] in s[i:j]: #  
                    if j-i > m:
                        m = j-i
                    break
                c += 1
            if c > m:
                m = c
        return m

# if __name__ == '__main__': 
#     q = Solution()
#     print(q.lengthOfLongestSubstring("abcabcbb"))
#     print(q.lengthOfLongestSubstring("bbbbb"))
#     print(q.lengthOfLongestSubstring("pwwkew"))



# @lc code=end

