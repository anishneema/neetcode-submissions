class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        memo = {}
        
        def dp(i):

            if i in memo:
                return memo[i]
            
            if i == 0:
                memo[i] = nums[0]
                return memo[i]
            if i == 1:
                memo[i] = max(nums[0], nums[1])
                return memo[i]
            
            memo[i] = max(nums[i] + dp(i-2), dp(i-1))
            return memo[i]
        
        return dp(len(nums)-1)









            



        