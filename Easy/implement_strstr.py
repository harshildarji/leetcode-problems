class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle.split()) == 0:
            return 0
        else:
            try:
                return haystack.index(needle)
            except:
                return -1
