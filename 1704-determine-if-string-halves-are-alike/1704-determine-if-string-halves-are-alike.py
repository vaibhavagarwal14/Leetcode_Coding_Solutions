class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c=0
        n=len(s)
        for i in range(n//2):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                c+=1
        for i in range(n//2,n):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                c-=1
        if c==0:
            return 1
        return 0