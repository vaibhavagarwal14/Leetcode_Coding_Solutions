#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        ret=[]
        def gcd(a,b):
            if(b==0):
                return a
            return gcd(b,a%b)
        hcf=gcd(A,B)
        ret.append(A*B//hcf)
        ret.append(hcf)
        return ret


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends