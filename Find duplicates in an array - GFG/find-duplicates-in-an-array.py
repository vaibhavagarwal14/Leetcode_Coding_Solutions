class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	lst=[]
    	for i in range(n):
    	    arr[arr[i]%n]+=n
    	for i in range(n):
    	    if arr[i] >= 2*n:
    	        lst.append(i)
    	if not lst:
    	    return [-1]
    	return lst
    	
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends