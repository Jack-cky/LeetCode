class Solution:
    def reverse(self, x: int) -> int:        
        if needle not in haystack:
            return -1
        elif len(haystack) == 0 or len(needle) == 0:
            return 0
        else:
            flag = 0
            for i in range(len(haystack)):
                #i=1
                if haystack[i] == needle[0]:
                    pointer = i
                    for j in range(len(needle)):
                        #j=0
                        if haystack[i + j] != needle[j]:
                            break
                        if j == len(needle) - 1:
                            flag = 1
                if flag == 1:
                    break
            return pointer
        '''
        # alternative: cheating
        return haystack.find(needle)

        # alternative: loop by sub-string
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
        '''