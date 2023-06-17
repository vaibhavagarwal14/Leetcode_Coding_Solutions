class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=max(len(a),len(b))
        a=a.zfill(n)
        b=b.zfill(n)
        res=""
        carry=0
        for i in range(n-1,-1,-1):
            r=carry
            r+=1 if a[i]=='1' else 0
            r+=1 if b[i]=='1' else 0
            res=('1' if r%2==1 else '0')+res
            carry=0 if r<2 else 1
        if carry!=0:
            res='1'+res
        return res