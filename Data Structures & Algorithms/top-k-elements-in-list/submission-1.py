class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        nums
        nums_map = {}
        for num in nums:
            nums_map[num] = nums_map.get(num,0)+1

        freq = [[] for i in range(len(nums)+1)]
        for n,c in nums_map.items():
            freq[c].append(n)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
        
        