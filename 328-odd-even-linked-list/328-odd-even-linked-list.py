# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        even=head.next
        de=even
        c=head
        while even and even.next:
            c.next=c.next.next
            even.next=even.next.next
            even=even.next
            c=c.next
        c.next=de
        #print(head)
        return head