class Solution:
    def addDigits(self, num: int) -> int:
        while(1):
            if len(str(num))==1:
                return num
            num=sum([int(digit) for digit in str(num)])