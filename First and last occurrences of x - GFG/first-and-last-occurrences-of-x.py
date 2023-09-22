#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        l=0
        u=n-1
        f=s=-1
        while l<=u:
            mid=(l+u)//2
            if arr[mid]==x and (mid-1==-1 or arr[mid-1]!=x):
                f=mid
                break
            elif arr[mid]<x:
                l=mid+1
            else:
                u=mid-1
        l=0
        u=n-1
        while l<=u:
            mid=(l+u)//2
            if arr[mid]==x and (mid+1==n or arr[mid+1]!=x):
                s=mid
                break
            elif arr[mid]>x:
                u=mid-1
            else:
                l=mid+1
        return [f,s]


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends