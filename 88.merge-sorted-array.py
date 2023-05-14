#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

from typing import List

# @lc code=start

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if m == 0:
        #     nums1[0] = nums2[-1]


        # that doesnt work
        t = m + n - 1
        i = m - 1
        j = n - 1
        # nums1 has length m
        # while i >= 0 or j >= 0:
        while j >= 0:
            print(t, i, j)
            if i >= 0 and nums1[i] >= nums2[j]:
                # got tripped up by checking if the entire i array had been consumed
                nums1[t] = nums1[i]
                # increment; i,t leave j
                i -= 1
            else:
                nums1[t] = nums2[j]
                # increment; j,t leave i
                j -= 1
            t -= 1
        print(nums1)

    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     for i in range(m,m+n):
    #         nums1[i]=nums2[i-m]
    #     nums1.sort()
           
# if __name__ == '__main__': 
#     s = Solution()
#     s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
#     s.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
#     s.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)



# @lc code=end

