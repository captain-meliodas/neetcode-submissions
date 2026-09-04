import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = 1
        max_rate_under_h = max(piles)
        res = max_rate_under_h
        while min_rate<=max_rate_under_h:
            total_hours = 0
            k = (min_rate+max_rate_under_h)//2
            for p in piles:
                total_hours += math.ceil(p/k)
            
            if total_hours <= h:
                res = k
                max_rate_under_h = k-1
            else:
                min_rate = k+1
        
        return res