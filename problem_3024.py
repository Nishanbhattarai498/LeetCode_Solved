class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        
        # Triangle Inequality Theorem: sum of any two sides > third side
        if a + b <= c:
            return "none"
        
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
