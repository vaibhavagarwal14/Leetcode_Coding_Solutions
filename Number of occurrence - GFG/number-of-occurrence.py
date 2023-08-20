#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		first=-1
		l=0
		u=n-1
		while l<=u:
		    mid=(l+u)//2
		    if arr[mid]==x and (mid==0 or arr[mid-1]<x):
		        first = mid
		        break
		    elif arr[mid]<x:
		        l=mid+1
		    else:
		        u=mid-1
	    if first==-1:
	        return 0
	    l=0
	    u=n-1
	    last=-1
	    while l<=u:
	        mid=(l+u)//2
	        if arr[mid]==x and (mid==n-1 or arr[mid+1]>x):
	            last=mid
	            break
	        elif arr[mid]>x:
	            u=mid-1
	        else:
	            l=mid+1
	    return last-first+1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends