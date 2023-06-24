class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx=0
        for i in range(len(s)):
            j=i
            p=""
            while j <len(s):
                if(s[j] not in p):
                    p+=s[j]
                    j+=1
                else:
                    if(len(p)>mx):
                        mx=len(p)
                    break
                if(j==len(s)):
                    if(len(p)>mx):
                        mx=len(p)
        return mx