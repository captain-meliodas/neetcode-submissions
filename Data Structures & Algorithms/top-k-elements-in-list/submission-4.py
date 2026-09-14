from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """{freq:num} {1:[1,2], 3:[3]} k=2 => 3,2 from collection import Counter most_common(k)"""

        res = Counter(nums)
        output = []
        for i in res.most_common(k):
            output.append(i[0])
        
        return output
        