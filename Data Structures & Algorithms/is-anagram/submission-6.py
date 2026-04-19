class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sWordCount ={}
        tWordCount ={}
        def wordCount(dic, string):
            for char in string:
                if char in dic:
                    dic[char] +=1
                else:
                    dic[char] = 1
        wordCount(sWordCount, s)
        wordCount(tWordCount, t)
        if len(sWordCount.keys()) != len(tWordCount.keys()):
            return False
        for char in sWordCount:
            if char not in tWordCount:
                return False
            if tWordCount[char] != sWordCount[char]:
                return False
        return True