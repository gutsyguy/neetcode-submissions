class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            distance = ((x * x) + (y * y)) ** 0.5
            # print(distance)
            heapq.heappush(heap, (distance, x, y))

        
        res = []

        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            res.append((x,y))

        return res
        