from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Attach original indices to each number
        indexed_nums = [(i, num) for i, num in enumerate(nums)]
        
        # Sort by value in descending order to get top k largest elements
        indexed_nums.sort(key=lambda x: x[1], reverse=True)
        
        # Take top k elements
        top_k = indexed_nums[:k]
        
        # Sort the top k elements by their original indices to maintain order
        top_k.sort(key=lambda x: x[0])
        
        # Extract and return just the values
        return [num for i, num in top_k]
