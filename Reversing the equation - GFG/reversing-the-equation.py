#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        rev=[]
        d=s[0]
        for i in range(1,len(s)):
            if(s[i].isdigit()):
                d+=s[i]
            else:
                rev.append(d)
                rev.append(s[i])
                d=""
        rev.append(d)
        revs=""
        for i in range(len(rev)-1,-1,-1):
            revs+=rev[i]
        
        return revs

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends