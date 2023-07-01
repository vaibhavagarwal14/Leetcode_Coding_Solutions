# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        n=0
        while curr != None:
            n+=1
            curr=curr.next
        if(n==0):
            return None
        if(k>n):
            k=k%n
        if(k==n or k==0):
            return head
        curr=head
        for i in range(n-1):
            curr=curr.next
        curr.next=head
        curr=head
        for i in range(n-k-1):
            curr=curr.next
        newhead=curr.next
        curr.next=None
        return newhead
        