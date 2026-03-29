from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)< 1):
            return 0
        set_list = nums[::]
        longest_list = 0
        candidate = set_list[0]
        while(candidate in set_list):
            long_list = []
            long_list.append(candidate)
            self.remove_value(set_list, candidate)            
            r = candidate+1
            l = candidate-1
            while(l in set_list):
                long_list.append(l)
                self.remove_value(set_list, l)            
                l-=1
            while(r in set_list):
                long_list.append(r)
                self.remove_value(set_list, r)
                r+=1
                
            if(len(long_list)>longest_list):
                longest_list = len(long_list)
                
            if(len(set_list) > 1):
                candidate = set_list[0]
                
        return longest_list
    
    def remove_value(self, set_list, val):
        while val in set_list:
            set_list.remove(val)