class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Loop through the array and find the amount of times each element appears using a hashmap
        2. Loop through the values of the hashmap to find the kth highest ones.
        3. return the values
        """
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        res = []
        for num, cnt in count.items():
            res.append([cnt, num])
        res.sort()

        out = []
        while len(out) < k:
            out.append(res.pop()[1])
        return out
