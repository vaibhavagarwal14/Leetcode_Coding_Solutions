"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        n=0
        curr=head
        while curr!= None:
            n+=1
            if n==k:
                newhead=curr
            curr=curr.next
        if k==1:
            return head
        curr=head
        i=1
        while i<n+1:
            if i+k<=n+1:
                l=k
            else:
                l=n%k
            j=1
            prev=curr
            nxt=curr.next
            while j<l:
                t=nxt.next
                nxt.next=prev
                prev=nxt
                nxt=t
                if j==l-1 and curr!=head:
                    pc.next= prev
                j+=1
            pc=curr
            curr.next=nxt
            curr=nxt
            i+=k
        return newhead


#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends