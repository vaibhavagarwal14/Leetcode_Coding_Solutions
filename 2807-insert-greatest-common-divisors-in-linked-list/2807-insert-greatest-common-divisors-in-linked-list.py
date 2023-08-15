# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        first=head
        second=head.next
        while first.next:
            new=ListNode(gcd(first.val,second.val))
            first.next=new
            new.next=second
            first=second
            second=second.next
        return head