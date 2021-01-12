class Solution:
    def reverse(self, x: int) -> int:
        ans = -(int(str(abs(x))[::-1])) if x < 0 else (int(str(abs(x))[::-1]))
        return 0 if abs(ans) >> 31 else ans
