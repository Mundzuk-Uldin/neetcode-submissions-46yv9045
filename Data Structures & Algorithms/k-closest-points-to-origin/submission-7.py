import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dic = {}
        def euclideanDistance(x2: int,y2: int)-> int:
            return math.sqrt(x2**2 + y2**2)
        for point in points:
            distance = euclideanDistance(point[0], point[1])
            heapq.heappush_max(heap, distance)
            if distance in dic:
                dic[distance].append(point)
            else:
                dic[distance] = [point]
            if len(heap) > k:
                heapq.heappop_max(heap)
        res = []
        for h in heap:
            res.append(dic[h].pop())
        return res