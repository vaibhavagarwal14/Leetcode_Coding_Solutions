class Solution:
    def minOperations(self, s: str) -> int:
        def cc(s):
            count=0
            curr=s[0]
            for i in range(1,len(s)):
                if s[i]==curr:
                    count+=1
                    if curr=='1':
                        curr='0'
                    else:
                        curr='1'
                else:
                    curr=s[i]
            return count
        
        if s[0]=='1':
            st='0'+s[1:]
        else:
            st='1'+s[1:]
        return min(cc(s),cc(st)+1)