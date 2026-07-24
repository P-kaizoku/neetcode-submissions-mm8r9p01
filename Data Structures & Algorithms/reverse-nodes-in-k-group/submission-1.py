# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_grp = dummy

        while True:
            kth = prev_grp
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            

            nxt_grp = kth.next
            prev, curr = nxt_grp, prev_grp.next
            while curr != nxt_grp:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            
            new_grp = prev_grp.next
            prev_grp.next = kth
            prev_grp = new_grp
        
        return dummy.next