class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(0, n, 3):
            group = nums[i:i+3]
            if group[-1] - group[0] > k:
                return []
            res.append(group)

        return res
