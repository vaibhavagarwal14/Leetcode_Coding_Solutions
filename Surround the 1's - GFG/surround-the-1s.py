#User function Template for python3

class Solution:
	def Count(self, matrix):
		# Code here
		count=0
		row=[-1,-1,0,1,1,1,0,-1]
		col=[0,1,1,1,0,-1,-1,-1]
		n=len(matrix)
		m=len(matrix[0])
		for i in range(n):
		    for j in range(m):
		        if matrix[i][j]==1:
		            zero=0
		            for k in range(8):
		                r=i+row[k]
		                c=j+col[k]
		                if r>=0 and r<n and c>=0 and c<m and matrix[r][c]==0:
		                    zero+=1
		            if zero>0 and zero%2==0:
		                count+=1
		return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends