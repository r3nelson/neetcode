class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        subset = set()
        l = 0
        maxL = 0

        for r in range(len(s)):
            while s[r] in subset:
                subset.remove(s[l])
                l+= 1
            subset.add(s[r])
            maxL= max(maxL, len(subset))
        
        return maxL
