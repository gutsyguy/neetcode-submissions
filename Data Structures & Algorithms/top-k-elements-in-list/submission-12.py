class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num,0)

        heap = []

        for key,val in freq.items():
            if len(heap) > k:
                heapq.heappop(heap)
            heapq.heappush(heap, (val, key))

        print(heap)
        
        res = []
        for i in range(k):
            res.append(heap.pop()[1])

        return res