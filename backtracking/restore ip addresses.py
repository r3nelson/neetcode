from typing import Optional, List

class Solution:

  # invalid conditions
        # > 255
        # leading 0s
        # len > 12
        # len < 4
        # more than 3 digits before a dot.
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return 
        res = []

        def backtrack(curIP: str, dots: int, i: int):
            # if not self.isValid(curIP):
            #     return
            if dots > 4:
                return
            if dots == 4 and i == len(s):
                return res.append(curIP[:-1])


            for j in range(i, min(i + 3, len(s))):
                if len(s[i:j + 1]) > 1 and s[i] == '0':
                    continue
                if int(s[i:j + 1]) > 255:
                    continue
                
                backtrack(curIP + s[i:j + 1] + '.', dots + 1, j + 1)
            
        backtrack("", 0,0 )

        return res

      
    
    



