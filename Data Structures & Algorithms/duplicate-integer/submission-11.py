class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i=0
        for _ in range(len(nums)//2):
            if (len(nums)-1 > i) and (nums[i] == nums[i+1]):
                return True
            i += 2
        return False