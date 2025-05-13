MOD = 10**9 + 7

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                count = freq[i]
                if i == 25:  # 'z'
                    new_freq[0] = (new_freq[0] + count) % MOD  # 'a'
                    new_freq[1] = (new_freq[1] + count) % MOD  # 'b'
                else:
                    new_freq[i + 1] = (new_freq[i + 1] + count) % MOD
            freq = new_freq
        
        return sum(freq) % MOD