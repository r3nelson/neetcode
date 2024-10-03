from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if i == j:
        #             continue
        #         print(f'{i = }')
        #         print(f'{j = }')
        #         print(f'{nums[i] + nums[j] = }')

        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        index = 0

        hash_map = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in hash_map:
                return [hash_map[diff], index ]

            hash_map[val] = index

        
x = Solution()
print(x.twoSum(nums=[2,5,5,11], target= 10))