# this is not the most efficent solution. It is good but not best. It runs in O(m * log(n)) 
# I can make it run in O(log(m) + log(n)) by running binary search on the list of matrixs to see which row would contain the target

from typing import List

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) -1 

        while start <= end:
            mid = (start + end)//2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid -1 
            else:
                return True
        return None


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for lis in matrix:
            # in this row
            if target >= lis[0] and target <= lis[-1]:
                print(f'{lis[0] = }')
                print(f'{lis[-1] = }')
                print(f'{target = }')
                print(lis)
                res =  self.binarySearch(nums= lis, target= target)
                print(res)
                if res:
                    return True
        return False
    
x = Solution()
x.searchMatrix(matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]],target= 10)
                
