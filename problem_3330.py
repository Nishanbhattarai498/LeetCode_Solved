class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        result = 1  # Case when no key was held too long

        i = 0
        while i < n:
            j = i
            # Count how many times the same character repeats
            while j < n and word[j] == word[i]:
                j += 1
            length = j - i
            # If the group length is more than 1, Alice may have overtyped
            if length > 1:
                result += (length - 1)
            i = j
        
        return result
