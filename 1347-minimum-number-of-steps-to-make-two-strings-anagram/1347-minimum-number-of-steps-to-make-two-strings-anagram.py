class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n=len(s)
        arr=[0]*26
        for i in range(n):
            arr[ord(s[i])-97]+=1
            arr[ord(t[i])-97]-=1
        ns=ps=0
        for i in arr:
            if i<0:
                ns+=i
            elif i>0:
                ps+=i
        d=ps+abs(ns)
        return d//2