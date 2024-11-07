from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        l,r = 1, piles[-1]
        min_speed = r
        
        while l<=r:

            # speed = k
            speed = (l+r) // 2
            hours = 0

            # can eat in time
            for num in piles:
                hours += math.ceil(num/speed) 
            
            if hours <= h:
                min_speed = min(min_speed, speed)
                r = speed -1
            else:
                l = speed + 1

        return min_speed
            

        

            
print(Solution().minEatingSpeed(piles = [25,10,23,4], h = 4))

