class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        q=n//3
        r=n%3
        if r==0:
            ans=3**q
        if r==1:
            ans=(3**(q-1))*4
        if r==2:
            ans=(3**q)*r
        return ans