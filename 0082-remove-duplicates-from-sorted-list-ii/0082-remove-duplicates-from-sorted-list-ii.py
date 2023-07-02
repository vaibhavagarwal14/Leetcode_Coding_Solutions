# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        n=0
        while curr!=None:
            curr=curr.next
            n+=1
        if n==0:
            return None
        prev=head
        curr=head
        new=0
        f=0
        while curr!=None:
            if curr.next!=None and curr.val == curr.next.val:
                if(curr==head):
                    new=1
                curr.next=curr.next.next
                f=1
            else:
                if(f==1):
                    prev.next=curr.next
                    curr=prev.next
                    f=0
                else:
                    prev=curr
                    curr=curr.next
        if(new==1):
            return head.next
        return head