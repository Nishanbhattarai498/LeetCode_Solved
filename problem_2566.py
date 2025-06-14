class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # Generate maximum possible value
        for ch in s:
            if ch != '9':
                max_val = int(s.replace(ch, '9'))
                break
        else:
            max_val = num  # all digits are 9 already

        # Generate minimum possible value
        for ch in s:
            if ch != '0':
                min_val = int(s.replace(ch, '0'))
                break
        else:
            min_val = num  # all digits are 0 already

        return max_val - min_val
