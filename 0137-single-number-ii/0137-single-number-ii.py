class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones=0
        twos=0
        for i in nums:
            ones^=i&~twos
            twos^=i&~ones
        return ones