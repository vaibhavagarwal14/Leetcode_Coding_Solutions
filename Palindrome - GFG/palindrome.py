#User function Template for python3

class Solution:
	def is_palindrome(self, n):
		# Code here
		c=n
		r=0
		while(n!=0):
		    d=n%10
		    r=r*10+d
		    n//=10
		if(c==r):
		    return "Yes"
		else:
		    return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends