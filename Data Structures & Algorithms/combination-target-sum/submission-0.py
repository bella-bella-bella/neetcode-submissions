class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start: int, path: List[int], total: int) -> None:
            if total == target:
                res.append(path)
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                dfs(i, path + [nums[i]], total + nums[i])

        dfs(0, [], 0)
        return res