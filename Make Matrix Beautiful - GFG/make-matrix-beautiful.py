#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code here
        s=0
        for i in range(n):
            for j in range(n):
                s+=matrix[i][j]
        rs=0
        cs=0
        for i in range(n):
            a=0
            for j in range(n):
                a=a+matrix[i][j]
            rs=max(rs,a)
            b=0
            for j in range(n):
                b=b+matrix[j][i]
            cs=max(cs,b)
        maxval=max(cs,rs)
        return maxval*n-s
            


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends