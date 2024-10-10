from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ## constraints
        # 1<= n<= 8
        # can't start with close
        # OpenCount >= closeCount at all times

        ## choices
        # open
        # close
        
        res = []
        stack =[]

        def backtrack(openCount, closeCount):
            if openCount == closeCount == n:
                print(stack)
                res.append(''.join(stack))

            if closeCount > openCount:
                return

            # add open
            if openCount < n:
                stack.append('(')
                backtrack(openCount + 1,closeCount)
                stack.pop()

            # add close
            if closeCount < openCount:
                stack.append(')')
                backtrack(openCount,closeCount +1)
                stack.pop()
        
        backtrack(0,0)
        return res

            

