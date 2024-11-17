class Solution:
    def trap(self, height: List[int]) -> int:    
        # min(maxL, maxR) - height[i] 

        ## two approaches

        # use two pointers
        l,r = 0, len(height) - 1
        res = 0
        
        maxL, maxR = height[l], height[r]

        while l<r:
            # val = min(maxL, maxR) - height[i] 
            if maxL <= maxR:
                val = maxL - height[l] 
                l+= 1
                maxL = max(maxL, height[l])
                res += max(val, 0)
            else:
                val = maxR - height[r] 
                r-= 1
                maxR = max(maxR, height[r])
                res += max(val, 0)

        return res
                
        # make maxL and maxR arrays
        # maxL, maxR = 0,0
        # arrMaxL, arrMaxR = [], []
        # res= 0

        # for i in range(len(height)):
        #     arrMaxL.append(maxL)
        #     arrMaxR.append(maxR)
        #     maxL = max(maxL, height[i])
        #     maxR = max(maxR, height[len(height) - 1 - i])

        # arrMaxR = arrMaxR[::-1]
                                
        # for i in range(len(height)):
        #     val = min(arrMaxL[i], arrMaxR[i]) - height[i]
        #     res += max(val, 0)
        
        # return res

      


