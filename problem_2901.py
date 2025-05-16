from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        # DP array to store the length of longest subsequence ending at each index
        dp = [1] * n
        # Parent array to reconstruct the subsequence
        parent = [-1] * n
        
        for i in range(n):
            for j in range(i):
                # Check conditions:
                # 1. Groups must be different
                # 2. Words must be same length
                # 3. Hamming distance must be exactly 1
                if (groups[i] != groups[j] and 
                    len(words[i]) == len(words[j]) and 
                    self.hamming_distance(words[i], words[j]) == 1):
                    
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
        
        # Find the index with maximum subsequence length
        max_len = max(dp)
        if max_len == 1:
            return [words[0]]  # return any single word if no longer subsequence exists
        
        last_idx = dp.index(max_len)
        
        # Reconstruct the subsequence in reverse order
        subsequence_indices = []
        while last_idx != -1:
            subsequence_indices.append(last_idx)
            last_idx = parent[last_idx]
        
        # Reverse to get correct order
        subsequence_indices.reverse()
        
        return [words[i] for i in subsequence_indices]
    
    def hamming_distance(self, s1: str, s2: str) -> int:
        # Calculate hamming distance between two equal-length strings
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))