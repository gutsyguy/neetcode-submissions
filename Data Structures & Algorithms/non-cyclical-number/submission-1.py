class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()


        while True:
            n_sum = 0

            for num in str(n):
                n_sum += int(num) * int(num)

            if n_sum == 1:
                return True
            elif n_sum in seen:
                return False
            else:
                seen.add(n_sum)

            n = n_sum
        