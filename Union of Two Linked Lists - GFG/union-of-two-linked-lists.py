#User function Template for python3

class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        l1=[]
        l2=[]
        fin=[]
        while head1!=None:
            l1.append(head1.data)
            head1=head1.next
        while head2!=None:
            l2.append(head2.data)
            head2=head2.next
        i=0
        j=0
        l1.sort()
        l2.sort()
        
        while i!=len(l1) or j!=len(l2):
            if(i==len(l1)):
                while j<len(l2):
                    fin.append(l2[j])
                    j+=1
            elif(j==len(l2)):
                while i<len(l1):
                    fin.append(l1[i])
                    i+=1
            elif(l1[i]<=l2[j]):
                fin.append(l1[i])
                i+=1
            else:
                fin.append(l2[j])
                j+=1
        fin=list(set(fin))
        fin.sort()
        llfin=linkedList()
        for i in fin:
            llfin.insert(i)
        return llfin.head



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    for _ in range(int(input())):
        
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        ob = Solution()
        printList(ob.union(ll1.head,ll2.head))
        print()

# } Driver Code Ends