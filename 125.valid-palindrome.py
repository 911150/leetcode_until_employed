#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     cs = ''.join([c for c in s if c.isalnum() == True]).lower() # clean the string
    #     l = len(cs)
    #     for i in range(0, l // 2):
    #         if cs[i] != cs[l-i-1]:
    #             return False
    #     return True
    
    # FASTER @ 30.4 %
    def isPalindrome(self, s: str) -> bool:
        # fast clean the string
        import string
        cs = s.translate(str.maketrans('', '', string.punctuation + ' ')).lower()
        # cs = ''.join([c for c in s if c.isalnum() == True]).lower() # slow clean
        mid = len(cs) // 2
        b = 0 if len(cs) % 2 == 0 else 1
        # print(cs[:mid], len(cs[:mid]))
        # print(cs[mid+b:][::-1], len(cs[mid+b:]))
        if cs[:mid] == cs[mid+b:][::-1]:
            return True
        return False
    
    # SLOWER 17%
    # def isPalindrome(self, s: str) -> bool:
    #     i,j = 0, len(s)-1
    #     while i <= j:
    #         if i == j:
    #             return True
    #         ti= s[i].isalnum()
    #         tj= s[j].isalnum()
    #         if ti and tj:
    #             if s[i].lower() == s[j].lower():
    #                 # print(s[i].lower(), s[j].lower())
    #                 i += 1
    #                 j -= 1
    #             else:
    #                 # print(s[i], s[j])
    #                 return False
    #         else:
    #             i += -ti + 1
    #             j -= -tj + 1
    #     return True

# if __name__ == '__main__': 
#     s = Solution()
#     print(s.isPalindrome("A man, a plan, a canal: Panama"))
#     print(s.isPalindrome("A man, a plan, a anal: Panama"))
#     print(s.isPalindrome('0P'))

# @lc code=end

