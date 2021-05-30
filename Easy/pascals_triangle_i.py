class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        out = [[1]]
        for i in range(numRows - 1):
            l = [1, 1]
            for i in range(1, len(out[-1])):
                l.insert(i, out[-1][i] + out[-1][i - 1])
            out.append(l)
        return out
