#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        def dfs(i,adj,ans,visited):
            visited[i]=True
            ans.append(i)
            
            for nei in adj[i]:
                if(visited[nei]==False):
                    dfs(nei,adj,ans,visited)
            
        ans=[]
        visited=[False]*V
        
        dfs(0,adj,ans,visited)
        
        return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends