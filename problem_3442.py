from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freqs = []
        even_freqs = []

        for count in freq.values():
            if count % 2 == 1:
                odd_freqs.append(count)
            else:
                even_freqs.append(count)

        max_diff = float('-inf')
        for o in odd_freqs:
            for e in even_freqs:
                max_diff = max(max_diff, o - e)

        return max_diff