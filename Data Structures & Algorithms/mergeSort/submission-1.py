# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs
        return self._mergeSort(pairs, 0, len(pairs)-1)
    
    def _mergeSort(self, pairs: List[Pair], s, e) -> List[Pair]:
        if e - s < 1:
            return [pairs[s]]
        
        m = (s+ e) // 2

        return self._merge(
            self._mergeSort(pairs, s, m),
            self._mergeSort(pairs, m+1, e)
            )
    
    def _merge(self, pair1: List[Pair], pair2: List[Pair]) -> List[Pair]:
        l = 0
        r = 0
        merged = []
        while l < len(pair1) and r < len(pair2):
            if pair1[l].key <= pair2[r].key:
                merged.append(pair1[l])
                l+=1
            else:
                merged.append(pair2[r])
                r+=1
        if r < len(pair2):
            merged.extend(pair2[r:])
        elif l < len(pair1):
            merged.extend(pair1[l:])
        return merged

        