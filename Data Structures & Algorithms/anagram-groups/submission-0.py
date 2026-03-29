class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i,n in enumerate(strs):
            sorted_word = "".join(sorted(n))
            if(sorted_word in hashmap):
                hashmap[sorted_word].append(n)
            else:
                hashmap[sorted_word] = [n]
        array = []
        for i in hashmap:
            array.append(hashmap[i])
        return array