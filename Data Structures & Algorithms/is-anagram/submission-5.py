class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = list(t)

        if len(s) != len(t) or len(s) < 1:
            return False
        for char in s:
            if char in array:
                array.remove(char)
            else:
                return False
        return True