#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start

# from typing import List
    #     P
    #    A S 
    #   C A L
    #  S T R I 
    # A N G L E
    #     1
    #    1 1
    #   1 2 1
    #  1 3 3 1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:        
        l = []
        if numRows == 0:return l
        l.append([1])
        if numRows == 1:return l
        # l.append([1,1])
        # if numRows == 2:return l
        # length of the array == numRows
        for r in range(2, numRows+1):
            t = [1] # add the front padded 1
            for i in range(0, r-2):
                # print(l, i)
                t.append(l[-1][i] + l[-1][i+1])
            t.append(1) # rear pad
            # add the new row to the result array            
            l.append(t)
        return l
    
# if __name__ == '__main__': 
#     s = Solution()
#     print(s.generate(numRows = 5))
#     print(s.generate(numRows = 1))



# @lc code=end


