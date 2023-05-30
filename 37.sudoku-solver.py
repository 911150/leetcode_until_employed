#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # board is a board of boards...
        b = np.array(board)
        # some sort of search, row wise?? or columnwise? or square wise?

        # get the top 3x3 matrix
        i = 0
        q1 = b[i:(i+1)*3, i:(i+1)*3].flatten()
        r1 = b[i]
        c1 = b.T[i]
        
        print(q1)
        print(r1)
        print(c1)
        d = set(['1','2','3','4','5','6','7','8','9'])
        
        def is_valid_row(row):
            pass

if __name__ == '__main__': 
    s = Solution()
    b1 = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(b1)


        
# @lc code=end


