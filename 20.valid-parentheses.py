#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    inv_map = {
            '{' : '}',
            '(' : ')',
            '[' : ']',
        }
    
    rev = {value: key for key, value in inv_map.items()}
        
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if c in self.inv_map.keys():
                l.append(c) # add c to the buffer
                continue
            elif len(l) == 0:
                return False
            else:
                if l[-1] == self.rev[c]:
                    # print(l[-1], c)
                    # found a partner
                    l.pop(-1)
                    continue
                return False

        return not l
        
# @lc code=end

