#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        lst=[]
        arr.sort()
        for i in range(len(arr)):
            if i>0 and arr[i]==arr[i-1]:
                continue
            for j in range(i+1,len(arr)):
                if j!=i+1 and arr[j]==arr[j-1]:
                    continue
                l=j+1
                m=len(arr)-1
                while l<m:
                    s=arr[i]+arr[j]+arr[l]+arr[m]
                    if s>k:
                        m-=1
                    elif s<k:
                        l+=1
                    else:
                        lst.append([arr[i],arr[j],arr[l],arr[m]])
                        l+=1
                        m-=1
                        while l<m and arr[l]==arr[l-1]:
                            l+=1
                        while l<m and arr[m]==arr[m+1]:
                            m-=1
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends