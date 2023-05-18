#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
# from typing import List
import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for duplicate numbers columnwise, rowwise, in da square
        b = np.array(board)
        
        for row in b:
            crow = [x for x in row if x.isnumeric()] # rem useless...
            # print(set(crow), crow)
            if len(set(crow)) < len(crow):
                return False

        for row in b.transpose():
            crow = [x for x in row if x.isnumeric()] # rem useless...
            # print(set(crow), crow)
            if len(set(crow)) < len(crow):
                return False
            
        # outer iterator ting # break matrix down into smaller tings
        for i in range(0, 3):
            for j in range(0, 3):
                mat = []
                for ii in range(i*3,(i+1)*3):
                    for jj in range(j*3,(j+1)*3):
                        mat.append(board[ii][jj])
                
                cmat = [x for x in mat if x.isnumeric()]
                if len(set(cmat)) < len(cmat):
                    return False
                # print(mat, '\n')
                        
        return True

# if __name__ == '__main__': 
#     s = Solution()
#     print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))
#     print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))

# @lc code=end

