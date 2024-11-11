class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i],0) + 1
    
        for i in range(len(t)):
            num = counts.get(t[i])
            if num:
                counts[t[i]] -= 1
                if counts[t[i]] < 0: return False
            else: return False

        return True
    
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         counts = {}
#         for i in range(len(s)):
#             num = counts.get(s[i])
#             if num:
#                 counts[s[i]] += 1
#             else: counts[s[i]] = 1
    
#         for i in range(len(t)):
#             num = counts.get(t[i])
#             print(num)
#             if num:
#                 counts[t[i]] -= 1
#                 if counts[t[i]] < 0: return False
#             else: return False

#         return True
