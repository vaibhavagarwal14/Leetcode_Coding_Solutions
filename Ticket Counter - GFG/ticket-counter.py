class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        # Code Here
        d=N//K
        r=N%K
        if(r==0):
            if(d%2==0):
                return (d//2)*K+1
            else:
                return ((d+1)//2)*K
        else:
            if(d%2==0):
                return (d//2)*K+r
            else:
                return ((d+1)//2)*K+1

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends