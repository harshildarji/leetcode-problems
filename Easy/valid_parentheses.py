class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        paran = {"(": ")", "[": "]", "{": "}"}
        open_par = ["(", "[", "{"]
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == paran[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
