class Solution:
    def myAtoi(self, s: str) -> int:
        num=0
        i=0
        while i<len(s) and s[i]==' ':
            i+=1
        if(i<len(s) and s[i]=='-'):
            i+=1
            while(i<len(s) and s[i].isdigit()):
                d=ord(s[i])-48
                num=num*10+d
                i+=1
            if(num>2**31):
                num=-(2**31)
            else:
                num=0-num
            return num
        else:
            if(i<len(s) and s[i]=='+'):
                i+=1
            while(i<len(s) and s[i].isdigit()):
                d=ord(s[i])-48
                num=num*10+d
                i+=1
            if(num>=2**31):
                num=(2**31)-1
            return num