class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = len(temperatures) * [0]

        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t,i = stack.pop()
                days = index - i
                res[i] = days
        
            # add (temp, index) to stack
            stack.append((temp,index))

        return res

        
        