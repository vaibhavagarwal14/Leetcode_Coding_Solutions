#User function Template for python3

from typing import List
from collections import deque
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
    
        for i in range(m):
            u, v, w = edges[i]
            adj[u].append((v, w))
    
        q = deque()
        dist = [float('inf')] * n
    
        dist[0] = 0
        q.append((0, 0))
    
        while q:
            node, distance = q.popleft()
    
            for neighbor, ndistance in adj[node]:
                if distance + ndistance < dist[neighbor]:
                    dist[neighbor] = distance + ndistance
                    q.append((neighbor, dist[neighbor]))
    
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
    
        return dist


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends