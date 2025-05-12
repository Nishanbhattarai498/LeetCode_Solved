from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        count = Counter(digits)
        
        for num in range(100, 1000, 2):  # even 3-digit numbers
            num_digits = [int(d) for d in str(num)]
            temp_count = Counter(num_digits)
            
            # Check if digits of num are covered by the given digits
            if all(count[d] >= temp_count[d] for d in temp_count):
                result.add(num)
        
        return sorted(result)