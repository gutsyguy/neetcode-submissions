class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        heap = []
        for key, value in frequency.items():
            heapq.heappush(heap, (-value, key))

        res = []

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
