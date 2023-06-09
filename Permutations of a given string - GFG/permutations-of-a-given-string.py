#User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        def permute(ch,ind,res):
            if(ind==len(ch)):
                str1=""
                res.append(str1.join(ch))
                return
            for i in range(ind,len(ch)):
                ch[i],ch[ind]=ch[ind],ch[i]
                permute(ch,ind+1,res)
                ch[i],ch[ind]=ch[ind],ch[i]
        res=[]
        ch=[*S]
        permute(ch,0,res)
        r=set(res)
        res=list(r)
        res.sort()
        return res
                
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends