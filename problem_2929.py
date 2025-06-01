from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Total number of unrestricted non-negative solutions (a + b + c = n)
        def count_ways(total):
            return comb(total + 2, 2) if total >= 0 else 0

        total_ways = count_ways(n)

        # Subtract ways where one child gets more than limit
        over1 = count_ways(n - (limit + 1)) * 3

        # Add back ways where two children get more than limit (double-subtracted)
        over2 = count_ways(n - 2 * (limit + 1)) * 3

        # Subtract again ways where all three children get more than limit
        over3 = count_ways(n - 3 * (limit + 1))

        return total_ways - over1 + over2 - over3
