class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        res=10
        ud=9
        an=9
        while n>1 and an>0:
            ud*=an
            res+=ud
            n-=1
            an-=1
        return res