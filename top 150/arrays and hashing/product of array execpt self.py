class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        nonZeroProduct = 1
        hasZeros = False
        zeroCounter = 0

        for i in range(len(nums)):
            product *= nums[i]

            if nums[i] == 0:
                hasZeros = True
                zeroCounter += 1
                continue

            nonZeroProduct *= nums[i]            

        if zeroCounter > 1:
            return [0] * len(nums)
      
        for i in range(len(nums)):
            if not hasZeros:
                output.append(product//nums[i])
            else:
                if nums[i] == 0:
                    output.append(nonZeroProduct)
                else:
                    output.append(0)

        return output