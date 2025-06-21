from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        min_deletions = float('inf')

        for i in range(n):
            base_freq = freq[i]
            deletions = 0

            # Delete all characters with frequency < base_freq
            deletions += sum(freq[j] for j in range(i))

            # Reduce characters with frequency > base_freq + k
            for j in range(i + 1, n):
                if freq[j] > base_freq + k:
                    deletions += freq[j] - (base_freq + k)

            min_deletions = min(min_deletions, deletions)

        return min_deletions
