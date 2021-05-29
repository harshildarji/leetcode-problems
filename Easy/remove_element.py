class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occ = nums.count(val)
        to_ret = len(nums) - occ
        for i in range(occ):
            nums.pop(nums.index(val))
        return to_ret
