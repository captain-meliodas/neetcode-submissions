from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        n = len(nums)
        res = []
        l=0
        for r in range(n):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            
            dq.append(r)

            if dq[0] < l:
                dq.popleft()
            
            if r >= k-1:
                res.append(nums[dq[0]])
                l += 1

        return res
        