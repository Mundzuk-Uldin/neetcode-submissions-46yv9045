class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                first = min(dic[complement][0], i)
                second = max(dic[complement][0], i)
                return [first, second]
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]


