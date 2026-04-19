class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        min_heap = []
        ans = []
        for point in points:
            heapq.heappush(min_heap, (point[0] * point[0] + point[1] * point[1], point))
        for i in range(k):
            ans.append(heapq.heappop(min_heap)[1])
        return ans