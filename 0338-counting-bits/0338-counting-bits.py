class Solution:
    def countBits(self, n: int) -> List[int]:
        # Approach 1
        # if n==0:
        #     return [0]
        # if n==1:
        #     return [0,1]
        # if n==2:
        #     return [0,1,1]
        # if n==3:
        #     return [0,1,1,2]
        # arr=[0]*(n+1)
        # j=2
        # arr[1]=1
        # arr[2]=1
        # arr[3]=2
        # for i in range(4,n+1):
        #     if i==2**j:
        #         arr[i]=1
        #         j+=1
        #     else:
        #         arr[i]=arr[i-(2**(j-1))]+1
        # return arr
        
        # Approach 2 Bit Masking
        arr=[0]*(n+1)
        for i in range(1,n+1):
            arr[i]=arr[i//2] + (i&1)
        return arr