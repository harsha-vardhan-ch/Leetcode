# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        d=ListNode(0)
        s=f=d
        s.next=head
        for i in range(n+1):
            print(f)
            f=f.next
            
        while f!=None:
            f=f.next
            s=s.next
        s.next=s.next.next
        print(s)
        return d.next
        