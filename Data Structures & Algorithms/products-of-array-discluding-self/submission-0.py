class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix technique

        length = len(nums)
        res = [None] * length
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i - 1]
        
        suf_mult = 1
        for j in range (length - 1, -1, -1):
            res[j] *= suf_mult
            suf_mult *= nums[j]

        return res