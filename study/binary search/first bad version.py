# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1, n + 1

        while l <= r:
            mid = (l+r)//2
            isBad = isBadVersion(mid)

            if isBad:
                r = mid
            else:
                l = mid + 1
        
            if l == r and isBad:
                return l
