class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0 and bin(n).count('1')==1 and (n-1)%3==0:
            return True
        return False