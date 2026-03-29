class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0
        r = 0
        sort = []
        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                sort.append(nums1[l])
                l+=1
            else:
                sort.append(nums2[r])
                r+=1
        # Handle leftovers
        while l <m:
            sort.append(nums1[l])
            l+=1
        while r < n:
            sort.append(nums2[r])
            r+=1
        i = 0
        # Solve in place
        while i < len(nums1):
            nums1[i] = sort[i]
            i+=1 