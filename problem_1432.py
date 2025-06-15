class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Step 1: Find max_num by replacing the first non-9 digit with 9
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # already all 9s

        # Step 2: Find min_num
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num  # already minimal

        return max_num - min_num