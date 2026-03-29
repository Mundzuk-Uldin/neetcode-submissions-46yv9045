class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(len(nums) == 1):
            return [nums[0]]
        
        left_pointer = 0
        frequent_dict = {}
        
        while (left_pointer < len(nums)):
            num = nums[left_pointer]
            if(num in frequent_dict):
                left_pointer += 1
                continue
            frequent_dict[num] = 1
            right_pointer = left_pointer + 1
            while(right_pointer < len(nums)):
                if(nums[right_pointer] == num):
                    frequent_dict[num] += 1
                right_pointer+=1
            if(len(frequent_dict) > k):
                smallest_key = min(frequent_dict, key=frequent_dict.get)
                del frequent_dict[smallest_key]
            left_pointer += 1
        return [*frequent_dict]