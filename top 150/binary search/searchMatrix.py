class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if i +1 < len(matrix):
                if matrix[i][0] <= target and target < matrix[i+1][0]:
                    # row = i
                    return self.binarySearch(matrix[i], target)
            else:
                return self.binarySearch(matrix[i], target)
        
    def binarySearch(self, nums: List[int], target: int)-> bool:

        l,r = 0, len(nums) -1
        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
       
        
                



        
