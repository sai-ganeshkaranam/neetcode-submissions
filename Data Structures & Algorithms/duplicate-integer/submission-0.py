class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]!= nums[j]:
        #             return False
                
        # return True
        return n != len(set(nums))


        