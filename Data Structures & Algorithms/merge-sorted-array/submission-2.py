class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n
        while i > 0:
            nums1[m + n - i] = nums2[n - i]
            i -= 1
        self._mergeSort(nums1, 0, len(nums1)-1)
    def _mergeSort(self, nums: List[int], s: int, e: int) -> List[int]:
        if e - s < 1:
            return nums
        m = (e+s)//2

        self._mergeSort(nums, s, m)
        self._mergeSort(nums, m+1, e)
        
        return self._mergeHelper(nums,s,m,e)
        
    def _mergeHelper(self, nums: List[int], s: int, m: int, e: int) -> None:
        sort = []
        i = s
        j = m+1
        while i <= m and j <= e:
            if nums[i] <= nums[j]:
                sort.append(nums[i])
                i += 1
            else:
                sort.append(nums[j])
                j += 1
        
        #Handle leftovers
        while i <= m:
            sort.append(nums[i])
            i += 1
        while j <= e:
            sort.append(nums[j])
            j += 1
        
        # Replace in-place
        n = 0
        k = s
        while k <= e:
            nums[k] = sort[n]
            k+=1
            n+=1