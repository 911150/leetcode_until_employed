#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # always start with open bracket and end with close bracket? ye

        ans = []
        def backtrack(cur, l, r):
            if len(cur) == 2 * n:
                ans.append(''.join(cur))
                return
            if l < n:
                cur.append('(')
                backtrack(cur, l+1, r)
                cur.pop()
            if r < l:
                cur.append(')')
                backtrack(cur, l, r + 1)
                cur.pop()
        backtrack([], 0, 0)
        return ans


if __name__ == '__main__': 
    s = Solution()
    print(s.generateParenthesis(n = 3))





# @lc code=end

