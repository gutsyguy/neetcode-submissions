class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        heap = []

        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        