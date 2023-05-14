#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

from typing import List

# @lc code=start
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     d = dict(int)
    #     s = list(set(nums)) * 2
    #     for c in nums:
    #         if c in s: s.remove(c) # n^2 time complexity is lame
    #     return s[0]
    # import collections
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     from collections import defaultdict
    #     d = defaultdict(int)
    #     for c in nums:
    #         d[c] += 1
    #     # print(d)
    #     for k, v in d.items():
    #         if v == 1:
    #             return k
            
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums) # the additive property !!

# if __name__ == '__main__': 
#     s = Solution()
#     print(s.singleNumber([4,1,2,1,2]))


# @lc code=end

