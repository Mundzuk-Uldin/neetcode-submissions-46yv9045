class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        dic = {}
        for i,n in enumerate(nums):
            difference = target - n
            if(n in dic):
                return [dic[n], i]
            dic[difference] = i
        return
        