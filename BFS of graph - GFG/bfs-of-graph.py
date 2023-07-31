#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        ans=[]
        q=Queue()
        visited=[False]*V
        
        q.put(0)
        visited[0]=True
        
        while(not q.empty()):
            u=q.get()
            
            ans.append(u)
            
            for el in adj[u]:
                if visited[el]==False:
                    q.put(el)
                    visited[el]=True

        return ans


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends