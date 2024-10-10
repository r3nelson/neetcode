from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # array of unique ints
        # don't have to use every number
        # ouput will always have at least []
        

        ## choices
        # keep same number
        # use next number
        # backtrack

        res = []
        subset = []

        def backtrack(i):
            # check if need to move before previous condition
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or sum(subset) > target:
                return

            subset.append(nums[i])
            backtrack(i)

            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return res



