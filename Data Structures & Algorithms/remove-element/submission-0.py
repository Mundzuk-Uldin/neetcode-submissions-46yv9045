class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        no_val = []
        for n in nums:
            if n != val:
                no_val.append(n)
        for i in range(len(no_val)):
            nums[i] = no_val[i]
        return len(no_val)