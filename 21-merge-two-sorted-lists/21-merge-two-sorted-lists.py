# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        r=ListNode(0)
        d=r
        while list1 and list2:
            if list1.val<list2.val:
                r.next=list1
                r=r.next
                list1=list1.next
            else:
                r.next=list2
                r=r.next
                list2=list2.next
        r.next=list1 or list2
        #print(d)
        return d.next