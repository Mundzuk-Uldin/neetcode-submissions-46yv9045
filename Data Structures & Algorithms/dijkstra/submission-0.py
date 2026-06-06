class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        # u is source, v is destination, and w is weight
        for u, v, w in edges:
            adjList[u].append((w,v))
        shortest = {}
        # weight first for the heap sorting to work properly 
        minHeap = [(0, src)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for w2, n2 in adjList[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w2+w1, n2))
        for n in adjList.keys():
            if n not in shortest:
                shortest[n] = -1
        return shortest

            