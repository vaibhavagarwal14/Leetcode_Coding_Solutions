#User function Template for python3
class Solution:
	def isDivisible(self, s):
	    # code here
		e=0
		o=0
		for i in range(len(s)):
		    if(s[i]=='1'):
		        if(i%2==0):
		            e+=1
		        else:
		            o+=1
		n=abs(e-o)
		if(n%3==0):
		    return 1
		else:
		    return 0


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.isDivisible(s)
		print(ans)

# } Driver Code Ends