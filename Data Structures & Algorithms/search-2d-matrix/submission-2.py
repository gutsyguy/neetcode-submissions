class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for arr in matrix:
            if (self.binarySearch(arr, target)):
                return True
        
        return False
        

    def binarySearch(self, arr, target):
        l,r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                return True