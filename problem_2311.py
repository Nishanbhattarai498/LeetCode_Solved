class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0        # Length of subsequence
        value = 0        # Current binary value of selected bits
        power = 0        # Current bit position (right to left)

        # Traverse the string from right (least significant bit) to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                count += 1  # Always include zeros
            else:
                # Only consider 1s if including them doesn’t exceed k
                if power < 32 and value + (1 << power) <= k:
                    value += (1 << power)
                    count += 1
            power += 1

        return count
