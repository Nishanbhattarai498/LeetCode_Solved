class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix: int, n: int) -> int:
            count = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        current = 1
        k -= 1  # Since we start from 1

        while k > 0:
            steps = count_prefix(current, n)
            if steps <= k:
                k -= steps
                current += 1  # move to next prefix
            else:
                current *= 10  # go deeper
                k -= 1

        return current