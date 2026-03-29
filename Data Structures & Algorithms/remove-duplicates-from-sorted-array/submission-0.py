class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_dups = [nums[0]]
        for n in nums:
            if n != non_dups[-1]:
                non_dups.append(n)
        for i in range(len(non_dups)):
            nums[i] = non_dups[i] 
        return len(non_dups)