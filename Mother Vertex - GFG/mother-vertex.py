
class Solution:
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		#Code here
		def dfs(i, vis, adj):
            vis[i] = 1
            for next_node in adj[i]:
                if vis[next_node] == 0:
                    dfs(next_node, vis, adj)
        ans = 0  # Mother vertex
        vis = [0] * V
 
        for i in range(V):
            if vis[i] == 0:
                ans = i
                dfs(i, vis, adj)
 
        vis = [0] * V
        dfs(ans, vis, adj)
 
        if 0 in vis:
            return -1
 
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends