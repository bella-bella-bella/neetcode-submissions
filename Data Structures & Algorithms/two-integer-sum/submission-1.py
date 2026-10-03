class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ixs = dict()
        for i, n in enumerate(nums):
            dif = target - n 
            if dif in ixs:
                return [ixs[dif], i]
            ixs[n] = i