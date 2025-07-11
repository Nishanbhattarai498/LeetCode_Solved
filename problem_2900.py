from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        last_group = -1  # Initialize with a value not in [0, 1]

        for word, group in zip(words, groups):
            if group != last_group:
                result.append(word)
                last_group = group

        return result