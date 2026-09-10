class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
            Understand:
                - Implement the power mathematical function
                    - Pow(x,n) => x^n
                - Cannot use built-in library functions
                - N is an integer but can be negative 
                - If x = 0 then n is positive

            Plan:
                - Incrementally multiply x by itself n times
                - If n is negative, turn it into a positive and then divide
                at the end.
        """

        total = 1
        multiplier = n 

        if n == 0:
            return 1

        if n < 0:
            multiplier = -n

        for i in range(multiplier):
            total *= x

        if n < 0:
            return 1/total
        else:
            return total

        