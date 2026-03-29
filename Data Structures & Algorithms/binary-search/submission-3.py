class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._binarySearch(nums, target, 0, len(nums)-1)
    def _binarySearch(self, nums, target, l, r):
        if l > r:
            return -1
        m = (l+r) // 2
        if nums[m] < target:
            return self._binarySearch(nums, target, m+1, r)
        elif nums[m] > target:
            return self._binarySearch(nums, target, l, m-1)
        else:
            return m
