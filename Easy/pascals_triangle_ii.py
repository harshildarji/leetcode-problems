class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        if rowIndex == 1:
            return [[1]][-1]
        out = [[1]]
        for i in range(rowIndex - 1):
            l = [1, 1]
            for i in range(1, len(out[-1])):
                l.insert(i, out[-1][i] + out[-1][i - 1])
            out.append(l)
        return out[-1]
