class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        dic = {}
        for i,n in enumerate(nums):
            difference = target - n
            if(difference in dic):
                return [dic[difference], i]
            dic[n] = i
        return
        