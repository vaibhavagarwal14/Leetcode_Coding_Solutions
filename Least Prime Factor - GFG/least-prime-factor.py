#User function Template for python3
import math
class Solution:
    def leastPrimeFactor (self, n):
        # code here
        lst=[0]*(n+1)
        lst[1]=1
        for i in range(2,n+1):
            if(lst[i]==0):
                lst[i]=i
                for j in range(i*i,n+1,i):
                    if(lst[j]==0):
                        lst[j]=i
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends