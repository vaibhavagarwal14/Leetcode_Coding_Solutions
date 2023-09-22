class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if len(s)==0:
            return 1
        if len(t)==0:
            return 0
        for i in range(len(t)):
            if t[i]==s[j]:
                j+=1
            if j==len(s):
                return 1
        return 0