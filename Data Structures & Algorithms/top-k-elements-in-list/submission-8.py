class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Loop through the array and find the amount of times each element appears using a hashmap
        2. Loop through the values of the hashmap to find the kth highest ones.
        3. return the values
        """
        group = {}

        for num in nums:
            group[num] = 1 + group.get(num, 0)

        arr = []
        for num, cnt in group.items():
            arr.append([cnt,num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res