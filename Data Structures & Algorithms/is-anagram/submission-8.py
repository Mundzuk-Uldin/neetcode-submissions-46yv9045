class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sWordCount, tWordCount = {}, {}

        for i in range(len(s)):
            sWordCount[s[i]] = 1 + sWordCount.get(s[i], 0)
            tWordCount[t[i]] = 1 + tWordCount.get(t[i], 0)
        return sWordCount == tWordCount