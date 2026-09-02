class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_map = set(nums)
        curr = 0
        for n in nums_map:
            if (n-1) not in nums_map:
                curr = n
                count = 0
                while curr in nums_map:
                    count += 1
                    curr += 1
                res = max(res,count)
        return res
        