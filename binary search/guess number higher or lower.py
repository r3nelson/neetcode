# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # assume list is in sorted order
        nums = range(1,n +1)

        left = 1
        right = len(nums) -1
        
        while left <= right:
            mid = (left + right)/2
            if guess(nums[mid]) == -1:
                left = mid + 1
            elif guess(nums[mid]) == 1:
                right = mid -1
            else:
                return mid