#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
# from typing import List
# import itertools
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking approach with dfs
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return # backtracking here apparently
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            # print(nums, target-nums[i], i, path + [nums[i]], res)
            self.dfs(nums, target-nums[i], i, path + [nums[i]], res)


# if __name__ == '__main__':
#     s = Solution()
#     print('nums', 'target', 'index', 'path', 'res')
#     print(s.combinationSum(candidates = [2,3,6,7], target = 7))

#     pass

        
# @lc code=end


