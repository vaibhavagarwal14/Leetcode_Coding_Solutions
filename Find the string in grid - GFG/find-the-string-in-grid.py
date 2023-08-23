#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
		# Code here
		def isSafe(i, j, k, grid, word, n, m):
            if i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == word[k]:
                return True
            return False
        def solve(i, j, k, grid, word, n, m, row, col):
            if k == len(word):
                return 1
            if isSafe(i + row, j + col, k, grid, word, n, m):
                count = solve(i + row, j + col, k + 1, grid, word, n, m, row, col)
                if count == 1:
                    return 1
            return 0
		row=[-1,-1,0,1,1,1,0,-1]
		col=[0,1,1,1,0,-1,-1,-1]
		n=len(grid)
		m=len(grid[0])
		ans=[]
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==word[0]:
		            res=0
		            for k in range(8):
		                r=i+row[k]
		                c=j+col[k]
		                count=0
		                if len(word)>1:
		                    if isSafe(r,c,1,grid,word,n,m):
		                        count = solve(r,c,2,grid,word,n,m,row[k],col[k])
		                        if count==1:
		                            res=1
		                            break
		                else:
		                    res=1
		            if(res==1):
                        abc=[]
                        abc.append(i)
                        abc.append(j)
                        ans.append(abc)
        arr = [[0]*2 for _ in range(len(ans))]
        for i in range(len(ans)):
            arr[i][0] = ans[i][0]
            arr[i][1] = ans[i][1]
        return arr
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends