class Solution:
    def isHappy(self, n: int) -> bool:
        while(1):
            if n==1:
                return True
            if n==4:
                return False
            n=sum([(int)(digit)**2 for digit in str(n)])