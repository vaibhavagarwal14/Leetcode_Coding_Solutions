class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st=""
        for i in s:
            if i.isalnum():
                st+=i
        n=len(st)
        if(n%2==0):
            s1=st[:n//2]
            s2=st[n//2:]
        else:
            s1=st[:n//2]
            s2=st[(n//2)+1:]
        s2=s2[::-1]
        if(s1==s2):
            return True
        return False