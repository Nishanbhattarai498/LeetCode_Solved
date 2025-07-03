class Solution:
    def kthCharacter(self, k: int) -> str:
        def shift(ch: str) -> str:
            return 'a' if ch == 'z' else chr(ord(ch) + 1)

        def helper(k: int) -> str:
            if k == 1:
                return 'a'
            # Find smallest power of 2 >= k
            length = 1
            while length < k:
                length <<= 1  # same as length *= 2
            half = length >> 1
            if k <= half:
                return helper(k)
            else:
                return shift(helper(k - half))

        return helper(k)
