#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

from typing import List

# @lc code=start
class Solution:
    # nice one
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str(int(''.join([str(x) for x in digits])) + 1)]

    # def plusOne(self, digits: List[int]) -> List[int]:
    #     res = 0
    #     for i in range(len(digits)):
    #         res += digits[i] * 10 ** (len(digits) - i - 1)
    #     # add one to the answer
    #     res += 1
    #     return [int(c) for c in str(res)]

        
# if __name__ == '__main__': 
#     s = Solution()
#     print(s.plusOne([4,3,2,1]))

    


# @lc code=end

