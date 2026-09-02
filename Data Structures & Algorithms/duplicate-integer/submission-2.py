class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        res = False
        for i in nums:
            if num_map.get(i):
                if num_map[i]+1 > 1:
                    res = True
                    break
            num_map[i] = num_map.get(i,0)+1
        
        return res

        