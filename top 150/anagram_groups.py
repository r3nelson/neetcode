class Solution:
    def isAnagram(self, word1:str, word2:str ) -> bool:
        return ''.join(sorted(word1)) == ''.join(sorted(word2))


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}
        skip = False

        for i in range(len(strs)):
            for key in hash_map:
    
                # if anagram match add to bin
                if self.isAnagram(strs[i], key):
                    hash_map[key].append(strs[i])
                    skip = True
                    break
            
            # if no anagram match yet 
            if not skip:
                hash_map[strs[i]] = [strs[i]]
            skip = False

        result = []
        for key in hash_map:
            result.append(hash_map[key])

        return result