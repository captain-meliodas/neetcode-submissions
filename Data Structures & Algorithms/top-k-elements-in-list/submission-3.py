class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """{freq:num} {1:[1,2], 3:[3]} k=2 => 3,2"""

        freq = {}
        nums_map = {}
        res = []
        for n in nums:
            nums_map[n] = nums_map.get(n,0)+1
        
        freq = [[] for i in range(len(nums)+1)]
        for num,count in nums_map.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res