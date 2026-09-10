class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        out = []
        for num, count in count.items():
            out.append([count, num])

        out.sort()

        res = []
        while len(res) < k:
            res.append(out.pop()[1])

        return res
        
            
        