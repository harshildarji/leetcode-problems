class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        pair = [strs[0][0:i] for i in range(len(strs[0]) + 1)]
        for i, p in enumerate(pair):
            if not all(s.startswith(p) for s in strs):
                return pair[i - 1]
        return p
