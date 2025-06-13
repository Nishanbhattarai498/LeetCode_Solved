from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def can_form_pairs(max_diff: int) -> bool:
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2  # Skip both elements to avoid overlap
                else:
                    i += 1
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        result = right

        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result