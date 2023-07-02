#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        c={}
        for i in A:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        mx=max(c.values())
        if(mx>N//2):
            for key in c:
                if(c[key]==mx):
                    return key
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends