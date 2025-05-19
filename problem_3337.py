MOD = 10**9 + 7

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Step 1: Create a 26x26 transformation matrix M
        M = [[0] * 26 for _ in range(26)]
        
        for i in range(26):  # for each character from 'a' to 'z'
            for j in range(nums[i]):
                M[i][(i + j + 1) % 26] += 1  # wrap around with modulo 26

        # Step 2: Matrix exponentiation to raise M to power t
        def mat_mult(A, B):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    for j in range(26):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res

        def mat_pow(mat, power):
            res = [[int(i == j) for j in range(26)] for i in range(26)]  # Identity matrix
            while power:
                if power % 2:
                    res = mat_mult(res, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return res

        Mt = mat_pow(M, t)  # M raised to the power t

        # Step 3: Count initial frequency of each character in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Step 4: Calculate total resulting string length
        total = 0
        for i in range(26):  # for each starting character
            for j in range(26):  # sum how many characters it generates
                total = (total + freq[i] * Mt[i][j]) % MOD

        return total
