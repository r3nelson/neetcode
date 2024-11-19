class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in hashSet:
                j = 1
                while nums[i] + j in hashSet:
                    j+=1
                longest = max(longest, j)
        
        return longest
        