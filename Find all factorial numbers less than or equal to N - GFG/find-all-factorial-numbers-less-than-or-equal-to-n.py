#User function Template for python3
import math
class Solution:
    def factorialNumbers(self, N):
    	#code here 
    	lst=[]
    	for i in range(1,N+1):
    	    if(math.factorial(i)<=N):
    	        lst.append(math.factorial(i))
    	    else:
    	        break
    	return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        
# } Driver Code Ends