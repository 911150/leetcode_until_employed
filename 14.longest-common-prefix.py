#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


from typing import List

# @lc code=start
class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     # sort an array of strings        
    #     shortest_prefix = min(len(s) for s in strs)
    #     print(shortest_prefix)
    #     # first letters for all words
    #     running = True
    #     i = 0
    #     l = []
    #     while running and i < shortest_prefix:
    #         c = None
    #         cont = True
    #         for s in strs:
    #             if c is None:
    #                 c = s[i]
    #                 continue
    #             elif s[i] == c:
    #                 continue
    #             else:
    #                 cont = False
            
    #         if cont == False:
    #             return ''.join(l)
    #         else:
    #             l.append(c)
    #             i += 1
        
    #     return ''

    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        s = sorted(strs)
        first = s[0]
        last = s[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            else:
                ans += first[i]
        return ans

    # def longestCommonPrefixFirst(self, strs: List[str]) -> str:
    #     # first get the shortest string
    #     ss = min(strs, key=len)
    #     cont = True
    #     i = 0
    #     l = ''
    #     while i < len(ss):
    #         all_same = all(ss[i] == s[i] for s in strs)
    #         if all_same:
    #             l = l + ss[i]
    #             i += 1
    #         else:
    #             return l
        
    #     return l



if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['a']))


# @lc code=end

