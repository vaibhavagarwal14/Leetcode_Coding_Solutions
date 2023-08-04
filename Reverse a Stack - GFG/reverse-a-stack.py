#User function Template for python3

from typing import List
import sys

sys.setrecursionlimit(10000000)
class Solution:
    def reverse(self,St): 
        #code here
        def insertAtLast(St,val):
            if(len(St)==0):
                St.append(val)
                return
            
            el=St.pop(len(St)-1)
            insertAtLast(St,val)
            St.append(el)
            
        if(len(St)==0): return;
        
        el=St.pop(len(St)-1)
        self.reverse(St)
        
        insertAtLast(St,el)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends