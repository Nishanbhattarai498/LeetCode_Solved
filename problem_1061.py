class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize parent array for Union-Find (26 lowercase letters)
        parent = [i for i in range(26)]

        # Helper: Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Helper: Union two characters by attaching larger root to smaller one
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py

        # Union all character pairs from s1 and s2
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        # Build the result string by replacing each character with its group's smallest equivalent
        result = []
        for ch in baseStr:
            smallest_char = chr(find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest_char)

        return ''.join(result)