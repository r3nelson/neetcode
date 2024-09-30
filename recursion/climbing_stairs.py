class Solution:
    def climbStairs(self, n: int) -> int:
        
        l,r = 1, 1

        for i in range(n):
            temp = r
            r = l + r
            l = temp
        
        return r
    
        # # recursive solution
        # if n == 1:
        #     return 1
        
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
