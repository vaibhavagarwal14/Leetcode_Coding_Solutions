#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        if 1 not in arr:
            return 1
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = 1
        for i in range(n):
            arr[((arr[i] - 1) % n + n) % n] += n
        for i in range(n):
            if arr[i] <= n:
                return i + 1
        return n + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends