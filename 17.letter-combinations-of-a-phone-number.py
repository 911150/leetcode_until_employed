#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        s = 'abcdefghijklmnopqrstuvwxyz'
        d = {i+1 : s[(i-1)*3:(i)*3] for i in range(1,6)}
        d[7] = 'pqrs'
        d[8] = 'tuv'
        d[9] = 'wxyz'
        # print(d)
        p = itertools.product(*[list(d[int(i)]) for i in digits])
        return [''.join(o) for o in list(p)]
        # return arr

# if __name__ == '__main__': 
#     s = Solution()
#     print(s.letterCombinations('23'))


# @lc code=end

