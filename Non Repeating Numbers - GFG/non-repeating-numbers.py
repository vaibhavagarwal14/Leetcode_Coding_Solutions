#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		z=0
		for i in nums:
		    z^=i
		z&=-z
		z1=0
		z2=0
		for i in nums:
		    if i&z>0:
		        z1^=i
		    else:
		        z2^=i
		l=[z1,z2]
		l.sort()
		return l



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends