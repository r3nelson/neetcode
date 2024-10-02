class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        nums = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3":3,
            "4":4,
            "5": 5,
            "6": 6,
            "7":7,
            "8":8,
            "9": 9
        }

        # edge cases
        if num1 == "0" or num2 == "0":
            return "0"

        res = 0
        num2_index = 1
        for i in num1[::-1]: #123 -> 321
            num1_index = 1

            for j in num2[::-1]: #456 -> 654
                res += (nums[i] * num1_index ) * (nums[j]* num2_index)
                num1_index *= 10
            num2_index *= 10

        return str(res)
            
