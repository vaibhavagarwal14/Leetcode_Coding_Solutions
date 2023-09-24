class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	for i in range(n):
    	    arr[arr[i]%n]+=n
    	lst=[]
    	for i in range(n):
    	    if arr[i]>=2*n:
    	        lst.append(i)
    	if len(lst)==0:
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