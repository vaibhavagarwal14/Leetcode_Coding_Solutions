#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        # code here
        s=0
        for i in arr:
            n=i
            while n!=0:
                d=n%10
                s+=d
                n=n//10
        if s%3==0:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends