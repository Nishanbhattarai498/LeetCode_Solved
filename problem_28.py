class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, return 0 (LeetCode convention)
        if not needle:
            return 0

        # Use Python's built-in string method find()
        return haystack.find(needle)
