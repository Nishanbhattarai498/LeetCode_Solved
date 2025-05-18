from functools import lru_cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        colors = [0, 1, 2]  # 0 = Red, 1 = Green, 2 = Blue

        # Generate all valid color combinations for one column (no two adjacent in row same)
        def is_valid(col):
            for i in range(1, m):
                if col[i] == col[i - 1]:
                    return False
            return True

        from itertools import product
        all_cols = [col for col in product(colors, repeat=m) if is_valid(col)]

        # Check if two columns can be adjacent (no same color in same row)
        def is_compatible(col1, col2):
            for i in range(m):
                if col1[i] == col2[i]:
                    return False
            return True

        # Build adjacency graph of valid column transitions
        adj = {col: [] for col in all_cols}
        for col1 in all_cols:
            for col2 in all_cols:
                if is_compatible(col1, col2):
                    adj[col1].append(col2)

        @lru_cache(None)
        def dp(pos, prev_col):
            if pos == n:
                return 1
            total = 0
            for col in adj[prev_col]:
                total = (total + dp(pos + 1, col)) % MOD
            return total

        # Start DP with each valid first column
        res = 0
        for col in all_cols:
            res = (res + dp(1, col)) % MOD

        return res