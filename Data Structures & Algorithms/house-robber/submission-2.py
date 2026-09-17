class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def robOrSkip(n):
            if n == 1:
                return max(nums[n],nums[n-1])
            if n == 0:
                return nums[0]
            if n in memo:
                return memo[n]
            memo[n] = max(nums[n] + robOrSkip(n-2), robOrSkip(n-1))
            return memo[n]
            
        return robOrSkip(len(nums)-1)
            
