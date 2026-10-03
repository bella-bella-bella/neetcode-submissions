class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        # nums[i] + nums[j] + nums[k] == 0
        # nums[j] + nums[k] = -nums[i]

        for i in range(n):
            if nums[i] > 0:
                # nums[i] is the smallest, if it's positive we can't make zero
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue # avoid duplicate work
            l = i + 1
            r = n - 1

            target = -nums[i]
            while l < r:
                sum = nums[l] + nums[r]
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res