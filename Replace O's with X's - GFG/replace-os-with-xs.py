#User function Template for python3

class Solution:
    def __init__(self):
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, 1, 0, -1]
 
    def fill(self, n, m, mat):
        def is_safe(i, j, mat, vis):
            return (i >= 0 and j >= 0 and i < len(mat) and j < len(mat[0]) and not vis[i][j] and mat[i][j] == 'O')
 
        def dfs(i, j, mat, vis):
            vis[i][j] = True
            for k in range(4):
                ni, nj = i + self.dx[k], j + self.dy[k]
                if is_safe(ni, nj, mat, vis):
                    dfs(ni, nj, mat, vis)
 
        vis = [[False for _ in range(m)] for _ in range(n)]
 
        # Doing DFS for 'O's in the first row
        for i in range(m):
            if not vis[0][i] and mat[0][i] == 'O':
                dfs(0, i, mat, vis)
 
        # Doing DFS for 'O's in the last row
        for i in range(m):
            if not vis[n - 1][i] and mat[n - 1][i] == 'O':
                dfs(n - 1, i, mat, vis)
 
        # Doing DFS for 'O's in the first column
        for i in range(n):
            if not vis[i][0] and mat[i][0] == 'O':
                dfs(i, 0, mat, vis)
 
        # Doing DFS for 'O's in the last column
        for i in range(n):
            if not vis[i][m - 1] and mat[i][m - 1] == 'O':
                dfs(i, m - 1, mat, vis)
 
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O' and not vis[i][j]:
                    mat[i][j] = 'X'
 
        return mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends