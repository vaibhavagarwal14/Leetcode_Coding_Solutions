#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        lens=[]
        for i in arr:
            lens.append(len(i))
        mn=min(lens)
        s=""
        for i in range(mn):
            count=0
            d=arr[0][i]
            for j in arr:
                if(j[i]==d):
                    count+=1
            if(count==n):
                s+=d
            else:
                break
        if(len(s)==0):
            return -1
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends