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

            Initial Implementation:
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
            Evaluation:
                - Time: O(n)
                - Space: O(1)

            Review: I can make improve time complexity by multiplying total 
            by itself because x^4 = x^2 * x^2.

            Evalution 2:
                - Time: O(log n)
                - Space: O(1)

            Optimizations:
                - Exponential multiplication instead of linear to reduce
                time complexity to O(log n)
        """
        if n < 0:
            x = 1/x
            n = -n 

        res = 1

        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2

        return res

        