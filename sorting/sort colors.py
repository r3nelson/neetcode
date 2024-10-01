from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
    
        # Assuming arr only contains 0, 1 or 2
        counts = [0, 0, 0]

        # Count the quantity of each val in arr
        for n in nums:
            counts[n] += 1
        
        # Fill each bucket in the original numsay
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                
                nums[i] = n
                print(f"{nums[i] = }")
                print(f"{n = }")
                i += 1
        return nums
    
    
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         # values within a specific range

#         color_count = {i: 0 for i in range(3)}

#         for i in nums:
#             color_count[i]+= 1

#         # for i, num in enumerate(nums):
#         #     for _ in range(len(color_count)):
#         #         nums[i] = color_count[num]

#         index = 0
#         for i in range(len(color_count)):
#             for _ in range((color_count[i])):
#                 nums[index] = i
#                 index += 1

        
#         return nums
    
# print(Solution().sortColors(nums = [2,0,2,1,1,0]))