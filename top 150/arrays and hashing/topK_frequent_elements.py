class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        
        arr = []
        for i in counts:
           key = i
           value = counts[i]
           arr.append((value,key))
        
        arr.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(arr[i][1])
        
        return res


