#User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
    	#code here 
    	s=0
        for i in range(1,N+1):
            d=N//i
            s+=i*d
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends