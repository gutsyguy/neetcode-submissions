class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dist = ((x * x) + (y * y)) ** 0.5
            heapq.heappush(heap, [dist, (x, y)])

        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res


        