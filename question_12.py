from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start by assuming the entire first string is the common prefix
        prefix = strs[0]

        # Compare the prefix with every other string in the list
        for s in strs[1:]:
            # Keep reducing the prefix until it's a prefix of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
                if not prefix:
                    return ""
        
        return prefix
