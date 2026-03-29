class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = []
        for n in nums:
            if n in array:
                return True
            else:
                array.append(n)
        return False