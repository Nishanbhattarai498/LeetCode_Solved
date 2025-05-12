from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        length = len(arr)
        for a in range(length - 2):  # Stop at length-2 to avoid IndexError
            if arr[a] % 2 == 1 and arr[a + 1] % 2 == 1 and arr[a + 2] % 2 == 1:
                return True
        return False
