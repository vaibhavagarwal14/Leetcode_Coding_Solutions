#User function Template for python3


def LargButMinFreq(arr,n):
    #code here
    count={}
    for i in arr:
        if i in count and count[i]!=0:
            count[i]+=1
        else:
            count[i]=1
    mn=min(count.values())
    lst=[key for key in count if count[key]==mn]
    return max(lst)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends