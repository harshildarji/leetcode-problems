class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 2, 1
        for x in range(2, n):
            c = a + b
            b, a = a, c
        return c
