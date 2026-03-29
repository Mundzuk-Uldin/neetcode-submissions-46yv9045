class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            if n in dic.keys():
                return True
            dic[n] = 0
        return False