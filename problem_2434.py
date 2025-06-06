class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        count = Counter(s)
        result = []
        stack = []
        min_char = 'a'

        for ch in s:
            stack.append(ch)
            count[ch] -= 1

            # Update min_char to be the smallest character still remaining in s
            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Greedily pop from the stack if the top is <= min_char
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())

        # Pop remaining characters from the stack
        while stack:
            result.append(stack.pop())

        return ''.join(result)
