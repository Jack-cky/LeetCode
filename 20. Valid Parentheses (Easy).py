class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {'(':')', '[':']', '{':'}'}
        for value in s:
            if value in table:
                stack.append(value)
                continue
            if (len(stack) == 0) or (value != table[stack.pop()]):
                return False
        return stack == []