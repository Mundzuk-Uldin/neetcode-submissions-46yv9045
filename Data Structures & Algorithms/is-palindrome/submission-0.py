class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower().replace(" ","")
        s_list = [x for x in string if x.isalnum()]
        i = 1
        reverse_list = []
        for _ in s_list:
            reverse_list.append(s_list[-i])
            i+=1
        print(reverse_list)
        return reverse_list == s_list
