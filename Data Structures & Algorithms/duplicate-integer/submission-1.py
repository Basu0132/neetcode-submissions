class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # k = set(nums)
        # # print(len(k) != len(nums))
        # return len(k) != len(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        return False