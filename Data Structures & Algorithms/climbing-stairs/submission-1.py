class Solution:
    def climbStairs(self, n: int) -> int:
        arr = {}
        def memo(n):
            if n <= 2:
                return n
            if n in arr:
                return arr[n]
            arr[n] = memo(n-1)+memo(n-2)
            return arr[n]
        return memo(n)