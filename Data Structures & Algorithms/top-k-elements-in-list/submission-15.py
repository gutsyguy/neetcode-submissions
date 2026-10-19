class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        heap = []

        for key, val in counter.items():
            heapq.heappush(heap, [-val, key])

        res = []
        while k > 0:
            freq, num = heapq.heappop(heap)
            res.append(num)
            k -= 1

        return res
        