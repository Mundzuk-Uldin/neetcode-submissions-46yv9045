class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify_max(nums)
        ans = 0
        while k>0:
            ans = heapq.heappop_max(nums)
            k-=1
        return ans