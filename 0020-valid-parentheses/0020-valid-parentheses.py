class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                lst.append(s[i])
            else:
                if(len(lst)==0):
                    return 0
                cc=lst.pop()
                if cc=='(' and s[i]!=')':
                    return 0
                if cc=='[' and s[i]!=']':
                    return 0
                if cc=='{' and s[i]!='}':
                    return 0
        if len(lst)!=0:
            return 0
        return 1