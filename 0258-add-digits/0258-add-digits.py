class Solution:
    def addDigits(self, num: int) -> int:
        # while(1):
        #     if len(str(num))==1:
        #         return num
        #     num=sum([int(digit) for digit in str(num)])
        
        return 0 if num==0 else 1+(num-1)%9