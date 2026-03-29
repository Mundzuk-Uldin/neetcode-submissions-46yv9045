class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower().replace(" ","")
        s_list = [x for x in string if x.isalnum()]
        return s_list[::-1] == s_list
