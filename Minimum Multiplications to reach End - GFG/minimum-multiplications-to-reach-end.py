#User function Template for python3

from typing import List
from collections import deque 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        ans = [-1 for i in range(100001)]
        mod = 100000
 
        q = deque()
        q.append(start % mod)
 
        ans[start] = 0
        while (len(q) > 0):
 
            top = q.popleft()
 
            if (top == end):
                return ans[end]
 
            for i in range(n):
                pushed = top * arr[i]
                pushed = pushed % mod
 
                if (ans[pushed] == -1):
                    ans[pushed] = ans[top] + 1
                    q.append(pushed)
             
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends