class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            distance = ((x*x)+(y*y))**0.5
            heapq.heappush(heap, [distance, (x,y)])

        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res