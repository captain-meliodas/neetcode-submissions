class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        _map ={}
        for i in nums:
            _map[i] = _map.get(i,0)+1
            if _map[i] > 1:
                result = True
                break
        
        return result
        