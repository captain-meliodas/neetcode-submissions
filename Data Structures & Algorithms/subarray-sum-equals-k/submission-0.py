class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}
        curr_sum = 0
        res = 0
        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curr_sum] = prefixSums.get(curr_sum, 0) + 1

        return res
