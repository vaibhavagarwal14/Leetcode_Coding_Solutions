class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        n=len(s)
        st=""
        while i<n:
            if s[i]==' ':
                i+=1
                continue
            j=i+1
            while j<n:
                if s[j]==' ':
                    break
                j+=1
            for k in range(j-1,i-1,-1):
                st+=s[k]
            if j!=n:
                st+=' '
            i=j+1
        return st