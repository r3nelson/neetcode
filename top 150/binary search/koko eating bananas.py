import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # return min k = eatingSpeed
        # piles.sort(reverse=True)
        # piles.sort()
        l,r = 1, max(piles)
        minK = r

        # use loop to find min k
        while l<=r:
            k = (l+r)//2

            # time taken to eat all piles
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k) 
            
            if hours <= h:
                minK = min(minK, k)
                r = k - 1
            else:
                l = k + 1
        
        
        return minK
        
