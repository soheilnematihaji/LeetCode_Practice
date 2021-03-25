"""
This a solution for the problem from
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Here is the copy of the problem from leetcode:

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def lc(digits):
            if not digits:
                return []
            if len(digits)==1:
                return [s for s in map_[digits]]
            result=lc(digits[1:])
            output=[]
            for i in map_[digits[0]]:
                for item in result:
                    output.append(i+item)
            return output
        return lc(digits)
        
        
