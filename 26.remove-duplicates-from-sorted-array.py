#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

from typing import List

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        j = 0
        for i in range(0, len(nums)):
            print(nums[i])
            print(s)
            if nums[i] in s:
                continue
            else:
                s.add(nums[i])
                nums[j] = nums[i]
                j += 1
                continue
        # return nums[0:j]
        return j
        

# if __name__ == '__main__':
#     s = Solution()
#     print(s.removeDuplicates([1,1,2]))
# @lc code=end

