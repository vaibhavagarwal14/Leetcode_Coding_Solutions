class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Appraoch 1 - BF O(((n*m)*(n+m))+(n*m))~O(n^3)
        
        # Approach 2 - Better BF O(2*m*n) and SC=O(m+n)
        
        # Approach 3 - O(2*n*m) and SC=O(1)
        col=1
        if matrix[0][0]==0:
            col=0
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if j!=0:
                    if(matrix[i][0]==0 or matrix[0][j]==0):
                        matrix[i][j]=0
                else:
                    if(matrix[i][0]==0 or col==0):
                        matrix[i][j]=0