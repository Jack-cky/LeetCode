class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if (x == int(str(x)[::-1])) & (x <= 2 ** 31 - 1):
            return True
        else:
            return False
        '''
        # alternative
        y = str(x)
        for i in range(int(len(y) / 2)):
            if y[i] != y[len(y) - 1 - i]:
                return False
        return True
        '''