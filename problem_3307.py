class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        n = len(operations)
        lengths = [1] * (n + 1)  # length after each step, initial word = "a"

        # Step 1: compute lengths at each step
        for i in range(n):
            lengths[i + 1] = lengths[i] * 2

        shift_count = 0  # how many times the character is shifted due to op==1 on second half

        # Step 2: backtrack from last operation
        for i in range(n - 1, -1, -1):
            op = operations[i]
            prev_len = lengths[i]

            if k > prev_len:
                # We're in the second half
                k -= prev_len
                if op == 1:
                    shift_count += 1  # because second half is "next" version
                # if op == 0: it's just a copy, so no change
            else:
                # Still in first half, k remains same
                continue

        # Step 3: Original character is always 'a'
        base_char = ord('a')
        final_char = chr((base_char - ord('a') + shift_count) % 26 + ord('a'))
        return final_char
