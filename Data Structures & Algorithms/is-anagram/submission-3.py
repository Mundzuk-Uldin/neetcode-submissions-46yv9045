class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) == len(t)):
            char_arr1 = [x for x in s]
            char_arr2 = [x for x in t]
            if(sorted(char_arr1) == sorted(char_arr2)):
                return True

        return False