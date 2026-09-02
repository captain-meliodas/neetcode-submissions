class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        _map ={}
        for i in nums:
            if _map.get(i):
                _map[i] += 1
                result = True
                break
            else:
                _map[i] = 1
        
        return result
        