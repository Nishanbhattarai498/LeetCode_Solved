from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        group_count = 1
        group_start = nums[0]  

        for num in nums:
            if num - group_start > k:
                group_count += 1
                group_start = num  
        return group_count
