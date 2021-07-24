class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = ''
        max = 0
        for i in range(len(s)):
            if s[i] in stack:
                stack = stack[stack.find(s[i]) + 1:] + s[i]
            else:
                stack += s[i]
                if len(stack) > max:
                    max = len(stack)
        return max