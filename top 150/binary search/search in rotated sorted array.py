class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l<r: 
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        minIndex = l

        # target can't be less than our minimum
        if nums[minIndex] > target:
            print('condition')
            return -1

        # determine bounds 
        print(minIndex)
        if minIndex == 0:
            l,r = 0,len(nums) -1
        elif nums[minIndex] <= target and target <= nums[len(nums) -1]:
            l,r = minIndex, len(nums) - 1
        else:
            l,r = 0, minIndex - 1

        print(l,r)

        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1




      