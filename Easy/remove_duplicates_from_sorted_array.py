class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_ret = len(set(nums))
        try:
            num = nums[0]
            for i in nums[1:]:
                if i == num:
                    nums.pop(nums.index(i))
                else:
                    num = i
            return to_ret
        except:
            return 0
