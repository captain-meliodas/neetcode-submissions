import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        speed = max_speed

        while min_speed<=max_speed:
            total_hours = 0
            curr_speed = (min_speed+max_speed)//2
            for p in piles:
                total_hours += math.ceil(p/curr_speed)
            
            if total_hours <= h:
                speed = curr_speed
                max_speed = curr_speed - 1
            
            else:
                min_speed = curr_speed + 1
        
        return speed