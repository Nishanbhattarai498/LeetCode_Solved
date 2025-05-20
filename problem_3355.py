from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        
        # Step 1: Mark the range updates using difference array
        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(diff):
                diff[r + 1] -= 1
        
        # Step 2: Calculate the prefix sum to get the actual coverage per index
        coverage = [0] * n
        current = 0
        for i in range(n):
            current += diff[i]
            coverage[i] = current
        
        # Step 3: Check if each nums[i] can be decremented to 0
        for i in range(n):
            if nums[i] > coverage[i]:
                return False
        
        return True
