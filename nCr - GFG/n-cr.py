#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        C = [0 for i in range(r+1)]
        C[0] = 1  # since nC0 is 1
        m=10**9+7
        for i in range(1, n+1):
            j = min(i, r)
            while (j > 0):
                C[j] = ((C[j]%m) + (C[j-1]%m))%m
                j -= 1
 
        return C[r]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends