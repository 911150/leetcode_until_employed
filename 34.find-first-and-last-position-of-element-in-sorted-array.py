#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     start = None
    #     for i, num in enumerate(nums):
    #         if num == target:
    #             start = i
    #         else:
    #             continue
    #         while i+1 < len(nums):
    #             if nums[i] == target:
    #                 i += 1
    #             else:
    #                 return [start, i-1]
    #     if start:
    #         return [start, start]
    #     return [-1, -1]
        
    # nums.index(target)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            if target in nums:
                return [0,0]
            else:
                return [-1,-1]
        try:
            s = nums.index(target)
        except ValueError:
            return [-1,-1]
        i = s
        while i < len(nums):
            if nums[i] == target:
                i += 1
            else:
                return [s, i-1]        
        return [s, i] if s else [-1,-1]

# if __name__ == '__main__': 
#     s = Solution()
#     print(s.searchRange([5,7,7,8,8,10], target = 6))
#     print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))



# @lc code=end

