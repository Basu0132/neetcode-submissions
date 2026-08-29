class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = set(nums)
        # print(len(k) != len(nums))
        return len(k) != len(nums)