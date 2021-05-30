class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        for i in range(len(s)):
            if s[i] in s[:i]:
                start = max(start, s[:i].rfind(s[i]) + 1)
            max_length = max(max_length, i + 1 - start)
        return max_length
