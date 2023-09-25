class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Approach 1 - use map and count
        
        # count = collections.Counter(s)
        # for i, c in enumerate(t):
        #     count[c] -= 1
        #     if count[c] == -1:
        #         return c
        
        # Approach 2 - sum ascii
        ss=0
        ts=0
        for i in range(len(s)):
            ss+=ord(s[i])
            ts+=ord(t[i])
        ts+=ord(t[-1])
        return chr(abs(ts-ss))