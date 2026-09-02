class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        n = len(nums)
        res = []
        for i in range(n):
            curr = target - nums[i]
            if curr in nums_map:
                res = [nums_map[curr],i]
                break
            
            nums_map[nums[i]] = i
        return res