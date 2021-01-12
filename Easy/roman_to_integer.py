class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "-": 0,
        }
        total, i, s = 0, 0, s + "-"
        while i < len(s) - 1:
            if roman[s[i]] >= roman[s[i + 1]]:
                total += roman[s[i]]
                i += 1
            else:
                total += roman[s[i + 1]] - roman[s[i]]
                i += 2
        return total
