#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index, sell_index, profit = None, None, 0
        
        # as you move along prices via i
        max, min = 0, prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min :
                min = prices[i]
            elif((prices[i] - min) > max):
                max = prices[i] - min
        return max        


# if __name__ == '__main__': 
#     s = Solution()
#     # print(s.maxProfit([7,1,5,3,6,4]))
#     print(s.maxProfit([7,6,4,3,1])) # 0

        
# @lc code=end

