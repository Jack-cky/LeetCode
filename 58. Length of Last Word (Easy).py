class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        pointer = len(s) - 1
        while pointer >= 0 and s[pointer] == ' ':
            pointer -= 1
        while pointer >= 0 and s[pointer] != ' ':
            result += 1
            pointer -= 1
        return result
        '''
        # alternative: cheating
        if len(s.split()) > 0:
            return len(s.split()[-1])
        else:
            return 0
        '''