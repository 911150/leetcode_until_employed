#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List
import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
    
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     start = 0
    #     end = len(nums) - 1
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] > target:
    #             end = mid - 1
    #         else:
    #             start = mid + 1
    #     return end + 1

    

        
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert(nums = [1,3,5,6], target = 2))
    


# @lc code=end

