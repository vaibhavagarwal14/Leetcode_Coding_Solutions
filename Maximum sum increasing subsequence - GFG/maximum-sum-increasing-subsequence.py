#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		dp = Arr.copy()
		ans = dp[0]
		for i in range(1, n):
		    for j in range(i - 1, -1, -1):
		        if Arr[j] < Arr[i]:
		            dp[i] = max(dp[i], dp[j] + Arr[i])
            ans = max(ans, dp[i])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends