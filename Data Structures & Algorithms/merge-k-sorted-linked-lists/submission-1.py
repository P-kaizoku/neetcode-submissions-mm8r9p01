# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        return self.divide(lists, 0, len(lists)-1)

    
    def divide(self, lists, left, right):
        if left == right:
            return lists[left]
        
        mid = (left + right)//2
    
        l1 = self.divide(lists, left, mid)
        l2 = self.divide(lists, mid+1, right)
        
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        temp = ListNode()
        tail = temp

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        tail.next = l1 if l1 else l2

        return temp.next
            