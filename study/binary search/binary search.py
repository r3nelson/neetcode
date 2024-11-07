from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start,end = 0, len(nums) -1

        while start <= end:
            mid = (start + end) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid -1
        
        return -1
        

        
x = Solution()
print(x.search(nums =[-1,0,2,4,6,8], target = 6 ))
print(x.search(nums =[-1,0,2,4,6,8], target = 3 ))