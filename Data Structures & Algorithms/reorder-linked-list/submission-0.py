# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head

        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        
        rev_l1 = self.reverse(l1.next)
        l1.next = None

        curr = head

        while curr and rev_l1:
            temp = curr.next
            curr.next = rev_l1
            curr = temp
            temp = rev_l1.next
            rev_l1.next = curr
            rev_l1 = temp
        
        

    
    def reverse(self,node) -> ListNode:
        curr = node
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



        