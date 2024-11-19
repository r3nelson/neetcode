class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        res = ''
        for word in strs:
            res += str(len(word)) + '~' + word
        return res
            

    def decode(self, s: str) -> List[str]:    
        res = []
        l = 0

        while l < len(s):
            j = l

            while s[j] != '~':
                j+=1
            
            num = int(s[l:j])
            word = s[j+1: j + 1 +num]
            res.append(word)

            l = j + 1 + num
        
        return res

        

            


        
