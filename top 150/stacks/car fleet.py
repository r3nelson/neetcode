class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        if len(speed) == 1:
            return 1


        stack = []
        pairs = [[p,s] for p,s in zip(position,speed)]
        
        for p,s in sorted(pairs)[::-1]:
            if stack:
                oldP, oldS = stack[-1]
                oldTime = (target - oldP) / oldS
                time = (target - p) /s
                # will become a car fleet
                if time <= oldTime:
                    continue
                 
            stack.append([p,s])

        return len(stack)



        
