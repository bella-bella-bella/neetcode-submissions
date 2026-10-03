class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = set(nums)
        longest = 0

        for num in nums_hash:
            if num - 1 not in nums_hash:
                length = 1
                while num + length in nums_hash:
                    length += 1
                longest = max(longest, length)

        return longest
