class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=len(num1)
        n2=len(num2)
        lst=[0]*(n1+n2)
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                mul=int(num1[i])*int(num2[j])
                summ=mul+lst[i+j+1]
                lst[i+j]+=summ//10
                lst[i+j+1]=summ%10
        for i in range(n1+n2):
            if(lst[i]!=0):
                break
        s=''.join(map(str,(lst[i:])))
        return s