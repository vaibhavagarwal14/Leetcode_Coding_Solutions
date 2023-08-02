#User function Template for python3
from queue import Queue
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        if(A[0][0]==0): return -1
        
        queue=Queue()
        visited=[[False for i in range(M)] for j in range(N)]
        path=0;

        queue.put([0,0])
        visited[0][0]=True
        while(not queue.empty()):
            
            size=queue.qsize()
            
            for i in range(size):
                cur=queue.get()
                
                if(cur[0]==X and cur[1]==y): return path
                
                if(cur[0]+1<N and (not visited[cur[0]+1][cur[1]]) and A[cur[0]+1][cur[1]]==1):
                    queue.put([cur[0]+1,cur[1]])
                    visited[cur[0]+1][cur[1]]=True
                if(cur[0]-1>=0 and (not visited[cur[0]-1][cur[1]]) and A[cur[0]-1][cur[1]]==1):
                    queue.put([cur[0]-1,cur[1]])
                    visited[cur[0]-1][cur[1]]=True
                if(cur[1]+1<M and (not visited[cur[0]][cur[1]+1]) and A[cur[0]][cur[1]+1]==1):
                    queue.put([cur[0],cur[1]+1])
                    visited[cur[0]][cur[1]+1]=True
                if(cur[1]-1>=0 and (not visited[cur[0]][cur[1]-1]) and A[cur[0]][cur[1]-1]==1):
                    queue.put([cur[0],cur[1]-1])
                    visited[cur[0]][cur[1]-1]=True

            
            
            path+=1
            
            
        return -1

#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends