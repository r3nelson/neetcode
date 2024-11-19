class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False
            
        stack = []
        hash_map = {
                '}': '{',
                ']': '[',
                ')':'('
                }

        for i in range(len(s)):
            if s[i] in hash_map:
                if stack and stack[-1] == hash_map[s[i]]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(s[i])

        if stack:
            return False
        else:
            return True
    
        
        

