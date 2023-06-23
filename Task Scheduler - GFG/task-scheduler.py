#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def leastInterval(self, N, K, tasks):
        # Code here
        freq=[0]*26
        for i in tasks:
            freq[ord(i)-65]+=1
        freq.sort()
        mx=freq[25]
        idle=(mx-1)*K
        for i in range(24,-1,-1):
            if (freq[i]>0):
                idle-=min(freq[i],mx-1)
        idle=max(idle,0)
        return N+idle

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        tasks = input().split()
        ob = Solution()
        res = ob.leastInterval(N, K, tasks)
        print(res)
# } Driver Code Ends