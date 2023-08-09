#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        st=2
        
        while(st*st<=N):
            if(N%st==0):
                N//=st
            else:
                st+=1
        
        return N


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends