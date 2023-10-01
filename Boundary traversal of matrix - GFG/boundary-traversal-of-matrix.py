#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        lst=[]
        t=0
        b=n-1
        l=0
        r=m-1
        for i in range(m):
            lst.append(matrix[0][i])
        t+=1
        for i in range(1,n):
            lst.append(matrix[i][m-1])
        r-=1
        if t<=b:
            for i in range(m-2,-1,-1):
                lst.append(matrix[n-1][i])
            b-=1
        if l<=r:
            for i in range(n-2,0,-1):
                lst.append(matrix[i][0])
            l+=1
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends