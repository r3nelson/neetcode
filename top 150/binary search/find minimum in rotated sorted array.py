class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l,r = 0, len(nums) -1

        # break when l == r
        while l < r: 
            m = (l+r)//2

            # minimum is on right
            if nums[m] > nums[r]:
                l = m + 1
            # minimum is on left
            else:
                r = m

        return nums[l] 


        

