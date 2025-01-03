class Solution:
    def longestValidParentheses(self, s: str) -> int:
        array = [-1]
        length = 0
        for i, c in enumerate(s):
            if c == '(':
                array.append(i)
            else:
                array.pop()
                if not array:
                    array.append(i)
                else:
                    length = max(length, i - array[-1])
        
        return length
                