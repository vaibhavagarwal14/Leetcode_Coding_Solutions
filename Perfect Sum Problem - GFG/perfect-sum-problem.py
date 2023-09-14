#User function Template for python3
MOD = 10**9 + 7
class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		def solve(arr,n,i,sum,dp) :
            if sum==0:
                return 1
            if i>=n:
                return 0
            if (dp[i][sum] != -1):
                return dp[i][sum]

            t = 0
            nt = solve(arr, n, i + 1, sum, dp)

            if (sum >= arr[i]):
                t = solve(arr, n, i + 1, sum - arr[i], dp)

            dp[i][sum] = (t + nt) % (10**9+7)
            return dp[i][sum]
            
        dp=[[-1 for i in range(sum+1)] for j in range(n)]
        arr.sort()
        return solve(arr,n,0,sum,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends