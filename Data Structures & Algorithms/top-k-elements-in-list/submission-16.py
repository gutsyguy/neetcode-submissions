class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))

        res = []

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res