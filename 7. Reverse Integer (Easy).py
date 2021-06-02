class Solution:
    def reverse(self, x: int) -> int:        
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = -x
            x = int('-' + str(x)[::-1])
        if (x <= 2 ** 31 - 1) & (x >= -2 ** 31):
            return x
        else:
            return 0
        '''
        # alternative
        result = flag = 0
        if x < 0:
            x = -x
            flag = 1
        while x != 0:
            signfi = x % 10
            x = x // 10
            result = result * 10 + signfi
            if result > 2 ** 31 - 1:
                return 0
        if flag == 1:
            result = -result
        return result
        '''